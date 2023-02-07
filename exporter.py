from sumoexporter.sumoexporter import SUMOExporter
from yaramo.model import Topology


class Exporter:

    _topology: Topology

    def __init__(self, topology: Topology):
        self._topology = topology

    def export_topology(self):
        exporter = SUMOExporter(self._topology)
        exporter.convert()
        exporter.write_output()
