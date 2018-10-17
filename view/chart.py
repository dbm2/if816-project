import sys
import matplotlib.pyplot as plt

class Chart:

	def __init__(self, methods):

		fig, ax = plt.subplots()
		fig.set_size_inches(10.0, 6.0)

		for method in methods:
			name = method.type.getName()
			color = method.type.getColor()
			ax.plot(method.y, method.t, lw = 2, color = color, label = name)

		ax.set_title('Estimativas para os Métodos')
		ax.set_xlabel('valores de y')
		ax.set_ylabel('valores de t')

		ax.legend()
		
		fig.savefig('resources/chart.png', dpi=100)