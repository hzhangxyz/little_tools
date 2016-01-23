from tools import tools
from flask import render_template

@tools.route('/js')
def js():
	return render_template("js/js.html")
