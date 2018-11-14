from classes import Network, Neuron
from testing import test, train
from random import *
import sys

#seed()
#To run, python main.py
#Suggested: python main.py > output.txt 

#Number of generated tests, Number of backpropogations
train(20, 10)

#Number of tests
test(30)
