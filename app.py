from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        name="Max Dokukin",
        tagline="Student at SJSU",
        email="max.dokukin@sjsu.edu",  # change if needed
    )

if __name__ == "__main__":
    app.run(debug=True)
