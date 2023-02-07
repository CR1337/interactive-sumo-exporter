from typing import List

from cli_importer.cli import CLI
from planpro_importer.reader import PlanProReader
from yaramo.model import Topology

from server import run_server


class Importer:

    CHOICES: List[str] = ['cli', 'planpro', 'orm']

    _importer: str
    _filename: str
    _name: str

    def __init__(self, importer: str, filename: str, name: str):
        self._importer = importer
        self._filename = filename
        self._name = name

    def import_topology(self) -> Topology:
        topology = None
        if self._importer == 'cli':
            topology = self.import_cli()
        elif self._importer == 'planpro':
            topology = self.import_planpro()
        elif self._importer == 'orm':
            return self.import_orm()
        topology.name = self._name
        return topology

    def import_cli(self) -> Topology:
        cli = CLI()
        cli.run()
        return cli.topology

    def import_planpro(self, filename: str) -> Topology:
        return PlanProReader(filename).read_topology_from_plan_pro_file()

    def import_orm(self) -> Topology:
        run_server(self._name)
        return None
