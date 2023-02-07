import argparse

from exporter import Exporter
from importer import Importer


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--importer', type=str, default='cli', choices=Importer.CHOICES
    )
    parser.add_argument(
        '-f', '--file', type=str, default=""
    )
    parser.add_argument(
        '-n', '--name', type=str, default="output"
    )
    args = parser.parse_args()
    return args.importer, args.file, args.name


def main():
    importer_name, file, name = parse_arguments()
    importer = Importer(importer_name, file, name)
    topology = importer.import_topology()
    if topology is None:
        return
    exporter = Exporter(topology)
    exporter.export_topology()


if __name__ == "__main__":
    main()
