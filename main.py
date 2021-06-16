import random

class Entradas():
    def __init__(self, valor, pesos):
        self.valor = int(valor)
        self.pesos = dict(pesos)

def somatorio(entradas, peso):
    print(f'Peso do somatório selecionado = {peso}')
    valorSomatorio = 0
    constante = 0
    for e in entradas:
        valorSomatorio += e['valor'] * e['pesos'][peso]
    return round(valorSomatorio + constante, 2)

def custo(valorObitido, valorIdeal):
    return round(((valorObitido - valorIdeal) ** 2), 2)

def gerarPesos(qtdPesos):
    pesos = {}
    for peso in range(qtdPesos):
        pesos[f'w{peso}'] = round(random.random(), 2)
    return pesos

def gerarListaDeEntradas(qtdEntradas, qtdPesosPorEntradas):
    entradas = []
    for entrada in range(qtdEntradas):
        vars()[f'e{str(entrada)}'] = {
            "nome": f'Entrada {str(entrada)}',
            "valor": round(random.random(), 2),
            "pesos": gerarPesos(qtdPesosPorEntradas)
        }
        entradas.append(vars()[f'e{str(entrada)}'])
    return entradas

def exibirListaDeEntradas(entradas):
    for item in entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')

def exibirListaDeEntradasBrutas(entradas):
    for item in entradas:
        print(item)
    print("\n")

def chamarPesoAleatorio(entrada):
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'

def chamarPesoAleatorio(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'

def calibrar(entradas, peso):
    for entrada in entradas:
        if(round(random.random(), 2) <= 0.50):
            entrada['pesos'][peso] = round(random.random(), 2) * -1
    return entradas

def run():
    qtdEntradas = 10
    qtdPesos = 10

    # print(f'Quantidade de entradas: {qtdEntradas}.\nQuantidade de pesos por entrada: {qtdPesos}.\n')

    entradas = gerarListaDeEntradas(qtdEntradas, qtdPesos)
    custoFinal = 0
    exibirListaDeEntradas(entradas)

    listaSomatorio = []
    listaIdeais = []
    for x in range(qtdPesos):
        somar = somatorio(entradas, f"w{x}")
        ideal = round(random.random(), 2)
        listaSomatorio.append(somar)
        listaIdeais.append(ideal)
        custoFinal += custo(somar, ideal)

    somatorios = somatorio(entradas, chamarPesoAleatorio(qtdPesos))

    print(f"\nLista de somatorios {listaSomatorio}")
    print(f"Lista de ideais {listaIdeais}")
    print(f"Custo final {custoFinal}\n")

    novasEntradas = calibrar(entradas, chamarPesoAleatorio(qtdPesos))
    for x in range(6):
        print("\n============== Novas entradas ==============\n")
        exibirListaDeEntradas(novasEntradas)
        somatorios = somatorio(novasEntradas, chamarPesoAleatorio(qtdPesos))
        custos = custo(somatorios, 1)
        print(f'Valor da função de ativação: {somatorios}')
        print(f'Valor da função de custo: {custos}')
        novasEntradas = calibrar(entradas, chamarPesoAleatorio(qtdPesos))
        print("\n============== Fim das novas entradas ==============")

    print(f"Entradas: {(entradas[1])}")
    print(f"Entradas: {(entradas[2])}")

if __name__ == '__main__':
    run()