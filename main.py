import time
from maekawaMutex import MaekawaMutex
from threading import Thread
import config

# ANSI color codes for better output visibility
RESET = "\033[0m"
BLUE = "\033[34m"

def run_algorithm():
    maekawa_mutex = MaekawaMutex()
    print(f"{BLUE}Running Maekawa Mutex Algorithm...{RESET}")
    maekawa_mutex.run()

mutex_thread = Thread(target=run_algorithm)
mutex_thread.start()

time.sleep(config.exec_time)
print(f"{BLUE}Execution finished after {config.exec_time} seconds.{RESET}")
