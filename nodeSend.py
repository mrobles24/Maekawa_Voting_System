import select
from threading import Thread
import utils
import config
import json
from copy import deepcopy  # <-- Importar deepcopy correctamente

# ANSI color codes for better output visibility
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

class NodeSend(Thread):
    def __init__(self, node):
        Thread.__init__(self)
        self.node = node
        self.client_sockets = [utils.create_client_socket() for i in range(config.numNodes)]
    
    def build_connection(self):
        for i in range(config.numNodes):
            self.client_sockets[i].connect(('localhost', config.port + i))
    
    def run(self):
        """ El hilo de cliente no necesita hacer nada en este caso """
        pass

    def send_message(self, msg, dest, multicast=False):
        if not multicast:
            self.node.lamport_ts += 1
            msg.set_ts(self.node.lamport_ts)
        assert dest == msg.dest
        print(f"{GREEN}Sending message to Node {dest}: {msg.to_json()}{RESET}")  # Fix: Colors are now defined
        self.client_sockets[dest].sendall(bytes(msg.to_json(), encoding='utf-8'))

    def multicast(self, msg, group):
        self.node.lamport_ts += 1
        msg.set_ts(self.node.lamport_ts)
        for dest in group:
            new_msg = deepcopy(msg)  # Usamos deepcopy correctamente
            new_msg.set_dest(dest)
            assert new_msg.dest == dest
            assert new_msg.ts == msg.ts
            self.send_message(new_msg, dest, True)
