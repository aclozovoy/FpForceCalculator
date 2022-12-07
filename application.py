from flask import Flask
from views import views

application = Flask(__name__)
# application.config['SECRET_KEY'] = "randomstring"
application.register_blueprint(views, url_prefix="/")
# application.run(debug=True)

if __name__ == "__main__":
    application.run(debug=True)