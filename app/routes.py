# first app = library
# second app = variable
from app import main_app


@main_app.route("/")
@main_app.route("/index")
def index():  # view function
    return "Hello World"
