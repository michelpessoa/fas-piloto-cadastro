# Contexto vivo

Rascunho para revisão humana. Projeto fictício, sem dado real.

## Arquitetura
API FastAPI em `src/clientes/api.py`. Dados em dicionário na memória (`_clientes`).

## Convenções
- Português em nomes de domínio e mensagens.
- Testes em `tests/`, com `TestClient`. Limpar `_clientes` em `setup_function`.
- Lint: `ruff check .`. Testes: `python -m pytest -q`.

## Armadilhas
- Estado global: teste que não limpa `_clientes` afeta o seguinte.
- Sem rede no ambiente: dependência nova exige decisão humana.
