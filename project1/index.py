from flask import Flask

from app import app


@app.route('/')
def hello_world():
    """主页"""
    return 'index'
