import requests
import time
from flask import Flask, jsonify, request

url = "https://api.skyvern.com/api/v1/tasks"
headers = {""}

body = {"url": "https://www.portfoliovisualizer.com/monte-carlo-simulation",
        "navigation_goal": f"Enter the asset class and its allocations from the user payload and run simulation",
        "proxy_location": "RESIDENTIAL",
        "navigation_payload": {
            "US Stock Market": "40%",
            "10-year Treasury": "60%",
        },
        "data_extraction_goal": "Extract only the Portfolio Balance graph data, and the Expected Annual Return table"
    }

response = requests.post(url, headers=headers, json=body).json()
task_id = response.get("task_id")
iteration = 0
table_info = None
while response.get("status") != "COMPLETED" or iteration < 15:
    status_response = requests.get(f"{url}/{task_id}", headers=headers).json()
    table_info = status_response.get("expectedAnnualReturnTable")
    print(table_info)
    time.sleep(60)
    iteration += 1
    # print(response)

app = Flask(__name__)

@app.route('/query_api', methods=['POST'])
def query_api():

    data = request.get_json()
    if not data or 'navigation_payload' not in data:
        return jsonify({"error": "navigation_payload is required"}), 400
    
    body["navigation_payload"] = data["navigation_payload"]

    response = requests.post(url, headers=headers, json=body).json()
    task_id = response.get("task_id")
    iteration = 0
    table_info = None
    while response.get("status") != "COMPLETED" or iteration < 15:
        status_response = requests.get(f"{url}/{task_id}", headers=headers).json()
        table_info = status_response.get("expectedAnnualReturnTable")
        print(table_info)
        time.sleep(60)
        iteration += 1

    return jsonify(table_info)
        


if __name__ == '__main__':
    app.run(debug=True)
