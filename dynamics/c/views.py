from flask import request, render_template
from tools import tools
import sys, os

@tools.route("/c")
def c():
        if "run" in request.args.keys():
                src=request.args["run"]
		name=str(ash(src))
		inp=open('/tmp/tOoLs/%s.c'%name,'w')
                inp.write(src)
                inp.close()
                os.system("gcc /tmp/tOoLs/%s.c -o /tmp/tOoLs/%s 1>/tmp/tOoLs/%s.out 2>/tmp/tOoLs/%s.out"%(name,name,name,name))
                os.system("echo \"running...\" >/tmp/tOoLs/%s.out"%name)
                os.system("/tmp/tOoLs/%s 1>/tmp/tOoLs/%s.out 2>/tmp/tOoLs/%s.out"%(name,name,name))
                file=open("/tmp/tOoLs/%s.out"%name,"r")
                ans=file.read()
                file.close()
                return ans
        else:
                file=open("static/c/c.html","r")
                data=file.read()
                file.close()
                return data

