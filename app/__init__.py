from flask import Flask

# defined as an instance of class Flask
main_app = Flask(__name__)

# defined by the app directory
# routes is defined at the bottom to avoid circular imports
from app import routes

# routes - handles the different URLs that the appkication supports
