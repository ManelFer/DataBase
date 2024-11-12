import json


class Personagem:
    def __init__(self, nome, nivel, saude):
        self.nome = nome
        self.nivel = nivel
        self.saude = saude
        self.acoes = []

    def registrar_acoes(self, acao):
        self.acoes.append(acao)

    def mostrar_acoes(self):
        print(f'Ações de {self.nome}:')
        for acao in self.acoes:
            print(f"-{acao}")
    
    def salvar(self):
        with open(f"{self.nome}.json", "w") as f:
            json.dump(self.__dict__, f)

    @classmethod
    def carregar(cls, nome):
        with open (f"{nome}.json", "r") as f:
            dados = json.load(f)
            personagem = cls(dados['nome'])
            personagem.nivel = dados['nivel']
            personagem.saude = dados ['saude']
            personagem.acoes = dados ['acoes']
            return personagem
def main():
    print("""
        ============= Bem vindo ao CyberOeste =============
          
          ( 1 ) Iniciar
          ( 2 ) Historia
          ( 3 ) Finalizar

        ============= Bem vindo ao CyberOeste ============= 

""")
    opcoes = input("Escolha uma opão!!!!!!!")
    if opcoes == '1':
        nome = input("Olá, Bem vindo ao novo oeste vejo que é novo na cidade qual o seu nome: ")
        personagem = nome
        print(f"{nome} Bem vindo!!!!!")

    elif opcoes == '2':
        print("Aqui vai ser a historia do jogo")

    elif opcoes == '3':
        print("obrigado por jogar!!!")
    else:
        print("opção invalida, tente novamente!!!")

if __name__ == "__main__":
    main()
    
