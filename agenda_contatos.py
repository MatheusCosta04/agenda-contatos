class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:
    def __init__(self):
        self.contatos = []

    def add_contato(self, contato):
        self.contatos.append(contato)

    def listar_contato(self):
        for contato in self.contatos:
            print(f"Nome:{contato.nome}, Telefone: {contato.telefone} Email: {contato.email} " )

    def buscar_contato(self, nome):
        for c in self.contatos:
            if c.nome.lower() == nome.lower():
                return c
        return None
    
    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            print(f"Contato {nome} removido com sucesso.")
        else: 
            print("Contato não encontrado")


agenda = Agenda()

while True:
    print("\n 1. Listar contatos\n 2. Adicionar contato\n 3. Buscar contato\n 4. Remover contato\n 5. Sair")
    escolha = input("Escolha: ")
    
    if escolha == "1":
        if not agenda.contatos:
            print("Nenhum contato para listar.")
        agenda.listar_contato()

    elif escolha == "2":
        nome = input("Nome: ")
        telefone = input("Telefone:")
        email = input("Email: ")
        novo_contato = Contato(nome, telefone, email)
        agenda.add_contato(novo_contato)
        
    elif escolha == "3":
        nome = input("Digite um nome para buscar: ")
        contato = agenda.buscar_contato(nome)
        if contato:
            print(f"Encontrado: Nome {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        else:
            print("Contato não encontrado")
        
    elif escolha == "4":
        if not agenda.contatos:
            print("Nenhum contato para remover.")
        else:
            nome = input("Digite o nome para remover:")
            agenda.remover_contato(nome)
            
    elif escolha == "5":
        print("Saindo...")
        break
    
    else:
        print("Opção Inválida, tente novamente.")