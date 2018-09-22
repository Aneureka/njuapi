from flask import Flask, current_app, logging


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    app.config.from_envvar('APP_CONFIG_FILE')
    app.config.from_pyfile('config.py')  # instance

    from .api.index import index as index_buleprint
    app.register_blueprint(index_buleprint, url_prefix='/')
    from .api.bbs import bbs as bbs_buleprint
    app.register_blueprint(bbs_buleprint, url_prefix='/bbs')

    return app
