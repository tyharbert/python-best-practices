from flask import jsonify
from api import app

@app.errorhandler(Exception)
def handle_exception(exception: Exception):
    # You can log the exception here using your preferred logging method
    print(f"'{type(exception).__name__}: {exception}'")
    return jsonify({"success": False, "error": "Internal Server Error"}), 500
