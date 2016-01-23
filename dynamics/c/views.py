from flask import request, render_template
from tools import tools
import sys, os

@tools.route("/c")
def c():
        if "run" in request.args.keys():
                src=request.args["run"]
		name="n%s"%str(hash(src))
		inp=open('/tmp/tOoLs/%s.c'%name,'w')
                inp.write(src)
                inp.close()
                os.system("rm /tmp/tOoLs/%s.out"%name)
                os.system("touch /tmp/tOoLs/%s.out"%name)
                try:
                        os.system("gcc /tmp/tOoLs/%s.c -o /tmp/tOoLs/%s 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name,name))
                        os.system("/tmp/tOoLs/%s 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name))
                except:
                        pass
                file=open("/tmp/tOoLs/%s.out"%name,"r")
                ans=file.read()
                file.close()
                return ans
        else:
                file=open("static/c/c.html","r")
                data=file.read()
                file.close()
                return data

