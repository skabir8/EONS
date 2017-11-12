from flask import Flask, render_template, request
import utils.b_list
import utils.classify
import utils.geolocate
import utils.route_gen
import utils.cam_coors
import utils.complaint

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/map", methods=["POST"])
def map():
    start = request.form['start']
    #start = "858 Jamaica Ave, Brooklyn, NY 11208"
    end = request.form['end']
    #end = "C-Town Supermarkets, 241 Taaffe Pl, Brooklyn, NY 11205"
    data_dic = utils.route_gen.get_routes(start, end)
    print data_dic
    return render_template("map.html", data = data_dic)

@app.route("/pmap", methods=["GET","POST"])
def pmap():
    s = request.args.get('s')
    cl = request.args.get('cl')
    return s + cl

@app.route("/comp", methods=['GET','POST'])
def compform():
    print request.method
    if request.method=="GET":
        return render_template('complaintform.html')
    if request.method=="POST":
        complaint = request.form.get('complaint')
        address = request.form.get('location')
        utils.complaint.addComplaint(complaint,address)
        return "Complaint Submitted"

app.run(debug=True,host="0.0.0.0",port=5000)
