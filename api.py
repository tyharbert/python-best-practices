from flask import Flask
app = Flask(__name__)

@app.route('/<int:test>')
def hello_world(test: int) -> str:
    return 'Hello, World!'

app.run(port=5000)
# Don't use debug=True, because it disables the Visual Studio Code debugger
# app.run(port=5000, debug=True) - disables the Visual Studio Code debugger