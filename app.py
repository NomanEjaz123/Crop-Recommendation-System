
from flask import Flask, redirect, url_for, request, session
from flask import render_template
import pickle 
import numpy as np




crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))




app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"





if __name__ == '__main__':
    app.run(debug=True)



 

@app.route("/")
def first():
    return render_template('firstpage.html')


@app.route("/main")
def index():
    return render_template('index.html')

@app.route("/crop")
def crop():
    return render_template('crop.html')




@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Crop Recommendation System'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temp=int(request.form['temperature'])
        humi=int(request.form['humidity'])


        
        data = np.array([[N, P, K, ph, rainfall, temp, humi]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('crop-result.html', prediction=final_prediction, title=title)

    else:

        return render_template('try_again.html', title=title)

     