from flask import Flask, render_template
import subprocess

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('techkhazana.html')

@app.route('/run_script')
def run_script():
    result = subprocess.check_output(['python', 'run_script.py']).decode('utf-8')
    return result

if __name__ == '__main__':
    app.run(debug=True)
