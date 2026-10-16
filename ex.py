"""Simulação de monitoramento do nível de água de um reservatório."""

from colorama import Fore, Style, init

# Ativa as cores no terminal e restaura automaticamente o estilo ao final.
init(autoreset=True)

NIVEIS = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado."""
    for item in NIVEIS:
        if item["nivel"] == nivel:
            return item["cor"]
    return Fore.WHITE


def exibir_alerta(nivel):
    """Exibe no terminal a situação do reservatório com a cor adequada."""
    for item in NIVEIS:
        if item["nivel"] == nivel:
            cor = definir_cor(nivel)
            print(cor + f'Nível {nivel}: {item["situacao"]}' + Style.RESET_ALL)
            return

    print(Fore.WHITE + f"Nível {nivel}: valor inválido (use um nível de 1 a 5)." + Style.RESET_ALL)


def main():
    """Simula a leitura dos cinco níveis do reservatório."""
    print("Monitoramento do reservatório de água")
    print("=" * 38)

    # Valores definidos no código, conforme permitido na atividade.
    leituras = [1, 2, 3, 4, 5]
    for nivel in leituras:
        exibir_alerta(nivel)


if __name__ == "__main__":
    main()
