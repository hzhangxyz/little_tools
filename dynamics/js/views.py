from tools import tools

@tools.route('/js')
def js():
	file=open("static/js/js.html","r")
	data=file.read()
	file.close()
	return data
