import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(rootPath)
from sounds import snowboydecoder
import signal
import threading


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector('sounds/resources/小老弟.pmdl', sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=snowboydecoder.play_audio_file,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

