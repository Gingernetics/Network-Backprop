#Testing file

from classes import Network, Neuron
from random import *

generatedinputs = []
expectedoutputs = []

net = Network([1, 2, 1])

#Higher numbers make it learn faster to a point
learn_rate = 8

def train(num_tests, num_backprop):

    populate_tests(num_tests)
    print("Original network values\n")
    check_network()

    for i in range(num_backprop):
	print("\nRun " + str(i) + "\n")	
        backprop()
        check_network()


def test(num_tests):
    
    populate_tests(num_tests)
    check_network()



#Creates a new set of training data
def populate_tests(num_tests):
    global generatedinputs
    global expectedoutputs

    generatedinputs = []
    expectedoutputs = []

    for i in range(num_tests):

	#If you allow a large range, you require more training sets to get accuracy
        rand_input = randint(-10, 20)

	#Change training condition here
	#Works really well for values around center of range, less well for boundary numbers
	#Works really, really well if centered on 0
        if (rand_input >= 5):
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
    raw_outputs = []
    errors = []

    for i in range(len(generatedinputs)):
        output = net.getOutput(generatedinputs[i])

        producedoutputs.append(output)
        #round floats
        for j in range(len(output)):
	    raw_outputs.append(round(output[j], 3))
            output[j] = int(round(output[j]))
        #check output
        if (output != expectedoutputs[i]):
            pair = (generatedinputs[i], expectedoutputs[i], output)
            errors.append(pair)

    #Print the weights and biases of the network
    print net
    print "Generated Inputs"
    print generatedinputs
    print "Expected Outputs"
    print expectedoutputs
    print "Produced Outputs"
    print producedoutputs
    
    print "\n"
    print "Raw Outputs"
    print raw_outputs
    print "Stuff Correct: " + str(1 - len(errors)*1.0/len(generatedinputs))
    #print errors
    print "\n<--------------------------------------------------------------->\n"



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
	    #print("Expected: " + str(output[j]) + " Produced: " + str(neuron.result) + "\n")
            previous_errors.append((neuron.result - output[j])
                                   * neuron.calculateSigmoidPrime())

        #backprop
        layer = net.outputNeurons[0].incoming

	last_layer = 0

        while ( not last_layer):
	    if layer == net.inputNeurons:
		last_layer = 1

            current_errors = []

            #do current errors
            for j in range(len(layer)):
                error = 0

		for k in range(len(previous_errors)):
                    error += previous_layer[k].weights[j] * previous_errors[k]
                error *= layer[j].calculateSigmoidPrime()

                current_errors.append(error)

            #update previous layer
            for neuron, error in zip(previous_layer, previous_errors):
		#print str(neuron) + ", error: " + str(error) + "\n"
                neuron.bias -= learn_rate * error
                for k in range(len(neuron.weights)):
                    neuron.weights[k] -= learn_rate * error * layer[k].result
		#print str(neuron) + ", error: " + str(error) + "\n"


            previous_layer = layer
            layer = layer[0].incoming
            previous_errors = current_errors


	#for input neurons
        for neuron, error in zip(previous_layer, previous_errors):
            neuron.bias -= learn_rate * error
