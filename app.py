from flask import Flask, render_template, request
import utils.b_list
import utils.classify
import utils.geolocate
import utils.route_gen
import utils.cam_coors
import utils.complaint
import polyline
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
    s = request.args.get('cams')
    cl = request.args.get('route')
    all_c = s.split(',')[1:-2]
    all_lists =[]
    summ = 0
    for x in all_c:
        all_lists.append('http://nyctmc.org/google_popup.php?cid='+ x)
    summ = utils.classify.get_all_cams(all_lists)
    pol_val = polyline.decode(cl)
    origin = pol_val[0]
    destination = pol_val[-1]
    ret_dic = {}
    ret_dic['origin'] = origin
    ret_dic['destination'] = destination
    poly_line_array= [pol_val]
    rets=[]
    for i in poly_line_array:
        ret_val = ''
        for vals in i:
            ret_val += '{lat: ' + str(vals[0]) + ',' + 'lng: ' + str(vals[1])+'}, '
        ret_val = ret_val[:-2]
        rets.append(ret_val)
    data_dic = ret_dic
    ret_dic['way1'] = rets[0]
    ret_dic['safe'] = summ
    print(data_dic)
    return render_template("map2.html", data = data_dic)
    #print (summ)


    #print (all_c)
    #print cl
    #return "lol"

@app.route("/comp", methods=['GET','POST'])
def compform():
    #print request.method
    if request.method=="GET":
        return render_template('complaintform.html')
    if request.method=="POST":
        complaint = request.form.get('complaint')
        address = request.form.get('location')
        utils.complaint.addComplaint(complaint,address)
        return "Complaint Submitted"

app.run(debug=True,host="0.0.0.0",port=5000)
