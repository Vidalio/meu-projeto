
# calc.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
    
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


if __name__ == "__main__":
    print("Soma:", somar(5, 3))
    print("Subtração:", subtrair(5, 3))

