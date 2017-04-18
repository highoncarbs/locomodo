from flask import Flask , render_template, request, redirect, url_for
from search import get_all

app = Flask(__name__)

@app.route('/')
def source():
	return render_template('index.html')

@app.route('/index' , methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		print "Getting all values"
		search_term = str(request.form['search'])

		icon = str(request.form['iconInput'])
		photo_url , title = get_all(search_term , icon)
		print(icon)
		print(search_term)
		print("Generating Results....")
		print(title)
		return render_template('index.html' ,photo_url = photo_url , title = title)
	else:
		return redirect(url_for('source'))
	
if __name__ == "__main__":
	app.run(debug=True )