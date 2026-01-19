from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from conn import collection
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        try:
            existingUser = collection.find_one({"email":request.form["email"]})
            if existingUser:
                error = "Email already registered."
            else:
                data = {
                    "name": request.form["name"],
                    "email": request.form["email"]
                }
                collection.insert_one(data)
                return redirect(url_for("success"))
        except PyMongoError as e:
            error = f"Error submitting data: {str(e)}"
    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)