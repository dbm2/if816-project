import sys
from inout.input import Input
from inout.output import Output
from view.chart import Chart

print("- Projeto de Metodos Numericos.")
print("- Autor: Daniel Barbosa Maranhao | dbm2 | 107.698.344-85\n")

print("Iniciando leitura do arquivo resources/entrada.txt...")
entry = Input("resources/entrada.txt")
entry.parseAndAssembleMethods()

print("Calculando estimativas dos metodos numericos...")
for method in entry.methods:
	method.calculate()

print("Escrevendo resultados dos metodos no arquivo resources/saida.txt...")
exit = Output("resources/saida.txt", entry.methods)
exit.transcriptMethods()

print("Gerando graficos comparativso dos metodos na pasta resources/charts...\n")
view = Chart(entry.methods)
view.drawForEachMethod()
view.drawForAllMethods()

print("Pronto!")