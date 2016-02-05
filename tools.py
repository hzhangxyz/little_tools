from flask import Flask, request
import os, sys

os.system('mkdir /tmp/tOoLs')
tools = Flask(__name__)

@tools.route('/')
def index():
        return tools.send_static_file("index.html")

@tools.route('/js')
def js():
        return tools.send_static_file("js.html")

@tools.route("/python")
def python():
        if "run" in request.args.keys():
                src=request.args["run"]
                try:
                        src=src.encode('utf8')
                except:
                        pass
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
                return tools.send_static_file("python.html")

@tools.route("/c")
def c():
        if "run" in request.args.keys():
                src=request.args["run"]
                try:
                        src=src.encode('utf8')
                except:
                        pass
                name="n%s"%str(hash(src))
                inp=open('/tmp/tOoLs/%s.c'%name,'w')
                inp.write(src)
                inp.close()
                os.system("rm /tmp/tOoLs/%s.out"%name)
                os.system("touch /tmp/tOoLs/%s.out"%name)
                try:
                        os.system("gcc /tmp/tOoLs/%s.c -o /tmp/tOoLs/%s </dev/null 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name,name))
                        os.system("/tmp/tOoLs/%s </dev/null 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name))
                except Exception,e:
                        return e.__repr__()
                file=open("/tmp/tOoLs/%s.out"%name,"r")
                ans=file.read()
                file.close()
                return ans
        else:
                return tools.send_static_file("c.html")

@tools.route('/mathjs')
def mathjs():
        return tools.send_static_file("mathjs.html")

@tools.route('/markdown')
def markdown():
        return tools.send_static_file("markdown.html")
