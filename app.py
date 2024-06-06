from flask import Flask,render_template,request,abort,session
from predict_temp import Weather_L2_Regularization
from api import real_time_temp_data



app = Flask(__name__)
tommorow = Weather_L2_Regularization()
app.secret_key = 'super secure'




@app.route('/')
def index():
    
    #only allow 1 api call per session
    if 'low' not in session or  'high' in session:
        curr_temp_min,curr_temp_max = real_time_temp_data()
        session['low'] = (curr_temp_min)
        session['high'] = (curr_temp_max)
    
    return render_template('index.html',curr_temp_min=curr_temp_min, curr_temp_max=curr_temp_max)


@app.route('/predict',methods = ['POST','GET'])
def predict():
   
    if session.get('low') is None or session.get('high') is None:
        return abort(404)

    high = session['high']
    low = session['low']
    high,low = tommorow.predict(high,low)
    return f"<h1> tommorows high: {high} tomorrows low: {low}<h1>"
    


    



