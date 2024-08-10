from flask import Flask,render_template,request,abort,session
from predict_temp import Weather_L2_Regularization
from api import real_time_temp_data



app = Flask(__name__)
tommorow = Weather_L2_Regularization()
app.secret_key = 'super secure'




@app.route('/',methods =['POST'])
def index():
    
    #only allow 1 api call per session
    if 'low' not in session or  'high' in session:
        curr_temp_min,curr_temp_max = real_time_temp_data()
        curr_temp_class = get_class(int((curr_temp_max + curr_temp_min)/2))
        print(curr_temp_class)
        session['back'] = curr_temp_class
        session['low'] = (curr_temp_min)
        session['high'] = (curr_temp_max)
    
    return render_template('index.html',curr_temp_min=curr_temp_min, curr_temp_max=curr_temp_max,temp_class = curr_temp_class)


@app.route('/predict',methods = ['POST','GET'])
def predict():
   
    if session.get('low') is None or session.get('high') is None:
        return abort(404)

    curr_temp_max = session['high']
    curr_temp_min = session['low']
    pred_temp_max,pred_temp_min = tommorow.predict(curr_temp_max,curr_temp_min)
    pred_temp_class = get_class(int((pred_temp_min + pred_temp_max) / 2))
    print(pred_temp_class)
    return render_template('page.html',curr_temp_min=pred_temp_min, curr_temp_max=pred_temp_max,temp_class = pred_temp_class)
    


    
def get_class(temp: int) -> str:

    if temp <= 30:
        return "cold"
    elif 31 <= temp <=50:
        return "chilly"
    elif 51 <= temp <= 70: 
        return "warm"
    elif temp >= 71:
        return "hot"
    else:
        return "null"



