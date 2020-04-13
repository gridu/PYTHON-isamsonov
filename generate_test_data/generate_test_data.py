import argparse
from generate_test_data.system_type import *
from generate_test_data.config import SystemConfig


class TestSystem:

    def __init__(self):
        pass

    def arguments(self, parser):
        """
        Function for parsing program's arguments
        :param parser:
        :return: parsed arguemnts
        """
        parser.add_argument("--system", help="Type of system", required=True, choices=["kafka-in-action"])
        parser.add_argument("--conf", help="Type of system", default="conf.json")
        return parser.parse_args()

    def run(self):
        """
        Function to start processing of generating test data
        :return:
        """
        args = self.arguments(argparse.ArgumentParser())

        system_type = None
        if args.system == "kafka-in-action":
            system_type = KafkaInStreaming()
        self.process(system_type, SystemConfig(args.conf).config())

    def process(self, system_type, conf):
        system_type.process(conf)

