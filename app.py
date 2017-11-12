from flask import Flask, render_template, request
import utils.b_list
import utils.classify
import utils.geolocate
import utils.route_gen
import utils.cam_coors

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    data_dic = utils.route_gen.get_routes("858 Jamaica Ave, Brooklyn, NY 11208", "C-Town Supermarkets, 241 Taaffe Pl, Brooklyn, NY 11205")

    return render_template("map.html", data = data_dic)

@app.route("/comp", methods=['GET','POST'])
def compform():
    print request.method
    if request.method=="GET":
        return render_template('complaintform.html')
    if request.method=="POST":

        return "Complaint Submitted"

app.run(debug=True,host="0.0.0.0",port=5000)
