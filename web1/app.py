from flask import Flask, render_template
app = Flask(__name__)

#function binding
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello c4e, Hoho"

@app.route("/me")
def me():
    return "Khoai To Dep Zai"

@app.route("/hi/<name>")
def hi_khai(name):
    return "Hello " + name

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a +b
    return str(s)


@app.route("/posts/<int:index>/<int:cont>")
def posts(index,cont):
    titles=[
        "troi nang qua",
        "sap bao roi kia",
        "troi nhieu may qua",
    ]
    content = [
        "di choi thoi",
        "o nha ngu",
        "xoac nao",
    ]
    c = content[cont]
    t = titles[index]
    return render_template("post.html", titles = t , content = c)


@app.route("/movie")
def movie():
    return render_template("movie.html", name = "Sieu nhan", img = "https://www.xosothantai.com/data/avatars/l/478/478541.jpg?1536834318")

@app.route("/movies")
def movies():
#     movie_titles = [
#         "sieu nhan gao",
#         "sieu nhan cuong phong",
#         "sieu nhan da quang",
#     ]
    movie_list = [ 
        {
            "title" : "sieu nhan gao",
            "image" : "https://www.xosothantai.com/data/avatars/l/478/478541.jpg?1536834318",
        },
        {
            "title" : "sieu nhan cuong phong",
            "image" : "https://i.ytimg.com/vi/XMGwkfuSoNs/hqdefault.jpg",
        },
        {
            "title" : "sieu nhan cuong phong",
            "image" : "https://i.ytimg.com/vi/AiP-dKxX-aE/maxresdefault.jpg"
        }
    ]
    return render_template("movies.html", movies = movie_list )
if __name__ == "__main__":
    app.run(debug=True)