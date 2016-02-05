from tools import tools

@tools.route('/js')
def js():
        return tools.send_static_file("js/js.html")
