import sys
from models.input import Input

entry = Input("resources/entrada.txt")
entry.parseAndAssembleMethods()

for x in range(0,4):
	print(entry.methods[x].type)
	entry.methods[x].calculate()
	print()


