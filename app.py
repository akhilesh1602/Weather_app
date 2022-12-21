from flask import Flask , render_template, request
import requests
app = Flask(__name__)

@app.route("/" , methods=['POST','GET'] )
def home():
    if request.method== 'POST': 
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
        temp1 = '%.2f' % (abs(data['main']['temp']-273))
        temp2 = '%.4f' % (abs(data['main']['temp_min']-273))
        temp3 = '%.4f' % (abs(data['main']['temp_max']-273))
        temp4 = data['main']['humidity']
        temp5 = data['main']['pressure']
        temp6 = data['wind']['speed']
        temp7 = data['wind']['deg']
        temp8 = data['weather'][0]['description']
        temp9 = data['visibility']
        temp10 = data['weather'][0]['main']
        result=[]
        result.append(temp1)
        result.append(temp2)
        result.append(temp3)
        result.append(temp4)
        result.append(temp5)
        result.append(temp6)
        result.append(temp7)
        result.append(temp8)
        result.append(temp9)
        result.append(temp10)
        return render_template('search.html',data=result)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)


