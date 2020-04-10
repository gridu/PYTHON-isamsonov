import threading
import time


class Producer(threading.Thread):
    """
    To generate data in one thread
    """
    def __init__(self, producer_name, conf):
        threading.Thread.__init__(self)
        self._producer_name = producer_name
        self._conf = conf

    def conf(self):
        return self.conf()

    def producer_name(self):
        return self._producer_name

    def produce(self):
        """
        To Generate and write data to test file
        :return:
        """
        with open(self._producer_name + ".data", "a") as f:
            ip = self._conf["ip"]
            event_time = str(time.time())
            url = self._conf["url"]
            line = "{\"type\": \"click\", \"ip\": \"" + ip \
                   + "\", \"event_time\": \"" + event_time \
                   + "\", \"url\": \"" + url + "\"}\n"
            f.writelines(line)
            print(line)

    def run(self):
        """
        To run process in one thread
        :return:
        """
        run_count = self.conf["count"]
        for i in range(0, run_count + 1):
            timeout = self._conf["timeout"]
            time.sleep(timeout)
            self.produce()
