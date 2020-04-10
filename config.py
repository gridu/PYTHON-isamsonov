import os
import json


class SystemConfig:

    def __init__(self, config_file):
        self._config_file = config_file
        self._config = self._read_config()

    def _check_exist_config_file(self):
        return os.path.exists(self._config_file)

    def _read_config(self):
        if self._check_exist_config_file():
            with open(self._config_file, 'r') as f:
                return json.load(f)
        else:
            raise Exception("Config file {} is not exists in current directory".format(self._config_file))

    def config(self):
        return self._config
