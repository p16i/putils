import time

class Timer:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.stop = time.time()
        self.time_took = self.stop - self.start

        print(f"Finished block: {self.name} with {self.time_took} seconds")