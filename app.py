from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    return render_template("map2.html")

@app.route("/comp", methods=['GET','POST'])
def compform():
    print request.method
    if request.method=="GET":
        return render_template('complaintform.html')
    if request.method=="POST":
        
        return "Complaint Submitted"

app.run(debug=True,host="0.0.0.0",port=5000)
