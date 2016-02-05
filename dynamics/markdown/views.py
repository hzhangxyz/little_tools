from tools import tools

@tools.route('/markdown')
def markdown():
        return tools.send_static_file("markdown/markdown.html")
