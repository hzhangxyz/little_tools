from flask import request
from tools import tools
import sys, os

@tools.route("/python")
def python():
        if "run" in request.args.keys():
                src=request.args["run"]
                name="n%s"%str(hash(src))
                inp=open('/tmp/tOoLs/%s.py'%name,'w')
                inp.write(src)
                inp.close()
                os.system("rm /tmp/tOoLs/%s.out"%name)
                os.system("touch /tmp/tOoLs/%s.out"%name)
                try:
                        os.system("python /tmp/tOoLs/%s.py </dev/null 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name))
                except Exception,e:
                        return e.__repr__()
                file=open("/tmp/tOoLs/%s.out"%name,"r")
                ans=file.read()
                file.close()
                return ans
        else:
                return tools.send_static_file("python/python.html")

