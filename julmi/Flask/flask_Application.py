from flask import Flask, render_template

#WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1><b>Welcome to the Flask!</h1></b>"

@app.route("/index")
def hello():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)