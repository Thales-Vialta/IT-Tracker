from questionary import Style

CORES = {
    "RESET": "\033[0m",
    "NEGRITO": "\033[1m",
    "VERDE": "\033[32m",
    "AMARELO": "\033[33m",
    "AZUL": "\033[34m",
    "VERMELHO": "\033[31m"
}

minhas_cores = Style([
    ('question', 'fg:#FFF000 bold'),    # Cor do texto da pergunta
    ('answer', 'fg:#0055FF bold'),      # Cor da resposta depois de escolhida
    ('pointer', 'fg:#0055FF bold'),     # Cor da setinha (») que aponta para a opção
    ('highlighted', 'fg:#FFFFFF bold'), # Cor da opção selecionada no momento
    ('selected', 'fg:#ccff00'),         # Cor do texto selecionado
    ('disabled', 'fg:#858585 italic')   # Cor de opções desativadas
])