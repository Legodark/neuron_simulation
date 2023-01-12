import numpy as np

class Neuron:

  def __init__(self, weights, bias, func):
    self.weights = weights
    self.bias = bias
    self.func = func

  def run(self, input_data):
    calculo = self.__calculate(input_data)
    if self.func == 'ReLU':

      activacion = self.__relu(calculo)
      return activacion
    
    elif self.func == 'Tangente hiperbólica':
      activacion = self.__tanh(calculo)
      return activacion
    
    elif self.func == 'Sigmoide':
      activacion = self.__sigmoid(calculo)
      return activacion

  def __calculate(self, input_data):
    x = np.array(input_data)
    w = np.array(self.weights)

    y = np.dot(x, w) + self.bias
    
    return y
  
  def change_bias(self, bias):
    self.bias = bias

  @staticmethod
  def __relu(calculo):
    return np.maximum(0, calculo)

  @staticmethod
  def __tanh(calculo):
    return np.tanh(calculo)

  @staticmethod
  def __sigmoid(calculo):
    return 1 / (1 + np.exp(-calculo))