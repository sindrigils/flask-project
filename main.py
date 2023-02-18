from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bangaluru, India",
        "salary": "Rs. 1,00,00"
    },

    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 12,00,00"
    },

    {
        "id": 3,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$120,000"
    }
]

@app.route("/")
def print_hello():
    return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=(8080))