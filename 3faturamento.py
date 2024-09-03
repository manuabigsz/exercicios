import json

def analisar_faturamento(dados):
    if isinstance(dados, list):
        faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]
    else:
        faturamento_valido = [dia["valor"] for dia in dados["faturamento_diario"] if dia["valor"] > 0]

    if not faturamento_valido:
        return "Nenhum dia de faturamento válido encontrado."

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

with open('dados.json', 'r') as arquivo:
    dados_faturamento = json.load(arquivo)

resultado = analisar_faturamento(dados_faturamento)

print(f"Menor faturamento: R$ {resultado['menor_faturamento']:.2f}")
print(f"Maior faturamento: R$ {resultado['maior_faturamento']:.2f}")
print(f"Dias com faturamento acima da média: {resultado['dias_acima_da_media']}")
