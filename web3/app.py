from flask import Flask, render_template, request
import mlab
from register import Register
from gmail import GMail, Message
from random import choice
gmail = GMail('cookiedeptraivl@gmail.com','a06111997')
app = Flask(__name__)
mlab.connect()
@app.route("/add_register", methods = ["GET", "POST"])
def add_register():
    if request.method == "GET":
        #user request form
        return render_template("add_register.html")
    elif request.method == "POST":
        form = request.form 
        u = form["username"]
        p = form["password"]
        e = form["email"]     
        exist_user = Register.objects(username =  u).first()
        if exist_user != None:
            return "user already axists!"
        else:
            m = Register(username = u, password = p, email = e)
            m.save()
            template = '''<p>m&igrave;nh về m&igrave;nh c&oacute; nhớ ta&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
            <p>mười lăm năm ấy thiết tha mặn n&ocirc;ng&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-foot-in-mouth.gif" alt="foot-in-mouth" /></p>
            <p>m&igrave;nh về m&igrave;nh c&oacute; nhớ&nbsp; kh&ocirc;ng&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
            <p>nh&igrave;n c&acirc;y nhớ n&uacute;i nh&igrave;n s&ocirc;ng nhớ nguồn, h&acirc;y h&acirc;y h&acirc;y h&acirc;y&nbsp;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p> 
            '''
            message = Message('Chuc Mung', to= e, html= template)
            gmail.send(message)
            return "GOODDDDDDDDDDDDDD !!"
if __name__ == "__main__":
    app.run(debug=True)