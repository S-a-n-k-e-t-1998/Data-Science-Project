#from kivymd.app import MDApp
import tkinter
root=tkinter.Tk()
root.title("BMI Calculator")

#Create function
def calculate_bmi():
    kg= float(entry_kg.get())
    height= float(entry_height.get())
    bmi= round(kg / (height ** 2), 2)
    label_bmi['text'] = f"BMI: {bmi}"
    if bmi <= 25:
        print(" Yor are Fit")
    else:
        print("You are unfit")
#Create GUI
label_kg = tkinter.Label(root,text="KG: ")
label_kg.grid(column=0, row=1)

entry_kg=tkinter.Entry(root)
entry_kg.grid(column=1, row=1)

label_height = tkinter.Label(root, text="HEIGHT: ")
label_height.grid(column=0, row=2)

entry_height=tkinter.Entry(root)
entry_height.grid(column=1, row=2)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=3)

label_bmi = tkinter.Label(root, text="BMI: ")
label_bmi.grid(column=1, row=3)

label_msg = tkinter.Label(root, text="Result: ")
label_msg.grid(column=0, row=4)

label_remark = tkinter.Label(root, text="Welcome to BMI Calculator")
label_remark.grid(column=0, row=0, columnspan=2 )



root.mainloop()