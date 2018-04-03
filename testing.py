#Testing file

from classes import Network, Neuron
from random import *

generatedinputs = []
expectedoutputs = []

net = Network([1, 3, 1])

def test(num_tests):
    populate_tests(num_tests)
    return check_network(num_tests)

def populate_tests(num_tests):
    global generatedinputs
    global expectedoutputs

    for i in range(num_tests):
        rand_input = randint(-20, 20)
        if (rand_input >= 0):
            expected = 1
        else:
            expected = 0

        generatedinputs.append([rand_input])

        expectedoutputs.append([expected])

def check_network(num_tests):
    global generatedinputs
    global expectedoutputs
    global net

    producedoutputs = []
    errors = []

    for i in range(num_tests):
        output = net.getOutput(generatedinputs[i])
        producedoutputs.append(output)
        #round floats
        for j in range(len(output)):
            output[j] = int(round(output[j]))
        #check output
        if (output != expectedoutputs[i]):
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

def backprop():
    pass
