from generate_test_data.producer import Producer


class SystemType:
    """Abstract class for types of systems"""
    def __init__(self):
        pass

    def process(self, conf):
        pass


class KafkaInStreaming(SystemType):
    """Class for generating test data for Java Engineer to In-Stream processing engineer capstone project from GridU"""

    def _producers(self, conf):
        """
        Get producers which are described in the configuration file
        :param conf: Congiguration
        :return: list of producers
        """
        producers = []
        for producer_number in range(1, conf["count_producer"] + 1):
            producer_name = "producer" + str(producer_number)
            producers.append(Producer(producer_name, conf[producer_name]))
        return producers

    def producers(self, conf):
        """
        Get producers from private variable
        :param conf: Configuration
        :return: list of producers
        """
        return self._producers(conf)

    def process(self, conf):
        """
        Here is started code of producers it threads
        :param conf: Configuration
        :return:
        """
        for producer in self._producers(conf):
            producer.start()
