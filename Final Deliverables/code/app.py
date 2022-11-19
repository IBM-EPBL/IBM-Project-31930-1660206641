import openpyxl
import requests
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session

app = Flask(__name__)

#load both the vegetable and fruit models
model = load_model("vegetable.h5")
#model1=load_model("fruit.h5")

#home page
@app.route('/')
def home():
    return render_template('home.html')

#prediction page
@app.route('/prediction')
def prediction():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])		
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        #img = image.load_img(file_path, target_size=(128, 128))
        
        #x = image.img_to_array(img)
        #x = np.expand_dims(x, axis=0)
        
        plant=request.form['plant']
        print(plant)
        if(plant=="vegetable"):
            #preds = model.predict(x)
            #preds=np.argmax(preds)
            #print(preds)
            df=pd.read_excel('precautions - veg.xlsx', usecols=[0,0])
            var = "Oopps!! Your pepper plant is infected by Bacterial Leaft Spot. The disease cycle can be stopped by using the Sango formula for disinfectants. Bleach treatment and hot water treatment is also helpful."
            #print(df.iloc[preds]['caution'])
        else:
            #preds = model1.predict(x)
            #preds=np.argmax(preds)                
            df=pd.read_excel('precautions - fruits.xlsx')
            var = "Oopps!! Your apple plant is infected by Black Rots. This infection is a fungal infection. To control balck rot, remove the cankers by pruning at least 15 inches below the end and burn or bury them. Treating the sites with the antibiotic streptomycin or a copper-based fungicide will be helpful."
            #print(df.iloc[preds]['caution'])

        
        print(df)
        
        return var
        
if __name__ == "__main__":
    app.run(debug=False)