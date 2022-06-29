import numpy as np
import nnfs
from nnfs.datasets import spiral_data

# easy ML dataset package
nnfs.init()

class ReLU:
    """Some notes about ReLU:
    1. ReLU is not normalized, meaning values can range from [0,infinity]
    2. ReLU outputs are completely independent of each other (exclusive)
    3. Because of the two reasons above, ReLU cannot be used in the final layer for predicting probabilities (classification)
    4. np.maximum takes the element wise max between two arrays
    """
    
    def forward(self, inputs):
        
        # any negative values are turned into 0
        self.output = np.maximum(0, inputs)
        
class Softmax:
    """Some notes about softmax:
    1. Softmax returns a probability distribution (all the floats add up to 1)
    2. Each probability score also represents a confidence score (i.e., [.45, .55] means the model has low confidence)
    3. Softmax is almost exclusively used in the output layer
    """
    
    def forward(self, inputs):
        
        """More notes:
        1. axis=1 specifies that we should only operate across rows, not columns
        
        2. keepdims=True makes it so the output array has the same dimensions as the input
        
        3. we subtract the largest of the inputs to prevent "dead neurons" and exploding values.
            - Dead neurons = when neurons start always outputting a specific value and thus have a zero gradient
            - exploding values = when values start getting exponentially large
            
        4. performing this subtraction scales the values to a range [-1,0]
        
        """
        
        # get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        
        # normalize them for each sample
        probs = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        
        self.output = probs

class DenseLayer:
    
    def __init__(self, n_inputs, n_neurons):
        
        # initialize random weights. The shape is (input size, # of desired neurons)
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) # scale the weights down for faster training
        
        # initialize biases as zero vectors
        self.biases = np.zeros((1, n_neurons))
         
    def forward(self, inputs):
        # weighted sum
        self.output = np.dot(inputs, self.weights) + self.biases
        
        

        
X,y = spiral_data(samples=100, classes=3)

dense1 = DenseLayer(2,3)
relu = ReLU()

# create second Dense layer as the output layer with 3 input features (output of previous layer) and 3 output values
dense2 = DenseLayer(3,3)
softmax = Softmax()


# training data forward pass through Dense layer and forward pass through ReLU
dense1.forward(X)
relu.forward(dense1.output)

# make a forward pass through the second Dense layer
# takes the output of previous layer as input
dense2.forward(relu.output)
softmax.forward(dense2.output)

print(softmax.output[:5])