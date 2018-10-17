import sys
from sympy import sympify
from enums.methodstype import MethodsType
from models.method import Method

class InversedFormula(Method):

	def __init__(self, type, y, t, stepsSize, steps, function, order):
		self.type = type
		self.y = y
		self.t = t
		self.stepsSize = stepsSize
		self.steps = steps
		self.function = sympify(function)
		self.order = order