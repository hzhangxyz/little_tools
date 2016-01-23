from tools import tools

@tools.route('/')
def index():
	file=open("static/index/index.html","r")
	data=file.read()
	file.close()
	return data
