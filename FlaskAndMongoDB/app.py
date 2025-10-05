from flask import Flask
import json

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/api")
def userList():
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return "No data Found"

if __name__ == "__main__":
    app.run(debug=True)