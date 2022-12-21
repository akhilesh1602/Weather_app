from flask import Flask , render_template, request
import requests
app = Flask(__name__)

@app.route("/" , methods=['post','get'] )
def home():
    user_input = request.form.get('user_input')
    k=str(user_input)
    complete_api_link1 ="http://api.openweathermap.org/geo/1.0/direct?q="+k+"&limit=5&appid=52e40abca47fa344472973b265b5c319"
    location = requests.get(complete_api_link1)
    #print(location.status_code)
    loc = location.json()
    #print(location.text)
    a=float(loc[2]['lat'])
    b=float(loc[2]['lon'])
    lat = str(a)
    lon = str(b)
    complete_api_link ="https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=52e40abca47fa344472973b265b5c319"
    a = requests.get(complete_api_link)
    data = a.json()
    #print(a.status_code)
    #print(data)
    temp1 = data['main']['temp']
    temp2 = data['main']['temp_min']
    temp3 = data['main']['temp_max']
    temp4 = data['main']['humidity']
    temp5 = data['main']['pressure']
    temp6 = data['wind']['speed']
    result=[]
    result.append(temp1)
    result.append(temp2)
    result.append(temp3)
    result.append(temp4)
    result.append(temp5)
    result.append(temp6)
    return render_template('index.html',data=result)

app.run(debug=True)


