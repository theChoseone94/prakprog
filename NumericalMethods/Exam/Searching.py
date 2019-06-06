import numpy as np
import matplotlib.pyplot as plt
from math import *
import random


def BinarySearch(n,x,z):
    first=0
    last = n-1
    mid=floor((first+last)/2.)

    while(first<=last):
        if x[mid]==z:
            break
        elif x[mid]<z:
            first=mid+1
        elif x[mid]>z:
            last=mid-1
        mid=floor((first+last)/2.)
    return mid


