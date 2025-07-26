
from pathlib import Path


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\theul\OneDrive\Desktop\Advance Python Course\ML Project (Student Success Predictor)\Code\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Student Success Predictor")

window.geometry("1280x720")
window.configure(bg = "#F6EFE6")

def exit_app():
    window.destroy()

canvas = Canvas(
    window,
    bg = "#F6EFE6",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("1.png"))
image_1 = canvas.create_image(
    74.0,
    403.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("b1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1220.0,
    y=666.0,
    width=30.0,
    height=30.0
)

canvas.create_text(
    194.0,
    94.0,
    anchor="nw",
    text="TRAINED MODEL DETAILS",
    fill="#000000",
    font=("Inter Bold", 36 * -1, "bold")
)

image_image_2 = PhotoImage(
    file=relative_to_assets("2.png"))
image_2 = canvas.create_image(
    428.0,
    507.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("3.png"))
image_3 = canvas.create_image(
    971.0,
    506.0,
    image=image_image_3
)


def home_playing():
    exit_app()
    script_path = 'Home_Page.py'
    globals()['__file__'] = script_path
    exec(open(script_path).read())


button_image_2 = PhotoImage(
    file=relative_to_assets("b2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: home_playing(),
    relief="flat"
)
button_2.place(
    x=47.0,
    y=133.0,
    width=54.0,
    height=54.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("4.png"))
image_4 = canvas.create_image(
    74.0,
    53.0,
    image=image_image_4
)

canvas.create_text(
    219.0,
    321.0,
    anchor="nw",
    text="Actual vs Predicted Result",
    fill="#000000",
    font=("Inter Bold", 15 * -1,"bold")
)

canvas.create_text(
    760.0,
    321.0,
    anchor="nw",
    text="Heat Map",
    fill="#000000",
    font=("Inter Bold", 15 * -1,"bold")
)

canvas.create_text(
    194.0,
    160.0,
    anchor="nw",
    text="The Model was trained using ML and was given a data of 1000 entries, 80 percent of the data was used to train the model \nand 20 percent of it was used to test it. ",
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("5.png"))
image_5 = canvas.create_image(
    1185.0,
    143.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("6.png"))
image_6 = canvas.create_image(
    691.0,
    261.0,
    image=image_image_6
)

canvas.create_text(
    476.0,
    242.0,
    anchor="nw",
    text="Accuracy Rate of Model:      91.42 %",
    fill="#F6EFE6",
    font=("Inter Bold", 24 * -1, "bold")
)

button_image_3 = PhotoImage(
    file=relative_to_assets("b3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit_app(),
    relief="flat"
)
button_3.place(
    x=59.0,
    y=635.0,
    width=40.0,
    height=40.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("b4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=47.0,
    y=227.0,
    width=54.0,
    height=54.0
)



def calculator_playing():
    # exit_app()
    script_path = 'Calculation_Page.py'
    globals()['__file__'] = script_path
    exec(open(script_path).read())




button_image_5 = PhotoImage(
    file=relative_to_assets("b5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calculator_playing(),
   
    relief="flat"
)
button_5.place(
    x=47.0,
    y=321.0,
    width=54.0,
    height=54.0
)







image_image_7 = PhotoImage(
    file=relative_to_assets("7.png"))
image_7 = canvas.create_image(
    32.0,
    255.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("8.png"))
image_8 = canvas.create_image(
    425.0,
    508.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("9.png"))
image_9 = canvas.create_image(
    969.0,
    505.0,
    image=image_image_9
)
window.resizable(False, False)
window.mainloop()

