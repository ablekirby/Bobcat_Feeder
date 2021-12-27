# Layout Test for Bobcat Feeder
# August 14, 2021
# Able Kirby

import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import ttk as ttk
from bcilib import *



wbg = "#121b3b"
wbg2 = "#786fa6"
wfg2 = "#303952"
wfg = "#f8a5c2"
wfg3 = "#c44569"


myapp = bfAPP()
myapp.appendValue("AbleKirby","02f1962328552371769881a9f49c192c0df261f3e0bdf4cd68a4f6d449cc6fd4ad",100)
#myapp.appendValue("SirSpencer","03ecb3ee55ba6324d40bea174de096dc9134cb35d990235723b37ae9b5c49f4f53",50)
myapp.url = ""
myapp.importJPG("albumart_scaled.jpg")
myapp.link = "https://ablekirby.com/projects.html"
myapp.desc = "Able Kirby misc"

root = tk.Tk()
root.title("Bobcat Feeder v" + verstr)
#root.geometry("380x380")
root.configure(bg=wbg)

bkimg = Image.open("forest_iso1_380.png")
bkpimg = ImageTk.PhotoImage(bkimg)

# Titleblock
lb_title = tk.Label(text="Bobcat Feeder", font=("Ariel Bold",22),bg=wbg,fg=wfg)
lb_title.grid(row=0,column=0,columnspan=8)
lb_ver = tk.Label(text="Version "+verstr,font=("Arial",10),bg=wbg,fg=wfg3,anchor='nw',width=22,height=3)
lb_ver.grid(row=1,column=0,columnspan=3)
lb_flavor = tk.Label(text="BobcatIndex.com", font=("Arial",10),bg=wbg,fg=wfg3,anchor='ne',width=22,height=3,)
lb_flavor.grid(row=1,column=3,columnspan=3)

# Project Block
lb_project = tk.Label(text="Project Name",font=("Arial Bold",12),bg=wbg,fg=wfg3,anchor='w',width=10)
lb_project.grid(row=2,column=0,columnspan=2)
et_project = tk.Entry(width=34,text="test12")
et_project.insert(0,"Example Music Feed 1")
et_project.grid(row=2,column=2,columnspan=4)

lb_url = tk.Label(text="Project URL",font=("Arial Bold",12),bg=wbg,fg=wfg3,anchor='w',width=10)
lb_url.grid(row=3,column=0,columnspan=2)
et_url = tk.Entry(width=34)
et_url.insert(0,"")
et_url.grid(row=3,column=2,columnspan=4)


#ttk.Style().theme_use('default')
ttk.Style().configure('TNotebook.Tab', background="green3")
#ttk.Style().map("TNotebook", background= [("selected", "green3")])

nb = ttk.Notebook(root)

# Track List Panel
f1 = tk.Frame(nb,bg=wbg2)

# Headers
lb_h1 = tk.Label(f1,text='Track',bg=wbg2,fg="#EEEEFF")
lb_h2 = tk.Label(f1,text='Title',bg=wbg2,fg="#EEEEFF")
lb_h3 = tk.Label(f1,text='File',bg=wbg2,fg="#EEEEFF")
lb_h4 = tk.Label(f1,text='Value Key',bg=wbg2,fg="#EEEEFF")
lb_h1.grid(column=0,row=0)
lb_h2.grid(column=1,row=0)
lb_h3.grid(column=2,row=0)
lb_h4.grid(column=3,row=0)

# Column 0
lb_r10 = tk.Label(f1,text='1',bg=wbg2,fg="#EEEEFF")
lb_r20 = tk.Label(f1,text='2',bg=wbg2,fg="#EEEEFF")
lb_r30 = tk.Label(f1,text='3',bg=wbg2,fg="#EEEEFF")
lb_r40 = tk.Label(f1,text='4',bg=wbg2,fg="#EEEEFF")
lb_r50 = tk.Label(f1,text='5',bg=wbg2,fg="#EEEEFF")
lb_r60 = tk.Label(f1,text='6',bg=wbg2,fg="#EEEEFF")
lb_r70 = tk.Label(f1,text='7',bg=wbg2,fg="#EEEEFF")
lb_r10.grid(row=1,column=0)
lb_r20.grid(row=2,column=0)
lb_r30.grid(row=3,column=0)
lb_r40.grid(row=4,column=0)
lb_r50.grid(row=5,column=0)
lb_r60.grid(row=6,column=0)
lb_r70.grid(row=7,column=0)

# Column 1
en_r11 = tk.Entry(f1)
en_r11.insert(0," ")
en_r11.grid(row=1,column=1)
en_r21 = tk.Entry(f1)
en_r21.insert(0," ")
en_r21.grid(row=2,column=1)
en_r31 = tk.Entry(f1)
en_r31.insert(0," ")
en_r31.grid(row=3,column=1)
en_r41 = tk.Entry(f1)
en_r41.insert(0,"")
en_r41.grid(row=4,column=1)
en_r51 = tk.Entry(f1)
en_r51.insert(0,"")
en_r51.grid(row=5,column=1)
en_r61 = tk.Entry(f1)
en_r61.insert(0,"")
en_r61.grid(row=6,column=1)
en_r71 = tk.Entry(f1)
en_r71.insert(0,"")
en_r71.grid(row=7,column=1)

# Column 2
en_r12 = tk.Entry(f1)
en_r12.insert(0,"")
en_r12.grid(row=1,column=2)
en_r22 = tk.Entry(f1)
en_r22.insert(0,"")
en_r22.grid(row=2,column=2)
en_r32 = tk.Entry(f1)
en_r32.insert(0,"")
en_r32.grid(row=3,column=2)
en_r42 = tk.Entry(f1)
en_r42.insert(0," ")
en_r42.grid(row=4,column=2)
en_r52 = tk.Entry(f1)
en_r52.insert(0," ")
en_r52.grid(row=5,column=2)
en_r62 = tk.Entry(f1)
en_r62.insert(0," ")
en_r62.grid(row=6,column=2)
en_r72 = tk.Entry(f1)
en_r72.insert(0," ")
en_r72.grid(row=7,column=2)

lb_t1 = tk.Label(f1,text=1)
#lb_t1_name 

f2 = ttk.Frame(nb)
f3 = ttk.Frame(nb)

nb.add(f1, text='Track Listing')
nb.add(f2, text='Meta Data')
nb.add(f3, text='Options')
nb.grid(row=4,column=0,columnspan=8)


lb_bk = tk.Label(image=bkpimg,borderwidth=0)
lb_bk.grid(row=10,column=0,columnspan=8)

def bimport_press():
    filetypes = (
        ('MP3 files', '*.mp3'),
        ('All files', '*.*')
    )

    fns = fd.askopenfilenames(title="choose MP3 files", filetypes=filetypes)
    songno = 0
    for fn in fns:
        myapp.importMP3(fn)
        en_r11.insert(0,myapp.songs[0].title)
        en_r12.insert(0,myapp.songs[0].fn)
        print(fn + " has been imported") 
    print("done.")
    

    # Update GUI
    et_project.delete(0,'end')
    et_project.insert(0,myapp.getProjectName())

    


bimport = tk.Button(text="Import Files...",height=2,width=20,bg=wfg3,command=bimport_press)
bimport.grid(row=6,column=1,pady=15)


def bwrite_press():
    print("Writing XML to disk...")
    myapp.writeXML()
    print("done.")

bwrite = tk.Button(text="Rock n' Roll!",height=2,width=20,bg=wfg, command=bwrite_press)
bwrite.grid(row=6,column=5,pady=15)

root.mainloop()


