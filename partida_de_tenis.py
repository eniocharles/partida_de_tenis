import random

class Jogador:
    def __init__(self, nome, endereco, telefone, data_nascimento, nivel_habilidade):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.idade = self.calcular_idade(data_nascimento)
        self.nivel_habilidade = nivel_habilidade

    def calcular_idade(self, data_nascimento):
        return 2023 - int(data_nascimento.split('/')[-2])

class Partida:
    def __init__(self, data, horario, quadra_agendada):
        self.data = data
        self.horario = horario
        self.quadra_agendada = quadra_agendada
        self.jogadores = {}

    def registrar_jogador(self, jogador):
        if len(self.jogadores) < 2:
            self.jogadores[jogador.nome] = jogador.pontuacao
        else:
            print("A partida já tem dois jogadores registrados.")

    def apresentar_placar(self):
        if len(self.jogadores) == 2:
            nomes_jogadores = list(self.jogadores.keys())
            placar = f"Placar: {nomes_jogadores[0]} {self.jogadores[nomes_jogadores[0]].pontos} x {nomes_jogadores[1]} {self.jogadores[nomes_jogadores[1]].pontos}"
            print(placar)
        else:
            print("A partida ainda não tem dois jogadores registrados.")

    def marcar_ponto(self, nome_jogador, pontos):
        if nome_jogador in self.jogadores:
            self.jogadores[nome_jogador].pontos += pontos
            print(f"{nome_jogador} marcou {pontos} ponto(s).")
        else:
            print(f"Jogador {nome_jogador} não encontrado na partida.")

    def fim_da_partida(self):
        if len(self.jogadores) == 2:
            jogadores_pontos = list(self.jogadores.values())
            nomes_jogadores = list(self.jogadores.keys())

            if jogadores_pontos[0].pontos > jogadores_pontos[1].pontos:
                vencedor_nome, vencedor_pontos = nomes_jogadores[0], jogadores_pontos[0]
            elif jogadores_pontos[1].pontos > jogadores_pontos[0].pontos:
                vencedor_nome, vencedor_pontos = nomes_jogadores[1], jogadores_pontos[1]
            else:
                print("Houve um empate!")
                return

            print(f"Fim da partida. Vencedor: {vencedor_nome} ({vencedor_pontos.pontos} pontos)")
        else:
            print("A partida ainda não tem dois jogadores registrados.")

class PontuacaoJogador:
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.pontos = 0

if __name__ == "__main__":
    jogador1 = Jogador("Rangel", "Morro do Tiro", "123456789", "01/01/1985", 9)
    jogador2 = Jogador("André", "Pau Ferrado", "987654321", "15/06/1987", 9)
    jogador1.pontuacao = PontuacaoJogador(jogador1.nome)
    jogador2.pontuacao = PontuacaoJogador(jogador2.nome)

    partida = Partida("16/10/2023", "15:00", "Quadra do IFPI")

    partida.registrar_jogador(jogador1)
    partida.registrar_jogador(jogador2)

    partida.marcar_ponto("Rangel", 2)
    partida.marcar_ponto("André", 1)
    partida.marcar_ponto("André", 2)
    partida.marcar_ponto("Rangel", 1)

    partida.apresentar_placar()
    partida.fim_da_partida()