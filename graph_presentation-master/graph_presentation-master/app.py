from flask import Flask, send_from_directory
from server.routing import graph_routing
import sys

app = Flask(__name__)
app.register_blueprint(graph_routing)


@app.route('/resources/<path:path>')
def send_resources(path):
    return send_from_directory('server/resources', path)


if __name__ == '__main__':
    env = 'develop' if len(sys.argv) == 1 else sys.argv[1]

    if env == 'production':
        app.run(debug=True, host='0.0.0.0', port=int("80"))
    else:
        app.run(debug=True)
