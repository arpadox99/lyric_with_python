from time import sleep
import time
import sys

def print_lirik():
    line = [
        ("What if you had it all", 0.08),
        ("But nobody to call?", 0.07),
        ("Maybe then you'd know me", 0.06),
        ("'Cause I've had everything", 0.08),
        ("But no one's listening", 0.07),
        ("And that's just FUCKING lonely", 0.06),
        ("I'm so lonely", 0.09),
        ("Lonely", 0.25)
    ]

    delays = [1.5, 1.7, 3.6, 1.8, 1.6, 2, 4, 2]
    
    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lirik()
