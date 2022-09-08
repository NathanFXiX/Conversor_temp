from tkinter import *
from tkinter import ttk

############################################################

# Variavel global root que usa o Tkinter
root = Tk()

# Ícone do app
root.iconbitmap("thermometer.ico")

# class Functions():

############################################################

# Classe que englobla e organiza as funções do programa

class App():

    ############################################################

    # Ao iniciar:
    def __init__(self):
        self.root = root
        self.screen()
        self.main_frame()
        self.widgets()


        root.mainloop()

    ############################################################

    # Configurações de tela e título:
    def screen(self):
        # Título:
        self.root.title("Conversor de temperaturas")

        # Background:
        self.root.configure(background='lightblue')

        # Ajustes de fundo e permissões de ajustamento do usuário:
        self.root.wm_minsize(720, 480)
        self.root.resizable(False, False)

    # Função que cria o frame branco principal:
    def main_frame(self):
        self.frame = Frame(self.root, bd=4, highlightbackground='black')
        self.frame.place(relx=0.012, rely=0.012, relwidth=0.98, relheight=0.98)
        self.frame.configure(background='white')

    # Função que cria os widgets na tela:
    def widgets(self):

        # Label perguntando temperatura:
        self.temp_label = Label(self.frame, text='Qual a temperatura a ser convertida?')
        self.temp_label.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.06)
        self.temp_label.configure(background='white', font=('Dialog', 12, 'bold'))

        # Lista com as temperaturasa disponíveis:
        lista_temperaturas = [
            'C°',
            'F',
        ]

        # ComboBox para selecionar as temperaturas:
        self.combo_temp = ttk.Combobox(self.frame, values=lista_temperaturas, font=('Dialog', 12), state='readonly')
        self.combo_temp.place(relx=0.01, rely=0.07, relheight=0.05, relwidth=0.08)
        self.combo_temp.set('C°')

        # Entry para por a temperatura:
        self.temp_entry=Entry(self.frame, font=('Dialog', 12))
        self.temp_entry.place(relx=0.1, rely=0.07, relheight=0.05, relwidth=0.1)

        # Função que converte F para C e C para F:
        def converter():

            tipo_de_temp = self.combo_temp.get()
            valor_temp = self.temp_entry.get()

            if tipo_de_temp == 'F':
                resultado = (int(valor_temp) - 32) * 5 / 9
                print(resultado)
                self.label_resul = Label(text=f"O resultado da conversão é igual a: {round(resultado, 2)}")
                self.label_resul.place(relx=0.1, rely=0.18, relheight=0.06, relwidth=0.6)
                self.label_resul.configure(font=('Dialog', 12), background='white')

            else:
                resultado = (int(valor_temp) * 9 / 5) + 32
                print(resultado)
                self.label_resul = Label(text=f"O resultado da conversão é igual a: {round(resultado, 2)}")
                self.label_resul.place(relx=0.03, rely=0.18, relheight=0.06, relwidth=0.6)
                self.label_resul.configure(font=('Dialog', 12), background='white')


        self.conver_btn=Button(self.frame, text='Converter', font=('Dialog', 12), command=converter)
        self.conver_btn.place(relx=0.23, rely=0.07, relheight=0.06, relwidth=0.13)






App()
