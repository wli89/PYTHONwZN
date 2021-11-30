# -*- coding: utf-8 -*-
"""
Lis Weronika
Projekt002
Isung
"""
import argparse
from rich.console import Console
#import pillow
import rich
import rich.traceback
from rich.progress import track
import time
from PIL import Image, ImageDraw
import random
import numpy as np
import itertools
import os.path


parser = argparse.ArgumentParser(description = "Opis")

parser.add_argument('-s', '--size', help = 'Rozmiar siatki', type = int)
parser.add_argument('-J', '--value', help = 'Całka wymiany', type = float,)
parser.add_argument('-B', '--beta', help = 'Parametr Beta', type = float)
parser.add_argument('-H', '--field', help = 'Parametr Beta', type = float)
parser.add_argument('-n', '--number', help = 'Liczba krokow/spinóW', type = int)
parser.add_argument('-d', '--density', help = 'Gestoć spinu', type = float, default = 0.5)
parser.add_argument('-file',  help = 'file name' , default ='step')

args = parser.parse_args()
'''
print(f'Grid size: {args.size}')
print(f'J value: {args.value}')
print(f'B value: {args.beta}')
print(f'Hamiltonian value: {args.field}')
print(f'Number of steps: {args.number}')
#print(f'Spin density: {args.density}')
print(f'FILE name: {args.file}')
'''
image_folder = 'images'
console = Console()
console.clear()
console.rule("Symulacja modelu Isinga 2D")

def do_some_work():
    time.sleep(1)

for i in track(range(10)):
    do_some_work()

'''
class Simulation:
    def __init__(self, s, J, B, H, n, d, file):
        
        self.size = s
        self.value = J
        self.beta = B
        self.field = H
        self.number = n
        self.density = d
        self.file = file
        ...
        
        print()   
'''

'''
def rysunek(self, file):
    
    image = Image.new('RGB', (800, 600), (255, 0, 255))
    image.putpixel((500, 500), (0, 0, 255))

    draw = ImageDraw.Draw(image)
    draw.rectangle((20, 20, 300, 300), (0, 255, 0))

rysunek.save('test_image.png')
 '''
        for i in range(self.n):
            for j in range(self.n):
                if self.arr[i, j] == 1:
                    self.image.paste(Image.open("./data/spin_up.png"), (20 * j + 1, 20 * i + 1))
                else:
                    self.image.paste(Image.open("./data/spin_down.png"), (20 * j + 1, 20 * i + 1))
        self.image.save(f"./output/{self.f}{self.curr_step:0>3}.png")

'''   
    sim1 = Simulation(
        s = args.size,
        J = args.value, 
        B = args.beta,
        H = args.field, 
        n = args.number,
        d = args.density,
        file = args.file
        )
    sim1.rysunek()
'''

