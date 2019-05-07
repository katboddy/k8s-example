import os
from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def example():
    environ = os.environ.get("ENVIRON")
    githash = os.environ.get("GITHASH")
    return jsonify(
        environ=environ,
        githash=githash
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
