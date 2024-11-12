from threading import Event, Thread, Timer
from datetime import datetime
import time
from nodeServer import NodeServer
from nodeSend import NodeSend
from message import Message
import config

# ANSI color codes for better output visibility
RESET = "\033[0m"
BLUE = "\033[34m"

class Node():
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        self.port = config.port + id
        self.daemon = True
        self.lamport_ts = 0

        self.server = NodeServer(self)
        self.server.start()

        if id % 2 == 0:
            self.collegues = list(range(0, config.numNodes, 2))
        else:
            self.collegues = list(range(1, config.numNodes, 2))

        self.client = NodeSend(self)

    def do_connections(self):
        self.client.build_connection()

    def state(self):
        """Método que maneja el estado de cada nodo"""
        timer = Timer(1, self.state) # Cada 1s la función se llama de nuevo
        timer.start()
        self.curr_time = datetime.now()

        self.wakeupcounter += 1
        if self.wakeupcounter == 2:
            timer.cancel()
            print(f"{BLUE}Stopping Node {self.id}{RESET}")
            self.daemon = False
        else:
            print(f"{BLUE}This is Node {self.id} at TS: {self.lamport_ts} sending a message to my colleagues{RESET}")

            message = Message(
                msg_type="greetings",
                src=self.id,
                data=f"Hola, this is Node {self.id} - counter:{self.wakeupcounter}"
            )

            self.client.multicast(message, self.collegues)

    def run(self):
        print(f"{BLUE}Run Node {self.id} with colleagues {self.collegues}{RESET}")
        self.client.start()
        self.wakeupcounter = 0
        self.state()
