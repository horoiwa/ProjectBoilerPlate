import time


class Timer:

    def __init__(self, tag: str):
        self.tag = tag

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        fin = time.time() - self.start
        print(f"{self.tag}: {fin:.3f}sec")
