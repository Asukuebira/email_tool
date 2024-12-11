
from flask import Flask, request, render_template, jsonify
from utils.bulk_breach_checker import check_breaches
from utils.osint_tool import perform_osint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bulk_breach_checker', methods=['GET', 'POST'])
def bulk_breach_checker():
    if request.method == 'POST':
        data = request.form['emails']
        result = check_breaches(data)
        return jsonify(result)
    return render_template('bulk_breach_checker.html')

@app.route('/osint_tool', methods=['GET', 'POST'])
def osint_tool():
    if request.method == 'POST':
        data = request.form
        result = perform_osint(data)
        return jsonify(result)
    return render_template('osint_tool.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
