
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('p1.html')

@app.route('/patients')
def patients():
    return render_template('p2.html')

@app.route('/medications')
def medications():
    return render_template('p3.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
