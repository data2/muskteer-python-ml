import threading


class myThread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print("exec " + self.name)


thread = myThread(1, "testThread")
thread2 = myThread(2, "testThread")
thread.start()
thread2.start()
