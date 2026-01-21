import time
import os

class AnimationPlayer:
    def __init__(self, frames, delay=0.3):
        self.frames = frames
        self.delay = delay
        self.index = 0

    def play(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)
        time.sleep(self.delay)