from time import sleep
import sys

def print_lirik():
    # Lines with respective character delay per line
    lines = [
        ("Losing my head", 0.09),
        ("Over you", 0.09),
        ("And I'll be here", 0.1),
        ("'Cause we both know how it goes", 0.06),  # Faster pace
        ("I don't want things to change", 0.06),
        ("I pray they stay the same always", 0.08),  # Slightly faster
        ("And I don't care", 0.08),
        ("If you're with somebody else", 0.07),  # Faster delivery
        ("I'll give you time and space", 0.07),
        ("Just know I'm not a phase", 0.08),
        ("I'm always, ways, ways", 0.1),  # Slower for emphasis
        ("Always, ways, ways", 0.1),
        ("I'm always, ways, ways", 0.1)
    ]

    # Delay between each line (in seconds)
    delays = [1.1, 4.3, 0.7, 0.8, 1, 3.8, 0.8, 1, 1.1, 1.1, 1.3, 1.1, 1.2]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])  # Pause after printing the whole line
        print('')

print_lirik()
