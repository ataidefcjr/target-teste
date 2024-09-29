faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

print(f"Faturamento total: R${faturamento_total:.2f}")
print(f"SP - R$ {faturamento_sp}: = {percentual_sp:.2f}%")
print(f"RJ - R$ {faturamento_rj}: = {percentual_rj:.2f}%")
print(f"MG - R$ {faturamento_mg}: = {percentual_mg:.2f}%")
print(f"ES - R$ {faturamento_es}: = {percentual_es:.2f}%")
print(f"outros - R$ {faturamento_outros}: = {percentual_outros:.2f}%")
