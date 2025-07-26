



from pathlib import Path
# import Model_Page as mp
# import Home_Page as hp
# import Calculation_Page as cp

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

def exit_app():
    window.destroy()





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\theul\OneDrive\Desktop\Advance Python Course\ML Project (Student Success Predictor)\Code\assets\frame0")


# ASSETS_PATH = Path(r"C:\Users\theul\OneDrive\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Student Success Predictor")
window.geometry("1280x720")
window.configure(bg = "#F6EFE6")


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
    file=relative_to_assets("i1.png"))
image_1 = canvas.create_image(
    74.0,
    403.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
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

image_image_2 = PhotoImage(
    file=relative_to_assets("i2.png"))
image_2 = canvas.create_image(
    328.0,
    116.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("i3.png"))
image_3 = canvas.create_image(
    679.0,
    190.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("i4.png"))
image_4 = canvas.create_image(
    679.0,
    253.0,
    image=image_image_4
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=47.0,
    y=133.0,
    width=54.0,
    height=54.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("i5.png"))
image_5 = canvas.create_image(
    74.0,
    53.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("i6.png"))
image_6 = canvas.create_image(
    995.0,
    507.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("i7.png"))
image_7 = canvas.create_image(
    392.0,
    501.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("i8.png"))
image_8 = canvas.create_image(
    1072.0,
    538.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("i9.png"))
image_9 = canvas.create_image(
    1089.0,
    565.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("i10.png"))
image_10 = canvas.create_image(
    1081.0,
    592.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("i11.png"))
image_11 = canvas.create_image(
    1070.0,
    619.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("i12.png"))
image_12 = canvas.create_image(
    1072.0,
    646.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("i13.png"))
image_13 = canvas.create_image(
    1185.0,
    104.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("i14.png"))
image_14 = canvas.create_image(
    690.0,
    680.0,
    image=image_image_14
)

canvas.create_text(
    524.0,
    666.0,
    anchor="nw",
    text="Accuracy Rate of Model:      91.42 %",
    fill="#F6EFE6",
    font=("Inter Bold", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
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


def model_playing():
    exit_app()
    script_path = 'Model_Page.py'
    globals()['__file__'] = script_path
    exec(open(script_path).read())


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: model_playing(),
    relief="flat"
)
button_4.place(
    x=47.0,
    y=227.0,
    width=54.0,
    height=54.0
)




def calculator_playing():
    exit_app()
    script_path = 'Calculation_Page.py'
    globals()['__file__'] = script_path
    exec(open(script_path).read())



button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
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

image_image_15 = PhotoImage(
    file=relative_to_assets("i15.png"))
image_15 = canvas.create_image(
    32.0,
    162.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("i16.png"))
image_16 = canvas.create_image(
    690.0,
    386.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("i17.png"))
image_17 = canvas.create_image(
    393.0,
    579.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("i18.png"))
image_18 = canvas.create_image(
    688.0,
    383.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("i19.png"))
image_19 = canvas.create_image(
    397.0,
    577.0,
    image=image_image_19
)
window.resizable(False, False)
window.mainloop()










