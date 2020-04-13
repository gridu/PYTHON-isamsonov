import unittest
import os
from generate_test_data.config import SystemConfig
from generate_test_data.system_type import KafkaInStreaming


class SystemTypeTest(unittest.TestCase):
    """
    Test SystemType class and his implementations
    """
    def setUp(self) -> None:
        self.conf_file_name = "test_conf.json"
        with open(self.conf_file_name, 'w') as f:
            json_string = r"""
                {
                  "count_producer": 2,
                  "producer1": {
                    "type": "click",
                    "timeout": 2,
                    "url": "https://blog.griddynamics.com/in-stream-deduplication-with-spark-amazon-kinesis-and-s3",
                    "ip": "127.0.0.1"
                  },
                  "producer2": {
                    "type": "click",
                    "timeout": 20,
                    "url": "https://blog.griddynamics.com/why-you-need-data-quality-automation-to-make-data-driven-decisions",
                    "ip": "192.168.0.1"
                  }
                }
            """
            f.write(json_string)
        self.conf = SystemConfig("test_conf.json").config()

    def tearDown(self):
        try:
            os.remove(self.conf_file_name)
        except OSError:
            pass

    def test_count_producers(self):
        producers = KafkaInStreaming().producers(self.conf)
        self.assertEqual(len(producers), 2)
