import sys
from models.input import Input

entry = Input("resources/entrada.txt")
entry.parseAndAssembleMethods()

entry.methods[2].calculate()

