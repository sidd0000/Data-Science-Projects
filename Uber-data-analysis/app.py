
# # import nbformat

# # # Path to the uploaded notebook file
# # notebook_path = "./Uber Data Analysis - simple version.ipynb"

# # # Load the Jupyter notebook file
# # with open(notebook_path, 'r', encoding='utf-8') as f:
# #     notebook = nbformat.read(f, as_version=4)

# # # Extract the content of cells (markdown, code, and outputs)
# # parsed_data = []
# # for cell in notebook['cells']:
# #     if cell['cell_type'] == 'markdown':
# #         parsed_data.append({'type': 'markdown', 'content': cell['source']})
# #     elif cell['cell_type'] == 'code':
# #         outputs = []
# #         for output in cell.get('outputs', []):
# #             if 'text' in output:
# #                 outputs.append(output['text'])
# #             elif 'data' in output and 'text/plain' in output['data']:
# #                 outputs.append(output['data']['text/plain'])
# #         parsed_data.append({'type': 'code', 'content': cell['source'], 'outputs': outputs})

# # # Display the structure of the parsed data in the terminal
# # for entry in parsed_data:
# #     print(entry)
# import nbformat
# from flask import Flask, jsonify, send_file
# import matplotlib.pyplot as plt
# import pandas as pd
# import io
# from flask_cors import CORS


# app = Flask(__name__)
# CORS(app)
# # Step 1: Parse the Jupyter Notebook
# # Path to the notebook file
# notebook_path = "./Uber Data Analysis - simple version.ipynb"

# # Load the notebook file
# with open(notebook_path, 'r', encoding='utf-8') as f:
#     notebook = nbformat.read(f, as_version=4)

# # Extract the content of cells (markdown, code, and outputs)
# parsed_data = []
# for cell in notebook['cells']:
#     if cell['cell_type'] == 'markdown':
#         parsed_data.append({'type': 'markdown', 'content': cell['source']})
#     elif cell['cell_type'] == 'code':
#         outputs = []
#         for output in cell.get('outputs', []):
#             if 'text' in output:
#                 outputs.append(output['text'])
#             elif 'data' in output and 'text/plain' in output['data']:
#                 outputs.append(output['data']['text/plain'])
#         parsed_data.append({'type': 'code', 'content': cell['source'], 'outputs': outputs})

# # Step 2: Simulated Data and Logic (Replace with logic from notebook if needed)
# # Example DataFrame (Replace with parsed data or actual dataset)
# data = pd.DataFrame({
#     "hour": [0, 1, 2, 3],
#     "trips": [100, 200, 150, 250],
#     "weekday": ["Monday", "Tuesday", "Wednesday", "Thursday"],
# })

# # Step 3: Flask Routes
# @app.route("/data", methods=["GET"])
# def get_data():
#     """
#     API Endpoint to return data as JSON
#     """
#     return jsonify(data.to_dict(orient="records"))

# @app.route("/plots/hours", methods=["GET"])
# def plot_hours():
#     """
#     Generate and return 'Trips by Hour' chart
#     """
#     plt.figure(figsize=(8, 6))
#     plt.bar(data["hour"], data["trips"])
#     plt.title("Trips by Hour")
#     plt.xlabel("Hour")
#     plt.ylabel("Number of Trips")
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format="png")
#     buffer.seek(0)
#     return send_file(buffer, mimetype="image/png")

# @app.route("/plots/weekday", methods=["GET"])
# def plot_weekday():
#     """
#     Generate and return 'Trips by Weekday' chart
#     """
#     plt.figure(figsize=(8, 6))
#     plt.bar(data["weekday"], data["trips"])
#     plt.title("Trips by Weekday")
#     plt.xlabel("Weekday")
#     plt.ylabel("Number of Trips")
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format="png")
#     buffer.seek(0)
#     return send_file(buffer, mimetype="image/png")

# # Step 4: Print parsed data for debugging
# @app.route("/debug/parsed", methods=["GET"])
# def debug_parsed():
#     """
#     API Endpoint to return the parsed notebook data for debugging
#     """
#     return jsonify(parsed_data)

# # Step 5: Run the Flask Application
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)
from flask import Flask, jsonify, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io

app = Flask(__name__)

# Example Data Loading
# Replace this with data from the parsed notebook
data = pd.DataFrame({
    "hour": [0, 1, 2, 3],
    "trips": [100, 200, 150, 250],
    "weekday": ["Monday", "Tuesday", "Wednesday", "Thursday"],
})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data.to_dict(orient="records"))

@app.route("/plots/hours", methods=["GET"])
def plot_hours():
    plt.figure(figsize=(8, 6))
    plt.bar(data["hour"], data["trips"])
    plt.title("Trips by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Number of Trips")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return send_file(buffer, mimetype="image/png")

@app.route("/plots/weekday", methods=["GET"])
def plot_weekday():
    plt.figure(figsize=(8, 6))
    plt.bar(data["weekday"], data["trips"])
    plt.title("Trips by Weekday")
    plt.xlabel("Weekday")
    plt.ylabel("Number of Trips")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
