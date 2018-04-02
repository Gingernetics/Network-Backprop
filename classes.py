from random import *


class neuron:
    incoming = []
    weights = []
    bias = 0
    result = 0


    def setRandomBias():
        self.bias = randint(0,10)

    def addNeuron(self, neuron, weight):
        self.incoming.append(neuron)
        self.weights.append(weight)

    #Incoming neuron's results should be computed before calling this
    def computeResult(self):
        self.result = 0
        i = 0
        for neuron in self.incoming:
            self.result += self.weights[i] * neuron.result
            i += 1
        self.result += self.bias
        if (self.result >= 0):
            self.result = 1
        else:
            self.result = 0



class Network:
    inputNeuron = neuron()
    outputNeuron = neuron()

    def __init__(self, input):
        self.inputNeuron.result = input
        self.outputNeuron.addNeuron(self.inputNeuron, 9)

    def getOutput(self):
        self.outputNeuron.computeResult()
        return self.outputNeuron.result
