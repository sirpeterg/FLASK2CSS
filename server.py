from flask import Flask, render_template, request
from random import randint
from threading import Timer
import webbrowser

app = Flask(__name__)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


@app.route("/", methods = ["GET","POST"])  
def home():
    if request.method == "GET":
        color = '#{:02x}{:02x}{:02x}'.format( 150, 150, 150 ) # I use hex formating for colors
        return render_template("index.html", color = color[0])
    elif request.method == "POST":
        RGBcolor = [randint(0, 255), randint(0, 255), randint(0, 255)]
        color ='#{:02x}{:02x}{:02x}'.format( RGBcolor[0], RGBcolor[1] , RGBcolor[2] ) # I use hex formating for colors
        return render_template("index.html", color = color)


if __name__ == "__main__":
    Timer(1, open_browser).start() # waits a second and then opens the browser at port 20000
    app.run(debug=True, port=2000, use_reloader=False)