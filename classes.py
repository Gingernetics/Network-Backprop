from random import *


class Neuron:
    incoming = []
    weights = []
    bias = 0
    result = 0

    def addNeuron(self, neuron, weight):
        self.incoming.append(neuron)
        self.weights.append(weight)

    #Incoming neuron's results should be computed before calling this
    def computeResult(self):
        self.result = self.bias
        i = 0
        for neuron in self.incoming:
            self.result += self.weights[i] * neuron.result
            i += 1

        if (self.result >= 0):
            self.result = 1
        else:
            self.result = 0
        return self.result


class Network:
    inputNeurons = []
    outputNeurons = []

    #neurons is an array of ints, representing the number of neurons in each layer
    def __init__(self, neurons):
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
                    neuron.addNeuron(prev, randint(-20, 20))
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
        #make sure the incoming of each neuron is computed
        self.computeLayer(layer[0].incoming)

        for neuron in layer:
            neuron.computeResult()
