import time
import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n','--n',help = 'it',type = int, default = 1)
args = parser.parse_args()

def decorator (func):
    def wrapper():
        start = time.time()
        for i in range(args.number):
            func()
        end = time.time()
        print(f'Time: {end - start} sek' ) #jaki czas wykonywala sie funkcja
    return wrapper

#print('Hello')
def say_hi():
    return 'Heloo!'


def sat(): # zmiana jasn obrazka
    image = cv2.imread("image.bmp")
    alpha = 4
    new_image = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c], 0, 255)
    cv2.imwrite("change_imag.jpg", new_image)
    return new_image


say_hi = decorator(say_hi)
say_hi()

sat = decorator(sat)
sat()
