from tools import tools

@tools.route('/mathjs')
def mathjs():
        return tools.send_static_file("mathjs/mathjs.html")
