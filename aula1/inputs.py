salario = float(input("Salario: "))

inss = salario * 0.075
fgts = salario * 0.11

print(f"Desconto INSS: {inss} \nDesconto FGTS: {fgts} \nSalario liquido: {salario - (fgts + inss)}")