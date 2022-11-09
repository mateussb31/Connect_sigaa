# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from cProfile import label
from ctypes import alignment
from doctest import OutputChecker
from textwrap import fill
from tkinter import *
from unicodedata import name
from Sigaa import *
from turtle import bgcolor, left
from pathlib import Path
from tkinter import BOTTOM, LEFT, RIGHT, Frame, Tk, Canvas, Text, Button, PhotoImage

# from abre_boletim import *
# Explicit imports to satisfy Flake8


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def adequa_tamanho_nota(s):
    resultado = ""
    if len(s) > 22:
        s = s.split()
        for i in s:
            if i == "DE" or i == "DO":
                continue
            else:
                resultado += str(i[0])
        return resultado
    else:
        return s


def adequa_tamanho_atividade(s):
    resultado = ""


def round_rectangle(x1, y1, x2, y2, local, radius=25, **kwargs):

    points = [
        x1 + radius,
        y1,
        x1 + radius,
        y1,
        x2 - radius,
        y1,
        x2 - radius,
        y1,
        x2,
        y1,
        x2,
        y1 + radius,
        x2,
        y1 + radius,
        x2,
        y2 - radius,
        x2,
        y2 - radius,
        x2,
        y2,
        x2 - radius,
        y2,
        x2 - radius,
        y2,
        x1 + radius,
        y2,
        x1 + radius,
        y2,
        x1,
        y2,
        x1,
        y2 - radius,
        x1,
        y2 - radius,
        x1,
        y1 + radius,
        x1,
        y1 + radius,
        x1,
        y1,
    ]

    return local.create_polygon(points, **kwargs, smooth=True)


# Executa a função de abrir o sigaa -> para cada elemento no dicionário retornado cria
# um texto e uma caixa no canva passado como parâmetro
def acao_botao(
    canva_atividades, canva_notas, frame, entry1: Entry, entry2: Entry, janela: Toplevel
):

    print(entry1.get(), entry2.get())
    nav = Sigaa(entry1.get(), entry2.get())
    lista_atividades = nav.pega_atividades()
    lista_notas = nav.abre_boletim()

    contador = 0
    for i in lista_notas.keys():
        canva_notas.create_text(
            5,
            10 + contador * 25,
            anchor="nw",
            text=adequa_tamanho_nota(i),
            fill="#F2F2F2",
            font=("Montserrat", 13 * -1),
        )
        canva_notas.create_text(
            170,
            10 + contador * 25,
            anchor="nw",
            text=lista_notas[i],
            fill="#F2F2F2",
            font=("Montserrat", 13 * -1),
        )
        contador += 1
    contador = 0
    for i in lista_atividades.keys():
        round_rectangle(
            0,
            contador * 70,
            550,
            contador * 70 + 65,
            canva_atividades,
            radius=31,
            fill="#1A1A1A",
        )
        # round_rectangle(
        #     0, contador * 60, 550, 65, canva_atividades, radius=31, fill="#1A1A1A"
        # )
        # canva_atividades.create_image(211.0, 32 + 44 * contador, image=bloco)
        canva_atividades.create_text(
            11.0,
            4 + contador * 70.0,
            anchor="nw",
            text=i,
            fill="#F2F2F2",
            font=("Montserrat", 20 * -1),
        )
        canva_atividades.create_text(
            410.0,
            20 + contador * 70.0,
            anchor="nw",
            text=lista_atividades[i],
            fill="#F2F2F2",
            font=("Montserrat", 15 * -1),
        )
        contador += 1
    canva_atividades.pack()
    if contador > 5:
        vbar = Scrollbar(frame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canva_atividades.yview)
        canva_atividades.config(yscrollcommand=vbar.set)
        canva_atividades.pack(side=LEFT, expand=True, fill=BOTH)
        canva_atividades.config(scrollregion=(-1, -1, 529, contador * 45))
    janela.destroy()


window = Tk()

