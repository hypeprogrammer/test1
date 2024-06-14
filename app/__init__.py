from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    # Import and register blueprints here
    from app.controllers.iris_controller import iris_bp
    app.register_blueprint(iris_bp, url_prefix='/api/v1')

    return app
