from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)

label = Label(text="Boyunuzu giriniz (cm):")
label.pack()
boy = Entry(width=10)
boy.pack()

label1 = Label(text="Kilonuzu giriniz (kg):")
label1.pack()
kilo = Entry(width=10)
kilo.pack()

def hesapla():
    boy_val = float(boy.get()) / 100  # Convert height to meters
    kilo_val = float(kilo.get())
    sonuc = kilo_val / boy_val**2
    sonuc_label.config(text=f"BMI: {sonuc:.2f}")

    if sonuc >= 30:
        label8.config(text="Obezsiniz")
    elif 25 <= sonuc < 30:
        label8.config(text="Kilolusunuz")
    elif 18.5 <= sonuc < 25:
        label8.config(text="Kilonuz Normal")
    else:
        label8.config(text="Zayıfsınız!!")

button = Button(text="HESAPLA", command=hesapla)
button.pack()

sonuc_label = Label(text="")
sonuc_label.pack()

label8 = Label(text="")
label8.pack()

window.mainloop()
