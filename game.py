import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Gastos Compulsivos")
        self.saldo = 1000
        self.genero = None

        # Perguntas específicas para homens e mulheres
        self.perguntas_homem = [
            {"texto": "Promoção de eletrônicos! Comprar um fone por R$250?", "gasto": 250},
            {"texto": "Jaqueta de marca com 50% de desconto por R$300. Comprar?", "gasto": 300},
            {"texto": "Convite para jogo de futebol com ingressos a R$200. Aceitar?", "gasto": 200},
            {"texto": "Jantar com os amigos por R$150. Participar?", "gasto": 150},
            {"texto": "Coleção de filmes clássicos por R$180. Comprar?", "gasto": 180}
        ]
        self.perguntas_mulher = [
            {"texto": "Promoção em conjunto de maquiagem por R$180. Comprar?", "gasto": 180},
            {"texto": "Vestido de festa por R$350. Comprar?", "gasto": 350},
            {"texto": "Dia de spa com amigas por R$400. Participar?", "gasto": 400},
            {"texto": "Curso de culinária por R$150. Participar?", "gasto": 150},
            {"texto": "Kit de produtos para cabelo por R$100. Comprar?", "gasto": 100}
        ]
        
        self.pergunta_atual = 0
        self.criar_interface_inicial()

    def criar_interface_inicial(self):
        self.label_intro = tk.Label(self.root, text="Bem-vindo ao Quiz de Gastos Compulsivos!")
        self.label_intro.pack(pady=10)

        self.label_genero = tk.Label(self.root, text="Escolha seu gênero para começar:")
        self.label_genero.pack(pady=5)

        self.botao_homem = tk.Button(self.root, text="Homem", command=lambda: self.iniciar_quiz("homem"))
        self.botao_homem.pack(side="left", padx=10)

        self.botao_mulher = tk.Button(self.root, text="Mulher", command=lambda: self.iniciar_quiz("mulher"))
        self.botao_mulher.pack(side="right", padx=10)

    def iniciar_quiz(self, genero):
        self.genero = genero
        self.perguntas = self.perguntas_homem if genero == "homem" else self.perguntas_mulher
        self.label_intro.pack_forget()
        self.label_genero.pack_forget()
        self.botao_homem.pack_forget()
        self.botao_mulher.pack_forget()

        # Interface do quiz após a escolha do gênero
        self.label_saldo = tk.Label(self.root, text=f"Saldo: R${self.saldo}")
        self.label_saldo.pack(pady=10)

        self.label_pergunta = tk.Label(self.root, text=self.perguntas[self.pergunta_atual]["texto"])
        self.label_pergunta.pack(pady=10)

        self.botao_sim = tk.Button(self.root, text="Sim", command=self.gastar)
        self.botao_sim.pack(side="left"
        , padx=10)

        self.botao_nao = tk.Button(self.root, text="Não", command=self.proxima_pergunta)
        self.botao_nao.pack(side="right", padx=10)

    def gastar(self):
        gasto = self.perguntas[self.pergunta_atual]["gasto"]
        self.saldo -= gasto
        self.atualizar_saldo()

    def proxima_pergunta(self):
        self.pergunta_atual += 1
        if self.pergunta_atual < len(self.perguntas):
            self.label_pergunta.config(text=self.perguntas[self.pergunta_atual]["texto"])
        else:
            self.finalizar_quiz()

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R${self.saldo}")
        self.proxima_pergunta()

    def finalizar_quiz(self):
        if self.saldo > 500:
            mensagem = "Você aparenta ter um bom controle financeiro."
        else:
            mensagem = "Aparentemente você costuma gastar mais do que recebe."
        messagebox.showinfo("Resultado", mensagem)
        self.root.quit()

# Inicia o quiz
root = tk.Tk()
app = Quiz(root)
root.mainloop()
