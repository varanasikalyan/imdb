#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      kkrishnav
#
# Created:     15/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask
from sqlalchemy import create_engine
import config

application = Flask(__name__)
engine = create_engine(config.CONNECTION_STRING, echo=False)

from controllers import *