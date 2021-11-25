import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter.messagebox import *

class Text(tk.Frame):
    def __init__(self, parent=None, file=None):
        tk.Frame.__init__(self, parent)
        self.frm = tk.Frame(parent)
        self.frm.pack(fill=tk.X)
        self.layoutKolom = tk.Frame(root)
        parent.title("Text Editor")
        self.buatNamaFile()
        self.buatTombol()
        self.kolomTeksUtama()
        self.indeks = 1.0
        self.path = ''
    
    def buatTombol(self):
        tk.Button(self.frm, text='Open', relief='groove', command=self.openFile).pack(side=tk.LEFT)
        tk.Button(self.frm, text='Save', relief='groove', command=self.perintahSimpan).pack(side=tk.LEFT)
        tk.Button(self.frm, text='Exit', relief='groove', command=self.perintahKeluar).pack(side=tk.LEFT)
    
    def kolomTeksUtama(self):
        scroll = tk.Scrollbar(self)
        kolomTeks = tk.Text(self, relief=tk.GROOVE)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        kolomTeks.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=tk.YES, fill=tk.BOTH)
    
    def perintahSimpan(self):
        print(self.path)
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'file telah disimpan')
        else:
            tipeFile = [('Text File', '*.txt'), ('Python file', '*.py'),('All files','.*')]
            filename = asksaveasfilename(filetypes=(tipeFile))
            if filename:
                alltext = self.gettext()
                open(filename, 'w').write(alltext)
                self.path = filename
    
    def perintahKeluar(self):
        ans = askokcancel('Exit', 'Anda yakin mau keluar?')
        if ans:
            tk.Frame.quit(self)
    
    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.kolomTeks.delete('1.0', tk.END)
        self.kolomTeks.insert('1.0', text)
        self.kolomTeks.mark_set(tk.INSERT, '1.0')
        self.kolomTeks.focus()
    
    def gettext(self):
        return self.kolomTeks.get('1.0', tk.END+'-1c')
    
    def buatNamaFile(self):
        self.layoutKolom.pack(fill=tk.BOTH, expand=1, padx=17, pady=5)

    def openFile(self):
        ekstensiFile = [('All files', '*.*'), ('Text Files', '*.txt'), ('Python files', '*.py')]
        open = filedialog.askopenfilename(filetypes = ekstensiFile)
        if open != '':
            text = self.readFile(open)
            if text:
                self.path = open
                self.kolomTeks.delete('0.1', tk.END)
                self.kolomTeks.insert(tk.END, text)

    def readFile(self, filename):
        try:
            f = open(filename, 'r')
            text = f.read()
            return text
        except:
            messagebox.showerror('Error!')
            return None

root = tk.Tk()
Text(root)
tk.mainloop()
