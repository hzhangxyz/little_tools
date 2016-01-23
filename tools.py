from flask import Flask
tools = Flask(__name__)
from dynamics.index import *
from dynamics.js import *
from dynamics.python import *
from dynamics.c import *
