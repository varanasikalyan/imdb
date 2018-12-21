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
import urllib

conn_str = (
    "DRIVER={SQL Server Native Client 11.0};"
    "SERVER=(local)\\SQLEXPRESS;"
    "DATABASE=imdb;"
    "UID=kkrishnav;"
    "PWD='2018@Factset';"
    "Trusted_Connection=yes;"
)
quoted_conn_str = urllib.quote_plus(conn_str)

application = Flask(__name__)
engine = create_engine('mssql+pyodbc:///?odbc_connect={0}'.format(quoted_conn_str), echo=False)

from controllers import *