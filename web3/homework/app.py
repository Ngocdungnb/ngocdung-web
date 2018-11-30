from flask import Flask, render_template,request
import mlab
from bike import Bike



app = Flask(__name__)
mlab.connect()
@app.route("/new_bike", methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template ("add_bike.html")
    else:
        form = request.form 
        m = form["Model"]
        d = form["Dailyfee"]
        i = form["Image"]
        y = form["Year"]
        n = Bike(Model = m, Dailyfee = d, Image = i, Year = y)
        n.save()
        return "Ahihi DO ngoc", print(n)

if __name__ == "__main__":  
    app.run(debug=True)

