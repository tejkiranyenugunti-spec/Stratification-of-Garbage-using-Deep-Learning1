from flask import Flask, request,flash,render_template,send_from_directory,redirect,url_for
from tensorflow.keras.preprocessing import image
import os
from tensorflow.keras.models import load_model
import numpy as np
import mysql.connector
import pandas as pd
import cv2
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import shutil


app=Flask(__name__)
app.secret_key='random string'

classes=['Cardboard','Glass','Metal','Paper','Plastic','Trash']

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="garbage_classification"
)
mycursor = mydb.cursor()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/regback',methods = ["POST"])
def regback():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        addr=request.form['addr']

        sql = "select * from ureg"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed", "success")
            return render_template('index.html')
        if (pwd == cpwd):
            sql = "INSERT INTO ureg (name,email,pwd,addr) VALUES (%s,%s,%s,%s)"
            val = (name, email, pwd, addr)
            mycursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "warning")
            return render_template('index.html')
        else:
            flash("Password and Confirm Password not same")

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logback',methods=['POST', 'GET'])
def logback():
    if request.method == "POST":

        email = request.form['email']

        password1 = request.form['pwd']
        print('p')

        sql = "select * from ureg where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()
        print(results)
        global name

        if len(results) > 0:

            flash("Welcome ", "primary")
            return render_template('userhome.html', msg=results[0][1])
        else:
            flash("Invalid Credentials ", "danger")
            return render_template('index.html')

    return render_template('index.html')

@app.route('/userhome')
def userhome():
    return render_template("userhome.html")

@app.route('/upload')
def upload():

    return render_template("upload.html")

@app.route('/upload1/<filename>')
def send_image(filename):

    return send_from_directory("images", filename)

@app.route("/upload1", methods=["POST","GET"])
def upload1():
    print('a')

    # myfile = request.files['file']
    # fn = myfile.filename
    # mypath = os.path.join('D:/Fathima/Python/garbage classification/images/', fn)
    # myfile.save(mypath)
    #
    # print("{} is the file name", fn)
    # print("Accept incoming file:", fn)
    # print("Save it to:", mypath)
    # # import tensorflow as tf
    # import numpy as np
    # from keras.preprocessing import image
    # from keras.models import load_model
    # # img = r"D:\Fathima\Python\deforestation\dataset\test\deforestation\4.jpg"
    # new_model = load_model(r"D:\Fathima\Python\garbage classification\CNN.h5")
    # test_image = image.load_img(mypath, target_size=(64, 64))
    # test_image = image.img_to_array(test_image)
    # test_image = np.expand_dims(test_image, axis=0)
    # result = new_model.predict(test_image)
    #
    # prediction = classes[np.argmax(result)]
    # return render_template("template.html", image_name=fn, text=prediction)




    if request.method=='POST':
        myfile=request.files['f1']
        fn=myfile.filename
        print(type(fn))
        mypath=os.path.join('images/', fn)
        myfile.save(mypath)

        print("{} is the file name",fn)
        print ("Accept incoming file:", fn)
        print ("Save it to:", mypath)
        #import tensorflow as tf
        img = cv2.imread(mypath)
        # mypath=r"D:\RICE LEAF DISEASE DETECTION\imges\Blast_IMG_0_32.jpg"
        # dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        #

        new_model = load_model(r"CNN.h5")
        test_image = image.load_img(mypath, target_size=(64,64))
        test_image = image.img_to_array(test_image)
        test_image=test_image/255
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        classes=['Cardboard','Glass','Metal','Paper','Plastic','Trash']
        # prediction=np.argmax(result)
        prediction = classes[np.argmax(result)]
    return render_template("template.html", text=prediction ,image_name=fn)


if __name__=='__main__':
    app.run(debug=True)