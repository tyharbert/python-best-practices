from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(port=5000)
# Don't use debug=True, because it disables the Visual Studio Code debugger
# app.run(port=5000, debug=True) - disables the Visual Studio Code debugger