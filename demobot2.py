# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/', methods=['GET', 'POST'])
def hello_you():
    return 'Hello, You!'

@app.route('/ncss', methods=['GET', 'POST'])
def hello_NCSS():
    return '<h1> NCSS </h1> NCSS'

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'Hi {name}!'

@app.route('/weather', methods=['GET', 'POST'])
def show_weather():
    weather = request.values.get('text')
    if int(weather) > 30:
        return 'It\'s very hot.'
    else:
        return f"The temperature is {weather}."

if __name__ == '__main__':
    # Start the web server!
    app.run(debug = True)
