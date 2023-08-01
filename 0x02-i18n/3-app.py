#!/usr/bin/env python3
"""Parametrize templates."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """i18n configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the best locale match for the user."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Application entry point for i18n."""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
