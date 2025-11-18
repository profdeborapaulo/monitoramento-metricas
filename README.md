# Monitoramento de Métricas - Exemplo prático

Este projeto demonstra como definir indicadores de monitoramento e automatizar verificações usando  **GitHub Actions**.

## Objetivo
- Criar uma lista de métricas que seriam monitoradas em um sistema (fictício)
- Simular valores dessas métricas
- Automatizar validações via CI/CD

## Estrutura
- `docs/indicadores.md`: Documento com métricas definidas.
- `scripts/simular_metricas.py`: Script para gerar valores fictícios.
- `.github/workflows/pipeline.yml`: Pipeline CI-CD.

## Como usar
1. Clone este repositório.
2. Edite `docs/indicadores.md` com pelo menos 3 métricas
3. Faça commit e push para acionar o pipeline.