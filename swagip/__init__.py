"""
Author: Swagger.pro
File: __init__.py
Purpose: initializes the application settings modules
"""

from flask import Flask

app = Flask(__name__)


from swagip import views
