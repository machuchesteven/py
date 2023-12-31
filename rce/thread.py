import threading

def make_thread(command):
    attak_thread = threading.Thread(target=command)
    attak_thread.start()

