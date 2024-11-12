from node import Node
import config
import time

class MaekawaMutex(object):
    """Class that implements and runs Maekawa mutual exclusion algorithm"""
    def __init__(self):
        self.nodes = [Node(i) for i in range(config.numNodes)]

    def define_connections(self):
        for node in self.nodes:
            node.do_connections()

    def run(self):
        self.define_connections()
        for node in self.nodes:
            node.run()
