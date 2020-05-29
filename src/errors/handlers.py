from flask import render_template
from src.errors import errors


@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404