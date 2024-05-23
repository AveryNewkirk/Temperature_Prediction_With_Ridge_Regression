import pandas as pd
from sklearn.linear_model import Ridge
#from sklearn.metrics import mean_absolute_error

class Weather_L2_Regularization():

  #iniialize the class with all the essentials
  def __init__(self):

    weather = pd.read_csv('Charlotte_Douglas_Weather_Dataset.csv', index_col='DATE')
    self.real_weather = self.clean_data(weather)
    self.real_weather.index = pd.to_datetime(self.real_weather.index)


    self.reg_max = Ridge(alpha=.1)
    self.reg_min = Ridge(alpha=.1)
    self.real_weather = self.clean_data(weather)
    self.features = ['precip', 'snow', 'snow_depth', 'temp_max','temp_min','month_min','month_day_max','month_day_min','max_min']
    self.train_data()


  def train_data(self):
    train = self.real_weather.loc[:'2022-12-31']
    #test = self.real_weather.loc['2023-01-01':]

    self.reg_max.fit(train[self.features], train['target_max'])
    self.reg_min.fit(train[self.features], train['target_min'])


    
  def clean_data(self,dataframe: pd.DataFrame) -> pd.DataFrame:
    #Clean the data and add some feilds to help improve the ridge regression
    real_weather = dataframe[['PRCP','SNOW','SNWD','TMAX','TMIN']].copy()
    real_weather.columns = ['precip', 'snow', 'snow_depth', 'temp_max','temp_min']
    real_weather.index = pd.to_datetime(real_weather.index)
    real_weather['target_max'] = real_weather.shift(-1)['temp_max']
    real_weather['target_min'] = real_weather.shift(-1)['temp_min']
    real_weather = real_weather.iloc[:-1,:].copy()


    #get the mean of the last 30 days for that given data point
    real_weather['month_max'] = real_weather['temp_max'].rolling(30).mean()
    real_weather['month_min'] = real_weather['temp_min'].rolling(30).mean()

    #ratio of how diferent the mean temp is from the temp on a given day
    real_weather['month_day_max'] = real_weather['month_max'] / real_weather['temp_max']
    real_weather['month_day_min'] = real_weather['month_min'] / real_weather['temp_min']


    #check the ratio of the maximum and minimum temp on a given day
    real_weather['max_min'] = real_weather['temp_max'] / real_weather['temp_min']


    #take off the last 30 days of the dataset as its full of NaNa
    real_weather = real_weather.iloc[30:,:].copy()

    return real_weather


  def predict(self,today_temp_max,today_temp_min,today_percip=0,today_snow=0,today_snow_depth=0):

    today = self.real_weather.iloc[-1].copy()
    today['percip'] = today_percip
    today['snow'] = today_snow
    today['snow_depth'] = today_snow_depth
    today['temp_max'] = today_temp_max
    today['temp_min'] = today_temp_min
    today['month_max'] = self.real_weather['temp_max'].rolling(30).mean().iloc[-1]
    today['month_min'] = self.real_weather['temp_min'].rolling(30).mean().iloc[-1]
    today['month_day_max'] = today['month_max'] / today_temp_max
    today['month_day_min'] = today['month_min'] / today_temp_min
    today['max_min'] = today_temp_max / today_temp_min


    features = today[self.features].values.reshape(1,-1)

    pred_max = self.reg_max.predict(features)[0]
    pred_min = self.reg_min.predict(features)[0]


    return int(pred_max),int(pred_min)
  



