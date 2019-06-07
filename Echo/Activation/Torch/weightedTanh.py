'''
Applies the weighted tanh function element-wise:
f(x) = tanh(x * weight)
'''

# import pytorch
import torch
from torch import nn

# import activation functions
import Echo.Activation.Torch.functional as Func

class weightedTanh(nn.Module):
    '''
    Applies the weighted tanh function element-wise: weighted_tanh(x) = tanh(x * weight)

    Shape:
        - Input: (N, *) where * means, any number of additional
          dimensions
        - Output: (N, *), same shape as the input

    Examples:
        >>> m = weightedTanh(weight = 1)
        >>> input = torch.randn(2)
        >>> output = m(input)

    '''
    def __init__(self, weight = 1):
        '''
        Init method.
        INPUT:
            weight - weight to be multiplied with the argument of the function
        '''
        super().__init__()
        self.weight = weight

    def forward(self, input):
        '''
        Forward path of the function.
        '''
        return Func.weighted_tanh(input, self.weight)
