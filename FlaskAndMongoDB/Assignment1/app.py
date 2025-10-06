from flask import Flask, jsonify
import json

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/api")
def userList():
    try:
        with open("users1.json", "r") as f:
            data = json.load(f)
            return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({'error': "No data Found"}), 404

if __name__ == "__main__":
    app.run(debug=True)