from flask import Flask,render_template,request,abort
from predict_temp import Weather_L2_Regularization



app = Flask(__name__)
tommorow = Weather_L2_Regularization()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    high = request.form.get('high')
    low = request.form.get('low')

    if not(high.isnumeric() and low.isnumeric()):
        return abort(404)

    high,low = tommorow.predict(int(high),int(low))
    return f"<h1> tommorows high: {high} tomorrows low: {low}<h1>"
    


    



