from flask import render_template, current_app

def page_not_found(e):
    current_app.logger.error(e)
    return render_template('errors/404.html', error='Oooops... something get wrong :('), 404