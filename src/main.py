"""TaskTracker: gerenciador de tarefas em linha de comando (Bootcamp II - Fase 2)."""

# Chaves em minúsculas para aceitar "alta", "ALTA" etc.; o valor é o nome que será armazenado.
PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}


def ler_titulo():
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade in PRIORIDADES:
            return PRIORIDADES[prioridade]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição (opcional): ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite (DD/MM/AAAA): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso.")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] or 'Sem descrição'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite'] or 'Não informada'}")
        print(f"  Status:      {tarefa['status']}")
    print(f"\nTotal de tarefas cadastradas: {len(tarefas)}")


def main():
    tarefas = []
    print("=== TaskTracker ===")
    print("Atenção: as tarefas ficam salvas apenas durante esta sessão.")
    while True:
        print("\n1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Sistema encerrado. Os registros desta sessão não serão mantidos.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
