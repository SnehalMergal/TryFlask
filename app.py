# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:15:26 2022

@author: 91898
"""

from flask import Flask,render_template,request,flash

app=Flask(__name__)
app.secret_key="anypassword"

@app.route("/hello")
def index():
    flash("Quora duplicate Predict")
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    flash("hi" + str(request.form["question1_input"]) + ",great to see you")
    return render_template("index.html")