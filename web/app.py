import os
from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def root():
    runtime = os.getenv('RUN_ARG') or None
    buildtime = os.getenv('BUILD_ARG') or None
    return """
    <p>Welcome to a simple app that demonstrates build & run args with Docker & Compose.</p>
    <p>This is the provided runtime argument: {}</p>
    <p>This is the provided build-time argument: {}</p>
    """.format(runtime, buildtime)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')