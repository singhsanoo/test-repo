from flask import Flask, render_template, redirect
from flask import Response
# from werkzeug.datastructures import Headers
# from bs4 import BeautifulSoup
# from flask_restful import Resource, Api





#############################################################
# BEGIN FLASK ROUTING
#############################################################

app = Flask(__name__)
# app.config["JSON_SORT_KEYS"] = False
# app.config["SEND_FILE_MAX_PAGE_DEFAULT"] = 0

#############################################################
# Index endpoint
#############################################################

@app.route("/")
def index():
    
    return render_template("index.html")     

#############################################################

@app.route("/opt1")
def new1():
    return redirect("/", code=302)    
    # return render_template("map.html")    http://127.0.0.1:5000/opt1

# @app.route("/opt2")
# def new2():
#     return render_template("new.html")

@app.route("/opt2")
def new2():
   return render_template("volcano.html")

@app.route("/opt3")
def new3():
   return render_template("year.html")

#############################################################










#############################################################
# END FLASK ROUTING
#############################################################
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')