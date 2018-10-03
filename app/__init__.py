from flask import Flask, current_app, logging


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    app.config.from_envvar('APP_CONFIG_FILE')
    app.config.from_pyfile('config.py')  # instance

    from .api.index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')
    from .api.bbs import bbs as bbs_blueprint
    app.register_blueprint(bbs_blueprint, url_prefix='/bbs')
    from .api.core import core as core_blueprint
    app.register_blueprint(core_blueprint, url_prefix='/core')

    return app
