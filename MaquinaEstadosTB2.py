from transitions import Machine

class MaquinaHeroi(object):

    estados = ['iniciando_aventura', 'enfrentando_lorde', 'salvando_princesa', 'recuperando_energias', 'encontrando_amigos']

    def __init__(self, nome):
        self.nome = nome
        self.amigos_encontrados = 1
        self.maquina = Machine(model=self, states=MaquinaHeroi.estados, initial='iniciando_aventura')

        # Adicionando transições
        self.maquina.add_transition('lutar', '*', 'enfrentando_lorde')
        self.maquina.add_transition('escalar_torre', '*', 'salvando_princesa')
        self.maquina.add_transition('descansar', '*', 'recuperando_energias')
        self.maquina.add_transition('continuar_jornada', '*', 'encontrando_amigos', after='atualizar_diario')

    def atualizar_diario(self):
        self.amigos_encontrados += 1
        print(f"{self.nome} encontrou {self.amigos_encontrados} amigos.")

if __name__ == "__main__":
    nome_heroi = "Shrek"
    heroi = MaquinaHeroi(nome_heroi)

    # Verificando o estado inicial
    print(f"\nEstado inicial de {nome_heroi}: {heroi.state}")

    while True:
        acao = input("\nEscolha uma ação (continuar_jornada / lutar / escalar_torre / descansar / sair): ").lower()

        if acao == 'sair':
            print("Programa encerrado.")
            break

        try:
            getattr(heroi, acao)()
        except AttributeError:
            print("Ação inválida. Tente novamente.")

        print(f"{heroi.nome} está agora no estado: {heroi.state}")