window.geometry("780x520-300+100")
window.configure(bg="#1e1e1e")
window.title("Conect_sigaa")
window2 = Toplevel(window)
window2.geometry("300x350-600+275")
window2.configure(bg="#1E1E1E")
window2.title("Login")
window2.configure(highlightthickness=1, highlightcolor="#8E5AEE")
window2.resizable(False, False)
window2.attributes("-topmost", True)
window2.overrideredirect(True)

texto = Label(
    window2,
    text="Login",
    bg="#1e1e1e",
    fg="#f2f2f2",
    font=("Inter", 64 * -1),
)

instrucao = Label(
    window2,
    text="Forneça as suas credenciais do\nseu cadastro único:",
    bg="#1e1e1e",
    fg="#f2f2f2",
    font=("Inter", 18 * -1),
    height=2,
    width=25,
    justify=LEFT,
)
credenciais = Canvas()


texto.place(x=60, y=11)
instrucao.place(x=17, y=100)
credenciais = Canvas(window2, width=224, height=195, bg="#1E1E1E", highlightthickness=0)
credenciais.place(x=35, y=147)
round_rectangle(
    0.0,
    25.0,
    224.0,
    58.0,
    credenciais,
    radius=10,
    fill="#1A1A1A",
)
round_rectangle(
    0.0,
    63.0,
    224.0,
    96.0,
    credenciais,
    radius=10,
    fill="#1A1A1A",
)
usuario = Entry(
    credenciais,
    bg="#1A1A1A",
    fg="#f2f2f2",
    font=("Inter", 13 * -1),
    width=224,
    highlightthickness=0,
    borderwidth=0,
)
usuario.insert(0, "Usuário")
usuario.place(x=5, y=35)

senha = Entry(
    credenciais,
    bg="#1A1A1A",
    fg="#f2f2f2",
    font=("Inter", 13 * -1),
    width=224,
    highlightthickness=0,
    borderwidth=0,
    show="*",
)
senha.insert(0, "Senha")
senha.place(x=5, y=67)


canvas = Canvas(
    window,
    bg="#1e1e1e",
    height=520,
    width=780,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
Canvas_atividades = Canvas()
Canvas_notas = Canvas()

central = Frame()
direita = Frame()
canvas.place(x=0, y=0)

button_1 = Button(
    window2,
    text="Entrar",
    bg="#1e1e1e",
    fg="#f2f2f2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: acao_botao(
        Canvas_atividades, Canvas_notas, central, usuario, senha, window2
    ),
    relief="flat",
    font=("Inter", 18 * -1),
)
button_1.place(x=124, y=301, width=52, height=22)

central = Frame(window, width=550, height=500, background="#1e1e1e")
central.place(x=9, y=84)

direita = Frame(window, width=210, height=375, background="#1a1a1a")
direita.place(x=570, y=110)

Canvas_atividades = Canvas(
    central,
    bg="#1e1e1e",
    width=550,
    height=420,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
Canvas_atividades.pack(pady=(0, 10))

Canvas_notas = Canvas(
    direita,
    bg="#1a1a1a",
    width=210,
    height=375,
    highlightthickness=0,
    relief="ridge",
)
Canvas_notas.pack()

# canvas.create_rectangle(568.0, -1.0, 785.0, 525.0, fill="#1A1A1A", outline="#8E5AEE")
round_rectangle(
    568.0,
    -1.0,
    785.0,
    525.0,
    canvas,
    radius=31,
    fill="#1A1A1A",
    outline="#8E5AEE",
)

canvas.create_text(
    25.0,
    25.0,
    anchor="nw",
    text="Atividades",
    fill="#8E5AEE",
    font=("Montserrat", 40 * -1),
)

canvas.create_text(
    628.0,
    64.0,
    anchor="nw",
    text="Notas",
    fill="#919191",
    font=("Montserrat", 32 * -1),
)


window.resizable(False, False)
window.mainloop()