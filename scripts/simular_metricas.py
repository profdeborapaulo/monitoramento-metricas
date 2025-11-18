import random
import json

# Este script simula métricas fictícias para monitoramento.

metrics = {
    "tempo_resposta": round(random.uniform(0.1, 2.0), 2),
    "taxa_erro": round(random.uniform(0,5), 2),
    "disponibilidade": round(random.uniform(95,100), 2)
} 

# Salva as métricas em um arquivo json

with open("resultados.json", "w") as f:
    json.dump(metrics,f)

print("Métricas simuladas: ", metrics)