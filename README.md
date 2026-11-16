# Jenkins + GitHub: build e testes automáticos (Python)

Projeto da Segunda Atividade Prática de Gerência de Configuração (UFAM, 2026-2).

Contém dois métodos em `src/temperatura.py` (Fahrenheit para Celsius e Celsius para Fahrenheit),
quatro testes Pytest em `tests/` e um `Jenkinsfile` com o pipeline.

## Rodar local

    python3 -m venv .venv && . .venv/bin/activate
    pip install -r requirements.txt
    python -m pytest --cov=src

## Configurar no Jenkins

1. Plugins: Git, Pipeline e JUnit.
2. Novo item > Pipeline > Pipeline script from SCM > Git > URL do repositório > branch `main` > Script Path `Jenkinsfile`.
3. A máquina do Jenkins precisa de `python3` e `python3-venv`.

## Cenários (o que alterar em src/temperatura.py antes de cada build)

| # | Cenário | Alteração | Resultado esperado |
|---|---------|----------|--------------------|
| 1 | Sucesso | nenhuma | build SUCCESS, 4 testes passam |
| 2 | Falha de compilação | remover o `32` da linha `return c * 9 / 5 + 32` | estágio Build falha, FAILURE |
| 3 | Teste falha | trocar `(f - 32)` por `(f - 30)` | build UNSTABLE, testes vermelhos |
| 4 | Agendado | trigger `* * * * *` (demo), sem clicar em Build | build automático com SUCCESS |
| 5 | Cobertura | nenhuma | estágio Cobertura mostra 100% no log |

Depois de cada cenário, desfaça a alteração.
