from flask import Flask, render_template
from led_control import toggle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/toggle_led')
def toggle_led():
    toggle()
    return ''