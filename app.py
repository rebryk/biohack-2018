from tkinter import *
from tkinter.filedialog import askopenfilename
import csv
import os
import pandas as pd



class VScrollTable(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

        # here magic happens
        self.canvas = Canvas(root, width=1100, height=1000, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    # and here magic happens even
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #useful functions

    def add_item(self, text, row, column):
        Label(self.frame, text=text).grid(row=row, column=column)

    def reset(self):
        for widget in self.frame.winfo_children():
            widget.grid_forget()
            widget.destroy()

def openFile():
    path = askopenfilename()
    included_cols = ['chrom', 'inputPos', 'inputRef', 'inputAlt', 'varLocation', 'codingEffect', 'varLocation', 'alt_pNomen', 'score']
    #os.system('./run.sh')
    df = pd.read_csv("result.csv")
    df = df[included_cols]
    df.to_csv("result2.csv", sep=',', encoding='utf-8')
    with open("result2.csv", newline = "") as f:
        reader = csv.reader(f)
        table.reset()
        for r, texts in enumerate(reader):
            for c, text in enumerate(texts):
                table.add_item(text, r, c)

if __name__ == '__main__':
    root = Tk()
    root.title("Test")

    btn = Button(root, text="Open file", command=openFile)
    btn.pack()

    table = VScrollTable(root)
    table.pack()

    root.mainloop()
