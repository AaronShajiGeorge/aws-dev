from flask import Flask, render_template
import socket,getpass,platform
from datetime import datetime
app=Flask(__name__)
@app.route("/")
def home():
 return render_template("index.html",hostname=socket.gethostname(),username=getpass.getuser(),python=platform.python_version(),time=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
@app.route("/about")
def about(): return render_template("about.html")
@app.route("/contact")
def contact(): return render_template("contact.html")
if __name__=="__main__": app.run(host="0.0.0.0",port=5000)
