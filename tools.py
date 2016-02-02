from flask import Flask
import os
os.system('mkdir /tmp/tOoLs')
tools = Flask(__name__)
from dynamics.index import *
from dynamics.js import *
from dynamics.python import *
from dynamics.c import *
from dynamics.mathjs import *
from dynamics.markdown import *
