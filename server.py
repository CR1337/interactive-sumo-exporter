import webbrowser

from flask import Flask, render_template, request, url_for
from orm_importer.importer import ORMImporter

from exporter import Exporter

server = Flask(__name__)


@server.route("/", methods=['GET'])
def route_index():
    return render_template(
        'index.html',
        css_file=url_for('static', filename='pico.min.css')
    )


@server.route("/polygon", methods=['POST'])
def route_post_polygon():
    print("Processing polygon...")
    polygon = request.get_json()['polygon']
    if not polygon:
        return "No location specified", 400
    topology = ORMImporter().run(polygon)
    topology.name = server.config['TOPOLOGY_NAME']
    exporter = Exporter(topology)
    exporter.export_topology()
    return "", 200


def run_server(name: str):
    port = 8080
    server.config['TOPOLOGY_NAME'] = name
    webbrowser.open(f"http://localhost:{port}")
    server.run(port=port)
