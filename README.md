# TaskTracker

Gerenciador de tarefas em linha de comando (CLI) desenvolvido em Python 3 e empacotado com Docker para o Bootcamp II — Fase 3 (Entrega Final).

**Autor:** Renan Souza Gomes — Análise e Desenvolvimento de Sistemas — Polo Asa Norte

## Descrição funcional

O TaskTracker ajuda quem precisa conciliar estudos, trabalho e atividades pessoais a registrar o que precisa ser feito. Pelo terminal, o usuário pode:

1. **Cadastrar nova tarefa** — informa título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas** — lista todas as tarefas com seus dados e status.
3. **Sair da aplicação** — encerra o programa.

### Regras de negócio

| Campo | Regra |
|-------|-------|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o título é pedido novamente. |
| Descrição | Livre e opcional. Quando vazia, a listagem mostra "Sem descrição". |
| Prioridade | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`. Qualquer outro valor gera erro e o campo é pedido novamente. |
| Data limite | Data planejada para conclusão (formato livre ou DD/MM/AAAA). |
| Status | Definido automaticamente como `Pendente` no cadastro. |

As tarefas ficam em memória apenas durante a execução: ao sair, os registros da sessão são descartados.

## Tecnologias utilizadas

- Python 3.11 (somente biblioteca padrão)
- Docker e Docker Compose para empacotamento e execução
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore                   # Arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico entregue na Fase 1
├── src/
│   └── main.py                  # Código-fonte da aplicação (Fase 2)
├── Dockerfile                   # Receita da imagem da aplicação (Fase 3)
├── docker-compose.yml           # Execução interativa da CLI via orquestração (Fase 3)
└── README.md                    # Documentação principal e instruções de uso
```

## Execução com Docker

Pré-requisito: [Docker](https://docs.docker.com/get-docker/) instalado (no Windows e no macOS, o Docker Desktop já inclui o Docker Compose).

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/renan2026/tasktracker-projeto.git
cd tasktracker-projeto
```

### Como construir a imagem

```bash
docker build -t tasktracker .
```

### Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker
```

A flag `-it` mantém a entrada aberta e aloca um terminal, o que é necessário porque o menu usa `input()`. A flag `--rm` remove o container ao sair.

### Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker-app
```

O `docker-compose.yml` já define `stdin_open: true` e `tty: true`, que equivalem ao `-it`. Se a imagem ainda não existir, o Compose a constrói automaticamente. Depois de alterar o código, use `docker compose run --build --rm tasktracker-app` para reconstruí-la.

### Decisões técnicas do Dockerfile

| Instrução | Motivo |
|-----------|--------|
| `FROM python:3.11-slim` | Imagem base leve, com apenas o necessário para rodar Python. |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container. |
| `ENV PYTHONUNBUFFERED=1` | Faz as mensagens aparecerem no terminal imediatamente, sem buffer. |
| `COPY src/ /app/src/` | Copia só o código-fonte, mantendo a imagem pequena. |
| `CMD ["python", "src/main.py"]` | Inicia a aplicação quando o container sobe. |

A aplicação não tem dependências externas, por isso não há `requirements.txt` nem `pip install`.

## Execução sem Docker

Pré-requisito: [Python 3](https://www.python.org/downloads/) instalado.

```bash
python src/main.py
```

No Linux ou macOS, use `python3 src/main.py` caso o comando `python` não esteja disponível.
