import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = [(d['dia'], d['valor']) for d in dados if d['valor'] > 0]

dia_menor, menor_faturamento = min(faturamento, key=lambda x: x[1])
dia_maior, maior_faturamento = max(faturamento, key=lambda x: x[1])

media_mensal = sum(valor for _, valor in faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for _, valor in faturamento if valor > media_mensal)

print(f"Menor faturamento: R$ {menor_faturamento:.2f} (Dia {dia_menor})")
print(f"Maior faturamento: R$ {maior_faturamento:.2f} (Dia {dia_maior})")
print(f"Média mensal: R$ {media_mensal:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")