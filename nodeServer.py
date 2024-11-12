# nodeServer.py
import select
from threading import Thread
import utils
from message import Message
import json

# ANSI color codes for better output visibility
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

class NodeServer(Thread):
    def __init__(self, node):
        Thread.__init__(self)
        self.node = node
    
    def run(self):
        self.update()

    def update(self):
        self.connection_list = []
        self.server_socket = utils.create_server_socket(self.node.port)
        self.connection_list.append(self.server_socket)

        print(f"{BLUE}Node {self.node.id} server started on port {self.node.port}{RESET}")

        while self.node.daemon:
            (read_sockets, write_sockets, error_sockets) = select.select(
                self.connection_list, [], [], 5)
            
            if not (read_sockets or write_sockets or error_sockets):
                print(f"{YELLOW}NS{self.node.id} - Timed out{RESET}")
            else:
                for read_socket in read_sockets:
                    if read_socket == self.server_socket:
                        (conn, addr) = read_socket.accept()
                        self.connection_list.append(conn)
                        print(f"{GREEN}Node {self.node.id} accepted connection from {addr}{RESET}")
                    else:
                        try:
                            # Recibir datos del socket
                            msg_stream = read_socket.recv(4096)
                            if msg_stream:  # Verificar que msg_stream no esté vacío
                                msg = msg_stream.decode('utf-8')
                                ms = json.loads(msg)
                                self.process_message(ms)
                            else:
                                # Si el socket no envía datos, se cierra y elimina
                                print(f"{RED}Connection closed by peer at {read_socket.getpeername()}{RESET}")
                                read_socket.close()
                                self.connection_list.remove(read_socket)
                        except Exception as e:
                            print(f"{RED}Error reading from socket: {e}{RESET}")
                            read_socket.close()
                            self.connection_list.remove(read_socket)
                            continue
        self.server_socket.close()

    def process_message(self, msg):
        """ Procesa los mensajes recibidos """
        try:
            print(f"{BLUE}Node_{self.node.id} received msg: {msg}{RESET}")
        except Exception as e:
            print(f"{RED}Error processing message: {e}{RESET}")
