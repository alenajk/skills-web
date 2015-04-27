from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"
    return render_template("application-form.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application", methods=['POST'])
def submit_app():
	first_name=request.form['firstname']
	last_name=request.form['lastname']
	salary=request.form['salary']
	job=request.form['job']

	return "%s %s, you submitted your application for the %s role! Your minimum salary requirement is %s." % (first_name, last_name, job, salary)

if __name__ == "__main__":
    app.run(debug=True)