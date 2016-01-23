from tools import tools
from flask import render_template

@tools.route('/')
def index():
	return render_template("index/index.html")
