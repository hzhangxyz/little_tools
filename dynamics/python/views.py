from flask import request, render_template
from tools import tools
import sys, StringIO

@tools.route("/python")
def python():
        if "run" in request.args.keys():
                src=request.args["run"]
                tmp=sys.stdout
                sys.stdout=StringIO.StringIO()
                try:
                        exec(src)
                except Exception,e:
                        return e.__repr__()
                ans=sys.stdout.getvalue()
                sys.stdout.close()
                sys.stdout=tmp
                return ans
        else:
                file=open("static/python/python.html","r")
                data=file.read()
                file.close()
                return data

