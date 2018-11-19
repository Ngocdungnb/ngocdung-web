from flask import Flask, template_rendered
app = Flask(__name__)
@app.route("/user/<username>")
def files(username):
    users_list = {
        "rua" : {
            "name" : " Ngoc Rua ",
            "age" : 12,
        },
        "bo" : {
            "name" : "  Ngoc Bo ",
            "age" : 15,
        },
        "trau" : {
            "name" : " Ngoc Trau ",
            "age" : 16,
        },
        "tho" : {
            "name" : " Ngoc Tho ",
            "age" : 18,
        },
    }
    
    if username in users_list:
        return render_template("hoso.html",files = users_list[username] )
    else:
        return "User not found"

if __name__ == "__main__":
    app.run(debug=True)