#Testing file

from classes import Network, Neuron
from random import *


def test(num_tests):
    generatedinputs = []
    expectedoutputs = []
    producedoutputs = []

    errors = []


    populate_tests(num_tests, generatedinputs, expectedoutputs)

    test = Network()

    for i in range(num_tests):
        output = test.getOutput(generatedinputs[i])
        producedoutputs.append(output)
        if (output != expectedoutputs[i]):
            pair = (generatedinputs[i], expectedoutputs[i], output)
            errors.append(pair)
    print "Stuff Correct: " + str(1 - len(errors)*1.0/num_tests)
    return errors

def populate_tests(num_tests, generatedinputs, expectedoutputs):
    for i in range(num_tests):
        rand_input = randint(-20, 20)
        generatedinputs.append(rand_input)

        if (rand_input >= 0):
            expected = 1
        else:
            expected = 0
        expectedoutputs.append(expected)
