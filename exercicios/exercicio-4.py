# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda"

def biggest_name(list_names):
    biggest = ''
    for name in list_names:
        if len(name) > len(biggest):
            biggest = name
    print(biggest)

biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
