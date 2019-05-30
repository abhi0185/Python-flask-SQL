from flask import Flask, render_template, request, jsonify
from sqldataInsert import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Python_html_file.html')


@app.route('/api/say_nam', methods=['POST'])
def say_name():
	json = request.get_json()
	first_name = json['first_name']
	last_name = json['last_name']
	age = json['age']
	
	
	result = sqldatafetch().mydata(first_name,last_name,age)
	return result
	


if __name__ == '__main__':
    app.run(debug=True)