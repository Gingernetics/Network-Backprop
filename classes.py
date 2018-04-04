from random import *
from math import exp

class Neuron:
    def __init__(self):
        self.incoming = []
        self.weights = []
        self.bias = random() * 2 - 1
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
        return "Neuron: bias:%f, weights: %s" % (self.bias, self.weights)

class Network:
    #neurons is an array of ints, representing the number of neurons in each layer
    def __init__(self, neurons):
        self.inputNeurons = []
        self.outputNeurons = []

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

    def __repr__(self):
        res = "[\n"
        layer = self.outputNeurons
        while (layer):
            res += str(layer) + "\n"
            layer = layer[0].incoming
        return res + "]"
