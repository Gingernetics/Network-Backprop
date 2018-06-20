from random import *
from math import exp, trunc

class Neuron:
    def __init__(self):
        self.incoming = []
        self.weights = []
        self.bias = random() * 2
        self.result = 0
        self.z = 0


    def addNeuron(self, neuron, weight):
        self.incoming.append(neuron)
        self.weights.append(weight)

    #Incoming neuron's results should be computed before calling this
    def computeResult(self):
        self.z = self.bias
        i = 0
        for neuron in self.incoming:
            self.z += self.weights[i] * neuron.result
            i += 1

        self.result = self.calculateSigmoid(self.z)
        return self.result


    def calculateSigmoid(self, input):
        answer = 1/ (1 + exp(-1 * input))
        return answer

    def calculateSigmoidPrime(self):
        exponent = exp(-1 * self.z)
        sum = 1 + exponent
        return exponent / ((sum) ** 2)

    def __repr__(self):
	trunc_weights = []
	#Add a truncated version of weight for presentation
	for weight in self.weights:
	    trunc_weights.append(trunc(weight*100)/100.0)
	#print "Weights: " + str(trunc_weights) + "\n"
        return "B:%.2f, W:%s" % (self.bias, trunc_weights)

class Network:
    #neurons is an array of ints, representing the number of neurons in each layer
    def __init__(self, neurons):
        self.inputNeurons = []
        self.outputNeurons = []

	#Storing the initial data for repr function
	self.neurons = neurons

        for i in range(neurons[0]):
            self.inputNeurons.append(Neuron())

        #create layers, connect each new neuron to previous
        previous = self.inputNeurons
        for i in range(1,len(neurons)):
            current = []
            #create layer and connect
            for j in range(neurons[i]):
                neuron = Neuron()
                current.append(neuron)
                for prev in previous:
                    neuron.addNeuron(prev, random() * 2 - 1)
            previous = current
        self.outputNeurons = previous

    def getOutput(self, inputs):
        #set input neurons
        for i in range(len(inputs)):
            self.inputNeurons[i].result = inputs[i]

        self.computeLayer(self.outputNeurons)

        output = []
        for neuron in self.outputNeurons:
            output.append(neuron.result)
        return output

    def computeLayer(self, layer):
        if (layer == self.inputNeurons):
            return

        #print layer[0].incoming
        #make sure the incoming of each neuron is computed
        self.computeLayer(layer[0].incoming)

        for neuron in layer:
            neuron.computeResult()



##################################################################
#Printing out network


    def tree(self):
	tree = ""
	max_number = 0
	for number in self.neurons:
	    if (number > max_number):
		max_number = number

	line_num = max_number - 1
	while (line_num != 0):
	    tree = self.buildLine(line_num) + tree
	    line_num -= 1	
        tree = self.buildLine(line_num) + tree
	return tree	

    #line_num is 0 indexed
    def buildLine(self, line_num):
	position = 0
	line = ""
	filler = "\t\t"
	for num_neurons in self.neurons:
	    if(num_neurons > line_num):
		line += " " + str(self.getNeuronValue(position, line_num)) + "\t"
	    else:
		line += filler
	    position += 1
	line += "\n"
	return line


    #Imagine input neurons as 0th layer, output neurons as nth layer
    def getNeuronValue(self, layer_number, neuron_number):
	num_layers = len(self.neurons)
	neuron = self.outputNeurons[0]

	#Steps from output layer to desired layer
	steps = num_layers - layer_number - 2

	#Neuron will be set to the first neuron in each layer until 
	#the neuron before desired neuron
	while (steps > 0):
		neuron = neuron.incoming[0]
		steps -= 1

	print neuron
	if (num_layers != layer_number + 1):
		neuron = neuron.incoming[neuron_number] 
	print neuron
	print "\n"
	return neuron



#####################################################################
#Representation function

    def __repr__(self):
        res = "\n<--------------------------------->\n"
	'''
	output = ""
	layer = self.outputNeurons
        while (layer):
            output += str(layer) + "\n"
            layer = layer[0].incoming
       '''
	return res + self.tree() + res

#####################################################################
