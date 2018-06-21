#Testing file

from classes import Network, Neuron
from random import *

generatedinputs = []
expectedoutputs = []

net = Network([1, 2, 1])

learn_rate = 5

def test(num_tests, num_backprop):
    for i in range(num_backprop):
        populate_tests(num_tests)
        check_network()
	
        #backprop()
        #check_network()



#Creates a new set of training data
def populate_tests(num_tests):
    global generatedinputs
    global expectedoutputs

    generatedinputs = []
    expectedoutputs = []

    for i in range(num_tests):
        rand_input = randint(-20, 20)
        if (rand_input >= 0):
            expected = 1
        else:
            expected = 0

        generatedinputs.append([rand_input])
        expectedoutputs.append([expected])


def check_network():
    global generatedinputs
    global expectedoutputs
    global net

    producedoutputs = []
    errors = []

    for i in range(len(generatedinputs)):
        output = net.getOutput(generatedinputs[i])

        producedoutputs.append(output)
        #round floats
        for j in range(len(output)):
            output[j] = int(round(output[j]))
        #check output
        if (output != expectedoutputs[i]):
            pair = (generatedinputs[i], expectedoutputs[i], output)
            errors.append(pair)

    #Print the weights and biases of the network
    print net
'''
    print "Generated Inputs"
    print generatedinputs
    print "Expected Outputs"
    print expectedoutputs
    print "Produced Outputs"
    print producedoutputs
'''
    #print "Stuff Correct: " + str(1 - len(errors)*1.0/len(generatedinputs))
    #return errors

def backprop():
    global generatedinputs
    global expectedoutputs
    global net
    global learn_rate

    for i in range(len(generatedinputs)):
        input = generatedinputs[i]
        output = expectedoutputs[i]

        #Storing one layer at a time
        previous_errors = []

        #feedforward
        net.getOutput(input)

        #last layer
        previous_layer = net.outputNeurons
        for j in range(len(previous_layer)):
            neuron = previous_layer[j]
            previous_errors.append((neuron.result - output[j]
                                   * neuron.calculateSigmoidPrime()))

        #backprop
        layer = net.outputNeurons[0].incoming
        while (layer != net.inputNeurons):
            current_errors = []

            #do current errors
            for j in range(len(layer)):
                error = 0
                for k in range(len(previous_errors)):
                    error += previous_layer[k].weights[j] * \
                             previous_errors[k]
                error *= layer[j].calculateSigmoidPrime()
                current_errors.append(error)

            #update previous layer
            for neuron, error in zip(previous_layer, previous_errors):
                neuron.bias -= learn_rate * error
                for k in range(len(neuron.weights)):
                    neuron.weights[k] -= learn_rate * error * layer[k].result

            previous_layer = layer
            layer = layer[0].incoming
            previous_errors = current_errors
#            print "Hi\n"
#	    print current_deltas
