from tools import tools

@tools.route('/')
def index():
	return tools.send_static_file("index/index.html")
