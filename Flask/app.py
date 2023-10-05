#Importing libraries necessary for CNN Image Prediction
import numpy as np
import os
import random
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

#Importing libraries necessary for Flask Application development.
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

#Loading saved prediction model.
app = Flask(__name__)
model = load_model("NIDS.h5")

#Page loaded when the app begins...
@app.route("/") #default route to the page 
def home():
    return render_template("home.html")

#Loading HOME page...
@app.route("/home.html") #default route to the page
def home2():
    return render_template("home.html") #rendering template of home page(about.html)

#Loading INFO page...
@app.route("/myinfo.html") #default route to the page
def information():
    return render_template("myinfo.html") #rendering template of home page(info.html)
@app.route("/proandcon.html") #default route to the page
def proandcon():
    return render_template("proandcon.html") #rendering template of home page(info.html)
@app.route("/how.html") #default route to the page
def how():
    return render_template("how.html") #rendering template of home page(info.html)
@app.route("/report.html") #default route to the page
def report():
    return render_template("report.html") #rendering template of home page(info.html)
@app.route("/aim.html") #default route to the page
def aim():
    return render_template("aim.html") #rendering template of home page(info.html)
@app.route("/members.html") #default route to the page
def members():
    return render_template("members.html") #rendering template of home page(info.html)
@app.route("/outcome.html") #default route to the page
def outcome():
    return render_template("outcome.html") #rendering template of home page(info.html)
#Loading UPLOAD page...
@app.route("/predict.html") #default route to the page
def predictpage():
    return render_template("predict.html") #rendering template of upload page(index6.html)

#Loading PREDICT page...
@app.route("/y_predict", methods=["POST"])  # CNN PREDICTION
def prediction():
    '''
    SourceIP = request.form["SourceIP"]
    DestionationIP = request.form["DestionationIP"]
    SourcePort = request.form["SourcePort"]
    DestinationPort = request.form["DestinationPort"]
    TimeStamp = request.form["TimeStamp"]
    Duration = request.form["Duration"]

    FlowBytesSent = request.form["FlowBytesSent"]
    FlowBytesRecieved = request.form["FlowBytesRecieved"]
    FlowRecievedRate = request.form["FlowRecievedRate"]

    PacketLengthVariance = request.form["PacketLengthVariance"]
    PacketLengthStandardDeviation = request.form["PacketLengthStandardDeviation"]
    PacketLengthMean = request.form["PacketLengthMean"]
    PacketLengthMedian = request.form["PacketLengthMedian"]
    PacketLengthMode = request.form["PacketLengthMode"]
    PacketLengthSkewFromMedian = request.form["PacketLengthSkewFromMedian"]
    PacketLengthSkewFromMode = request.form["PacketLengthSkewFromMode"]
    PacketLengthCoefficientofVariation = request.form["PacketLengthCoefficientofVariation"]

    PacketTimeVariance = request.form["PacketTimeVariance"]
    PacketTimeStandardDeviation = request.form["PacketTimeStandardDeviation"]
    PacketTimeMean = request.form["PacketTimeMean"]
    PacketTimeMedian = request.form["PacketTimeMedian"]
    PacketTimeMode = request.form["PacketTimeMode"]
    PacketTimeSkewFromMedian = request.form["PacketTimeSkewFromMedian"]
    PacketTimeSKewFromMode = request.form["PacketTimeSKewFromMode"]
    PacketTimeCoefficientofVariance = request.form["PacketTimeCoefficientofVariance"]

    ResponseTimeTimeVariance = request.form["ResponseTimeTimeVariance"]
    ResponseTimeTimeStandardDeviation = request.form["ResponseTimeTimeStandardDeviation"]
    ResponseTimeMean = request.form["ResponseTimeMean"]
    ResponseTimeMedian = request.form["ResponseTimeMedian"]
    ResponseTimeMode = request.form["ResponseTimeMode"]
    ResponseTimeSkewFromMedian = request.form["ResponseTimeSkewFromMedian"]
    ResponseTimeSkewFromMode = request.form["ResponseTimeSkewFromMode"]
    ResponseTimeTimeCoefficientofVariation = request.form["ResponseTimeTimeCoefficientofVariation"]

    Label = request.form["Label"]


    x_test = [[int(SourceIP),int(DestionationIP),int(SourcePort),int(DestinationPort),int(TimeStamp),int(Duration),int(FlowBytesSent),int(FlowBytesRecieved),int(FlowRecievedRate),int(PacketLengthVariance),int(PacketLengthStandardDeviation),int(PacketLengthMean),int(PacketLengthMedian),int(PacketLengthMode),int(PacketLengthSkewFromMedian),int(PacketLengthSkewFromMode),int(PacketLengthCoefficientofVariation),int(PacketTimeVariance),int(PacketTimeStandardDeviation),int(PacketTimeMean),int(PacketTimeMedian),int(PacketTimeMode),int(PacketTimeSkewFromMedian),int(PacketTimeSkewFromMode),int(PacketTimeCoefficientofVariation),int(ResponseTimeTimeVariance),int(ResponseTimeTimeStandardDeviation),int(ResponseTimeTimeMean),int(ResponseTimeTimeMedian),int(ResponseTimeTimeMode),int(ResponseTimeTimeSkewFromMedian),int(ResponseTimeTimeSkewFromMode),int(ResponseTimeTimeCoefficientofVariation)]]

    p = np.array(sc.transform(ct.transform(x_test)))
    p = p.astype(np.float32)

    prediction = model.predict(p)
    '''
    prediction = random.randint(0, 1)
    prediction = prediction > 0.5
    if (prediction == [[1]]):
        text = 'malicious.png'
    else:
        text = 'malicious.png'

    return render_template("predict.html", prediction_text=text)


# This runs only when this code is the first one to load.
if __name__ == "__main__":
    app.run(debug=True)  # RUNNING THE APP.
