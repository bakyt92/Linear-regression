import sys
from ..ft_utils import ft_utils

class Training:
    epochs = 1000
    learning_rate = 0.01

    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0

    def ft_training(self, headers, data):
        learn_step = 0
        while learn_step < Training.epochs:
            self.ft_iteration(headers, data)

    def ft_iteration(self, headers, data):
        price_index = self.header.index('price')
        km_index = self.header.index('km')
        error_all = []
        for x in data:
            estimated_price = self.theta0 + self.theta1 * x[km_index]
            actual_price = x[price_index]
            error_step = estimated_price - actual_price
            error_all.append(error_step)
        

