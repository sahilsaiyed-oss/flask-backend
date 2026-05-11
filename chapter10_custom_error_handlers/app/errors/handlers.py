from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):

        return jsonify({
            "error": "Custom Not Found Error",
            "message": "Requested resource does not exist"
        }), 404