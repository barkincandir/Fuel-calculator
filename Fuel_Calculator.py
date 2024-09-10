import tkinter as tk
from tkinter import ttk

def hesapla():
    mesafe = float(mesafe_entry.get())
    yak = float(yak_entry.get())
    yak_fiyat = float(yak_fiyat_entry.get())
    yon = str(yon_combobox.get())

    if yon == "One way":
        aky = (mesafe * yak) / 100
    elif yon == "Two way":
        aky = ((mesafe * yak) / 100) * 2

    fiyat = aky * yak_fiyat

    sonuc_label.config(text=f"Used fuel: {aky} lt\n"
                           f"Price:{fiyat} TL.")


root = tk.Tk()
root.title("Fuel Calculator")
root.geometry("800x300")

mesafe_label = tk.Label(root, text="Distance(km):")
mesafe_label.pack()
mesafe_entry = tk.Entry(root)
mesafe_entry.pack()

yak_label = tk.Label(root, text="Fuel consumption per 100 km:")
yak_label.pack()
yak_entry = tk.Entry(root)
yak_entry.pack()

yak_fiyat_label = tk.Label(root, text="Fuel cost:")
yak_fiyat_label.pack()
yak_fiyat_entry = tk.Entry(root)
yak_fiyat_entry.pack()

yon_label = tk.Label(root, text="Way:")
yon_label.pack()
yon_combobox = tk.ttk.Combobox(root, values=["One way", "Two way"])
yon_combobox.pack()

hesapla_button = tk.Button(root, text="Calculate", command=hesapla)
hesapla_button.pack()

sonuc_label = tk.Label(root, text="")
sonuc_label.pack()

root.mainloop()
