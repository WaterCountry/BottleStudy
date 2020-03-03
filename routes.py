"""
Routes and views for the bottle application.
"""
import os
import bottle
from bottle import route, view


@route('/')
@view('home')
def home():
    """Renders the home page."""
    return dict(
        title='Home',
        message='Your home page.'
    )

@route('/lesson')
@view('lesson')
def lesson():
    """Renders the contact page."""
    return dict(
        title='Lesson',
        message='Your lesson page.'
    )

@route('/share')
@view('share')
def share():
    """Renders the about page."""
    return dict(
        title='Share',
        message='Your share page.'
    )

@route('/party')
@view('party')
def party():
    """Renders the about page."""
    return dict(
        title='Party',
        message='Your party page.'
    )
