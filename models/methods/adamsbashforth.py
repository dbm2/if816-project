import sys
from sympy import sympify
from enums.methodstype import MethodsType
from models.method import Method
from models.methods.euler import Euler
from models.methods.rungekutta import RungeKutta

class AdamsBashForth(Method):

	coefficients = [
		[1],
		[3/2, -1/2], 
		[23/12, -4/3, 5/12], 
		[55/24, -59/24, 37/24, -3/8], 
		[1901/720, -1387/360, 109/30, -637/360, 251/720],
		[4277/1440, -2641/480, 4991/720, -3649/720, 959/480, -95/288],
		[198721/60480, -18637/2520, 235183/20160, -10754/945, 135713/20160, -5603/2520, 19087/60480],
		[16083/4480, -1152169/120960, 242653/13440, -296053/13440, 2102243/120960, -115747/13440, 32863/13440, -5257/17280]
	]

	def __init__(self, type, y, t, stepsSize, steps, function, order):
		self.type = type
		self.y = y
		self.t = t
		self.stepsSize = stepsSize
		self.steps = steps
		self.function = sympify(function)
		self.order = order

		while len(self.t) < len(self.y):
			self.t.append(self.t[-1] + self.stepsSize)

	def calculate(self):

		if self.type != MethodsType.ADAMS_BASHFORTH:
			predictionMethod = None
			if self.type == MethodsType.ADAMS_BASHFORTH_BY_EULER:
				predictionMethod = Euler(MethodsType.EULER, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_BASHFORTH_BY_EULER_INVERSE:
				predictionMethod = Euler(MethodsType.EULER_INVERSE, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_BASHFORTH_BY_EULER_IMPROVED:
				predictionMethod = Euler(MethodsType.EULER_IMPROVED, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_BASHFORTH_BY_RUNGE_KUTTA:
				predictionMethod = RungeKutta(MethodsType.RUNGE_KUTTA, self.y, self.t, self.stepsSize, self.order - 1, self.function)
				
			predictionMethod.calculate()

		for i in range(len(self.t), self.steps + 1):
			previousTs = self.t[-self.order:]
			previousYs = self.y[-self.order:]

			v = self.calculateByAdamsBashForth(previousYs, previousTs)

			self.t.append(v[0])
			self.y.append(v[1])


	def calculateByAdamsBashForth(self, previousYs, previousTs):

		previousFunctionsEvaluations = 0.0
		for i in range(0, self.order):
			y = previousYs[self.order - i - 1]
			t = previousTs[self.order - i - 1]
			f = self.evaluateFunction(y, t)
			previousFunctionsEvaluations += (AdamsBashForth.coefficients[self.order - 1][i] * f)

		nextT = previousTs[-1] + self.stepsSize
		nextY = previousYs[-1] + self.stepsSize * previousFunctionsEvaluations

		return (nextT, nextY)