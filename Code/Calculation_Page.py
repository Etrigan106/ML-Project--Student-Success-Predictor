import Main_in_Python as n
import numpy as np
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

def exit_app():
    window.destroy()




x = [[]]
answer = 0


ASSETS_PATH = Path(r"C:\Users\theul\OneDrive\Desktop\Advance Python Course\ML Project (Student Success Predictor)\Code\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# Defining Window

window = Tk()

window.title("Student Success Predictor")

window.geometry("1280x720")
window.configure(bg = "#F6EFE6")






def Equation(x):
    
    #intercept
    b=n.M.intercept_
    # coefficient
    m=n.M.coef_

    print(m)
    print(x)
    mx=m*x
    mx=mx.sum()
    y=mx+b

    #predicting y using model (algorithm)
    y1=n.M.predict(x)
    y1=float(y1)
    y1
    print (y)
    print (y1)
    answer = y1

    return answer


def Prediction():

    
    
    x = np.array([[
        float(entry_1.get()),
        float(entry_2.get()),
        float(entry_3.get()),
        float(entry_4.get()),
        float(entry_5.get()),
        float(entry_6.get()),
        float(entry_7.get()),
        float(entry_8.get())
    ]])
    print(x)
    x = x.astype(float)
    print ('Execution Button Clicked')

    answer = Equation(x)
    answer = f'%.{3}f' %answer

    canvas.delete(answer_text_id)

    canvas.create_text(
    774.0,
    599.0,
    anchor="nw",
    text=f"{answer}",
    fill="#F6EFE6",
    font=("Inter Bold", 24 * -1, 'bold')
    )   


def exit_app():
    window.destroy()



# UI
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
    file=relative_to_assets("image_1.png"))
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

canvas.create_text(
    194.0,
    94.0,
    anchor="nw",
    text="PREDICTION CALCULATOR",
    fill="#000000",
    font=("Inter Bold", 36 * -1,"bold")
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    707.0,
    378.0,
    image=image_image_2
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    74.0,
    53.0,
    image=image_image_3
)



# About Button
about_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
About_Button = Button(
    image=about_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
About_Button.place(
    x=1220.0,
    y=666.0,
    width=30.0,
    height=30.0
)



# Input Boxes

# Row 1
# Entry Box 1
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    326.5,
    314.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=241.0,
    y=293.0,
    width=171.0,
    height=37.0
)


# Entry Box 2
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    578.5,
    314.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=493.0,
    y=293.0,
    width=171.0,
    height=37.0
)


# Entry Box 3
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    830.5,
    314.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=745.0,
    y=293.0,
    width=171.0,
    height=37.0
)


# Entry Box 4
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1082.5,
    314.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=997.0,
    y=293.0,
    width=171.0,
    height=37.0
)



# Row 2
# Entry Box 5
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    326.5,
    455.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=241.0,
    y=434.0,
    width=171.0,
    height=37.0
)


# Entry Box 6
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    578.5,
    455.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=493.0,
    y=434.0,
    width=171.0,
    height=37.0
)


# Entry Box 7
entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    830.5,
    455.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=745.0,
    y=434.0,
    width=171.0,
    height=37.0
)


# Entry Box 8
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    1082.5,
    455.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=997.0,
    y=434.0,
    width=171.0,
    height=37.0
)


def home_playing():
    exit_app()
    script_path = 'Home_Page.py'
    globals()['__file__'] = script_path
    exec(open(script_path).read())


# Home Button
Home_button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
Home_Button = Button(
    image=Home_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: home_playing(),
    relief="flat"
)
Home_Button.place(
    x=47.0,
    y=133.0,
    width=54.0,
    height=54.0
)





# Header 
canvas.create_text(
    194.0,
    94.0,
    anchor="nw",
    text="PREDICTION CALCULATOR",
    fill="#000000",
    font=("Inter Bold", 36 * -1,"bold")
)
canvas.create_text(
    194.0,
    160.0,
    anchor="nw",
    text="Enter the asked data of the student to get the prediction of his/her expected performance in academics. ",
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)


# Entry Box Texts
canvas.create_text(
    235.0,
    266.0,
    anchor="nw",
    text="Studied Hours",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    989.0,
    266.0,
    anchor="nw",
    text="Previous Score",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    488.0,
    266.0,
    anchor="nw",
    text="Sleep Hours",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    741.0,
    266.0,
    anchor="nw",
    text="Practiced Questions",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    741.0,
    407.0,
    anchor="nw",
    text="Writing Score",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    989.0,
    407.0,
    anchor="nw",
    text="Extra Activities(1/0)",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    235.0,
    407.0,
    anchor="nw",
    text="Math score",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)

canvas.create_text(
    488.0,
    407.0,
    anchor="nw",
    text="Reading Score",
    fill="#000000",
    font=("Inter Bold", 15 * -1, "bold")
)


# UI Elements
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1185.0,
    92.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    683.0,
    618.0,
    image=image_image_5
)



# Answer Text
canvas.create_text(
    468.0,
    599.0,
    anchor="nw",
    text="Predicted Performance :",
    fill="#F6EFE6",
    font=("Inter Bold", 24 * -1, 'bold')
)

answer_text_id = canvas.create_text(
    774.0,
    599.0,
    anchor="nw",
    text=f"{answer}",
    fill="#F6EFE6",
    font=("Inter Bold", 24 * -1, 'bold')
)


# Exit Button
Exit_button_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
Exit_Button = Button(
    image=Exit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit_app(),
    relief="flat"
)
Exit_Button.place(
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


# Model Button
Model_button_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
Model_Button = Button(
    image=Model_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:  model_playing()
    ,
    relief="flat"
)
Model_Button.place(
    x=47.0,
    y=227.0,
    width=54.0,
    height=54.0
)


Predictor_button_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
Predictor_Button = Button(
    image=Predictor_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
Predictor_Button.place(
    x=47.0,
    y=321.0,
    width=54.0,
    height=54.0
)


# Execution Button
Executor_button_image = PhotoImage(
    file=relative_to_assets("Prediction_Executor.png"))
Executor_Button = Button(
    image=Executor_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Prediction(),
    relief="flat"
)
Executor_Button.place(
    x=1075.0,
    y=546.0,
    width=114.0,
    height=25.0
)

label = Label(
    window,
    text="Predict",       
    font=("Inter Bold", 10),    
    fg="#F6EFE6",         
    bg="#1A332F"             
)
label.place(
    x=1108.0,              
    y=547.0                
)



image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    32.0,
    348.0,
    image=image_image_6
)


window.resizable(False, False)
window.mainloop()

