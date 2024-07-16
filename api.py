from flask import Flask, jsonify
from processes_service import get_process_data

app = Flask(__name__)

@app.route('/api/processes')
def get_processes():
    processes = get_process_data()
    return jsonify({"success": True, "processes": processes}), 200

@app.route('/api/exception')
def test_exception():
    raise Exception("Test")

@app.errorhandler(404)
def page_not_found(exception: Exception):
    return jsonify({"success": False, "error": "Not Found"}), 404

@app.errorhandler(Exception)
def handle_exception(exception: Exception):
    # You can log the exception here using your preferred logging method
    print(f"'{type(exception).__name__}: {exception}'")
    return jsonify({"success": False, "error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
# Don't use debug=True, because it disables the Visual Studio Code debugger
# app.run(port=5000, debug=True) - disables the Visual Studio Code debugger