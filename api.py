from flask import Flask

app = Flask(__name__)

@app.route('/data/<int:test>')
def hello_world(test: int) -> str:
    return 'Hello, World!'

@app.route('/exception')
def test_exception():
    raise Exception("Test")

@app.errorhandler(Exception)
def handle_exception(exception: Exception):
    # You can log the exception here using your preferred logging method
    print(f"'{type(exception).__name__}: {exception}'")
    raise

app.run(port=5000)
# Don't use debug=True, because it disables the Visual Studio Code debugger
# app.run(port=5000, debug=True) - disables the Visual Studio Code debugger