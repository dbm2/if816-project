import sys

class Output:

	def __init__(self, file, methods):
		self.file = file
		self.methods = methods


	def transcriptMethods(self):
		f = open(self.file, "w")

		for method in self.methods:
			self._writeMethodDefinitions(f, method)
			self._writeMethodCalculations(f, method)
			f.write('\n')

		f.close()

	@classmethod
	def _writeMethodDefinitions(self, f, method):
			name = method.type.getName()
			t0 = str(method.t[0])
			y0 = str(method.y[0])
			h = str(method.stepsSize)

			f.write(name + '\n')
			f.write('y(' + t0 + ') = ' + y0 + '\n')
			f.write('h = ' + h + '\n')

	@classmethod
	def _writeMethodCalculations(self, f, method):
		if len(method.y) > 1:
			for i in range(1, len(method.y)):
				y = str(method.y[i])
				s = str(i)
				f.write(s + ' ' + y + '\n')