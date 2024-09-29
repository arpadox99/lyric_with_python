from time import sleep
import time
import sys

def print_lirik():
    lines = [
        # Lirik baru
        ("Tuhanmu tak akan memberi", 0.23),
        ("Ular beracun pada yang minta roti", 0.20),
        ("Cobaan yang engkau alami", 0.2),
        ("Tak melebihi kekuatanmu", 0.15),
        ("-----------------", 0),
        ("Tangan Tuhan sedang merenda", 0.2),
        ("Suatu karya yang agung mulia", 0.25),
        ("Saatnya kan tiba nanti", 0.2),
        ("Kau lihat pelangi kasihNya", 0.2),
        ("", 0)
    ]
    
    delays = [1, 1.9, 2, 2.5, 3, 2.4, 1.8, 2., 1, 1]  # Durasi jeda antar baris
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lirik()