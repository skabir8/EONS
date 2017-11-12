from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    return render_template("map2.html")

@app.route("/comp")
def compform():
    return render_template('complaintform.html')


app.run(debug=True,host="0.0.0.0",port=5000)
