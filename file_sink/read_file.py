import matplotlib.pyplot as plt
import numpy as np


with open("output.bin", 'rb') as file:
    for byte in iter(lambda: file.read(1), b''):
        print(byte) # extracts one byte at a time to