# TaskTracker

Gerenciador de tarefas em linha de comando (CLI) desenvolvido em Python 3 para o Bootcamp II — Fase 2 (Entrega Intermediária).

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

- Python 3 (somente biblioteca padrão)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação principal e instruções de uso
├── .gitignore                   # Arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico entregue na Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação
```

## Instalação e execução

Pré-requisito: [Python 3](https://www.python.org/downloads/) instalado.

```bash
git clone https://github.com/<seu-usuario>/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

No Linux ou macOS, use `python3 src/main.py` caso o comando `python` não esteja disponível.

## Próximos passos (Fase 3)

Empacotamento da aplicação, containerização com Docker, testes e deploy.
