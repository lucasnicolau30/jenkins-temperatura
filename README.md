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

## Cenários

Cada cenário usa um job no Jenkins apontando para uma branch deste repositório.

| # | Cenário | Branch | Resultado esperado |
|---|---------|--------|--------------------|
| 1 | Sucesso | `main` | build SUCCESS, 4 testes passam |
| 2 | Falha de compilação | `cenario2-falha-compilacao` (erro de sintaxe em `celsius_para_fahrenheit`) | estágio Build falha, FAILURE |
| 3 | Teste falha | `cenario3-teste-falha` (`(f - 32)` trocado por `(f - 30)`) | build UNSTABLE, 2 testes falham |
| 4 | Agendado | `cenario4-agendado` (`cron('* * * * *')` no Jenkinsfile) | build automático com SUCCESS, sem clicar |
| 5 | Cobertura (bônus) | `main` | estágio Cobertura mostra 100% no log |

A `main` contém sempre o código correto. Os defeitos dos cenários 2 e 3 ficam apenas nas branches.
