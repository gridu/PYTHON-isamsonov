import unittest
from generate_test_data.config import *


class ConfigTest(unittest.TestCase):
    """
    Test Config class
    """
    def setUp(self) -> None:
        self.conf_file_name = "test_conf.json"
        with open(self.conf_file_name, 'w') as f:
            json_string = r"""
            { "name": "value" }
            """
            f.write(json_string)

    def tearDown(self):
        try:
            os.remove(self.conf_file_name)
        except OSError:
            pass

    def test_check_exists_config_file(self):
        system_config = SystemConfig(self.conf_file_name)
        self.assertEqual(system_config._check_exist_config_file(), True)

    def test_read_config(self):
        system_config = SystemConfig(self.conf_file_name)
        conf = system_config._read_config()
        self.assertEqual(conf["name"], "value")



