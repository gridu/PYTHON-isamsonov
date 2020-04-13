import unittest
import os
from producer import Producer
from config import SystemConfig
from system_type import KafkaInStreaming


class ProducerTest(unittest.TestCase):
    """
    Test Producer class
    """
    def setUp(self) -> None:
        self.conf_file_name = "test_conf.json"
        with open(self.conf_file_name, 'w') as f:
            json_string = r"""
                {
                    "type": "click",
                    "timeout": 2,
                    "url": "https://blog.griddynamics.com/in-stream-deduplication-with-spark-amazon-kinesis-and-s3",
                    "ip": "127.0.0.1"
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
        producer = Producer("producer1", self.conf)
        producer_data_file = producer.producer_name() + ".data"
        producer.produce()
        self.assertEqual(os.path.exists(producer_data_file), True)
        try:
            os.remove(producer_data_file)
        except OSError:
            pass
