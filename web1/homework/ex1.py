from flask import Flask, render_template
app = Flask(__name__)

@app.route("/about-me")
def about_me():
    list_titles  = [
        "Ten",
        "Co quan",
        "Truong",
        "so thich",
    ]
    
    return render_template("post1.html", titles = list_titles)
if __name__ == "__main__":
    app.run(debug=True)
