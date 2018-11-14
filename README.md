# Network-Backprop
An introdution to artificial neural networks

By default, this network is designed to determine if an input is greater than or equal to 0. 

In essence, it simulates a comparison operator.

---

If you are interested in running this, clone the repository and run `$ python main.py`
Alternatively, you can pipe the output into a file with `$ python main.py > test.txt`


The ouput will be look similar to this:

`
<--------------------------------------------------------------->


Run 9

 B:1.74, W:[]    B:1.96, W:[1.81]        B:-3.15, W:[3.92, 3.1]
                 B:1.81, W:[1.63]                       

Generated Inputs
[[-20], [6], [10], [-7], [-7], [1], [16], [13], [19], [-12], [-14], [12], [-17], [17], [5], [19], [-3], [0], [-8], [4]]
Expected Outputs
[[0], [1], [1], [0], [0], [1], [1], [1], [1], [0], [0], [1], [0], [1], [1], [1], [0], [1], [0], [1]]
Produced Outputs
[[0], [1], [1], [0], [0], [1], [1], [1], [1], [0], [0], [1], [0], [1], [1], [1], [0], [1], [0], [1]]


Raw Outputs
[0.041, 0.98, 0.98, 0.041, 0.041, 0.976, 0.98, 0.98, 0.98, 0.041, 0.041, 0.98, 0.041, 0.98, 0.98, 0.98, 0.052, 0.951, 0.041, 0.98]
Stuff Correct: 1.0

<--------------------------------------------------------------->
`

The first line signifies the cycle. The first time this runs, the program will attempt to feed the data into an untrained network. Each successive backpropigation cycle trains the network to be more accurate.

The diagram is a representation of the network, with the weights and biases of each neuron shown. In this case, there is one input neuron, one hidden layer with two neurons, and one output neuron.

Generated Inputs are random, and the threshold for 0 vs 1 is at .5. The raw output is available at the bottom, as is the percentage of produced output that was correct.

After the last backpropagation cycle, the program will test the network against a new set of random inputs.



There are several ways to modify the training conditions.

Within main.py,
	train(x,y) - number of generated tests, number of backpropagation cycles
	test(x) - number of verification tests

Within testing.py,
	line 45, `rand_input = randint(-20, 20)`
	Modifying this allows you to change the range of generated inputs. It is suggested that this be centered on the domain you choose to test.

	line 50, `if (rand_input >= 0):`
	This is the test condition. Play with it as you like.
