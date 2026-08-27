class tarefa:
    def __init__(self, titulo, concluido=False):
        self.titulo = titulo
        self.concluido = concluido

tarefas = [
    tarefa("Estudar Python"),
    tarefa("Fazer exercícios"),
    tarefa("Treinar"),
    tarefa("Devocional"),
    tarefa("Ler Bíblia")
]
def concluir(tarefa):
    tarefa.concluido = True
    print(f"Concluindo a tarefa '{tarefa.titulo}'.")
    print(f"Tarefa '{tarefa.titulo}' concluída!")

concluir(tarefas[0])

def pendentes(lista_tarefas):
    return [t for t in lista_tarefas if not t.concluido]

lista_pendentes = pendentes(tarefas)

print("\nTarefas pendentes:")
for t in lista_pendentes:
    print("-", t.titulo)