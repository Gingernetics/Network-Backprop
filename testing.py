#Testing file

from classes import Network, Neuron
from random import *


def test(num_tests):
    generatedinputs = []
    expectedoutputs = []
    producedoutputs = []

    errors = []

    populate_tests(num_tests, generatedinputs, expectedoutputs)

    test = Network([1, 3, 1])

    for i in range(num_tests):
        output = test.getOutput(generatedinputs[i])
        producedoutputs.append(output)
        #round floats
        for i in range(len(output)):
            output[i] = int(round(output[i]))
        #check output
        if (output == expectedoutputs[i]):
            pair = (generatedinputs[i], expectedoutputs[i], output)
            errors.append(pair)

    print "Generated Inputs"
    print generatedinputs
    print "Expected Outputs"
    print expectedoutputs
    print "Produced Outputs"
    print producedoutputs
    print "Stuff Correct: " + str(1 - len(errors)*1.0/num_tests)
    return errors

def populate_tests(num_tests, generatedinputs, expectedoutputs):
    for i in range(num_tests):
        rand_input = randint(-20, 20)
        if (rand_input >= 0):
            expected = 1
        else:
            expected = 0

        generatedinputs.append([rand_input])

        expectedoutputs.append([expected])
