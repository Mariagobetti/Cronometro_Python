from tkinter import *
import tkinter as tk

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("⏱️ Cronômetro")
        self.janela.geometry("470x280")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#f0f2f5")

        # Variáveis de estado do cronômetro
        self.tempo = 0        # Tempo em segundos
        self.rodando = False  # Estado do cronômetro (ligado/desligado)

        self.criar_interface()

    def criar_interface(self):
        # Container principal
        container = Frame(self.janela, bg="#f0f2f5", relief="ridge", bd=2)
        container.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Título
        titulo = Label(container, text="⏱️ CRONÔMETRO", font=("Arial", 12, "bold"), bg="#f0f2f5", fg="#171718")
        titulo.pack(pady=10)

        # Display
        self.display = Label(
            container, text="00:00:00", font=("Arial", 40, "bold"), bg="#4a90e2", fg="#ffffff", width=10
        )
        self.display.pack(pady=15)

        # Botões de controle
        botoes_frame = Frame(container, bg="#f0f2f5")
        botoes_frame.pack(pady=10, expand=True, fill=X)

        # Botão Iniciar
        self.btn_iniciar = Button(
            botoes_frame, text="Iniciar", font=("Arial", 12, "bold"), bg="#48da23", fg="white", command=self.iniciar
        )
        self.btn_iniciar.pack(side=LEFT, padx=5, expand=True, fill=BOTH)

        # Botão Pausar
        self.btn_pausar = Button(
            botoes_frame, text="Pausar", font=("Arial", 12, "bold"), bg="#f39c12", fg="white", command=self.pausar
        )
        self.btn_pausar.pack(side=LEFT, padx=5, expand=True, fill=BOTH)

        # Botão Zerar / Encerrar (adicionado para conectar com o método encerrar)
        self.btn_encerrar = Button(
            botoes_frame, text="Zerar", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", command=self.encerrar
        )
        self.btn_encerrar.pack(side=LEFT, padx=5, expand=True, fill=BOTH)

    def atualizar_tempo(self):
        if self.rodando:
            self.tempo += 1
            
            # Formatação de horas, minutos e segundos
            horas = self.tempo // 3600
            minutos = (self.tempo % 3600) // 60
            segundos = self.tempo % 60
            
            texto_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.display.config(text=texto_formatado)
            
            # Chama a função novamente após 1000ms (1 segundo)
            self.janela.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.btn_iniciar.config(text="Continuar")
            self.atualizar_tempo()

    def pausar(self):
        if self.rodando:
            self.rodando = False

    def encerrar(self):
        self.rodando = False
        self.tempo = 0
        self.display.config(text="00:00:00")
        self.btn_iniciar.config(text="Iniciar")


if __name__ == "__main__":
    janela = tk.Tk()
    app = Cronometro(janela)
    janela.mainloop()