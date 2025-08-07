from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, messagebox, Label, Frame, BooleanVar, Toplevel
import ctypes
import sys
import webbrowser
import subprocess

#Assat Linking---------------------------------------------------------------------------------------------------------------------------------------
if getattr(sys, 'frozen', False):
    # Wenn als EXE gepackt
    BASE_PATH = Path(sys._MEIPASS)
else:
    BASE_PATH = Path(__file__).parent

ASSETS_PATH = BASE_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Window Generation-----------------------------------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("1358x764")
window.configure(bg = "#1E1E1E")
window.overrideredirect(True)
window.title("Windows App Installer")
titlebar = Frame(window, bg="#232323", relief='raised', bd=0, highlightthickness=0)
titlebar.place(x=0, y=0, width=1358, height=32)
title_label = Label(titlebar, text="Windows App Installer", bg="#232323", fg="#ffffff", font=("Segoe UI", 10))
title_label.place(x=10, y=6)
def start_move(event):
    window.x_offset = event.x
    window.y_offset = event.y
def move_window(event):
    x = event.x_root - window.x_offset
    y = event.y_root - window.y_offset
    window.geometry(f'+{x}+{y}')
canvas = Canvas(window, bg = "#1E1E1E", height = 764, width = 1358, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 32)

#Variables-------------------------------------------------------------------------------------------------------------------------------------------
mode = "None"
cmdline_input = ""
silent_admin_var = BooleanVar()
adminchek = False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#Window Controls-------------------------------------------------------------------------------------------------------------------------------------
close_btn = Button(titlebar, text="✕", bg="#232323", fg="#ffffff", borderwidth=0,command=lambda: close_window(), activebackground="#ff5555", activeforeground="#fff")
close_btn.place(x=1320, y=0, width=38, height=32)
min_btn = Button(titlebar, text="━", bg="#232323", fg="#ffffff", borderwidth=0, command=lambda: minimize_window(), activebackground="#444", activeforeground="#fff")
min_btn.place(x=1282, y=0, width=38, height=32)

def minimize_window():
    window.overrideredirect(False)
    window.iconify()
    
def restore_window(event=None):
    if window.state() == "normal":
        window.overrideredirect(True)
        window.iconbitmap(relative_to_assets("appicon.ico"))
    
window.bind("<Map>", restore_window)
    
def close_window():
    window.destroy()
    
#Admin Check Function--------------------------------------------------------------------------------------------------------------------------------
silent_install_var = BooleanVar(value=False)
admin_prompted = [False]

def ask_for_admin(*args):
    if silent_install_var.get() and not admin_prompted[0]:
        admin_prompted[0] = True
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False
        if not is_admin:
            # Programm mit Adminrechten neu starten
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            window.destroy()
            silent_checkbox.select()
            
silent_install_var.trace_add("write", ask_for_admin)

#Window Content--------------------------------------------------------------------------------------------------------------------------------------
image_image_1 = PhotoImage(file=relative_to_assets("bg.png"))
cmdline_img = PhotoImage(file=relative_to_assets("entry_1.png"))
output_img = PhotoImage(file=relative_to_assets("entry_2.png"))
tutorialbutton_img = PhotoImage(file=relative_to_assets("tutorialbtn.png"))
infobutton_img = PhotoImage(file=relative_to_assets("infobtn.png"))
setpath_img = PhotoImage(file=relative_to_assets("cmdline.png"))
listswitch_img = PhotoImage(file=relative_to_assets("listswitchbtn.png"))
listswitchactive_img = PhotoImage(file=relative_to_assets("listswitchbtnactive.png"))
singleswitch_img = PhotoImage(file=relative_to_assets("singleswitchbtn.png"))
singleswitchactive_img = PhotoImage(file=relative_to_assets("singleswitchbtnacrive.png"))
updateactive_img = PhotoImage(file=relative_to_assets("updateactive.png"))
listsearch_img = PhotoImage(file=relative_to_assets("listsearchbtn.png"))
listinstall_img = PhotoImage(file=relative_to_assets("listinstallbtn.png"))
singlesearch_img = PhotoImage(file=relative_to_assets("singlesearchbtn.png"))
singleinstall_img = PhotoImage(file=relative_to_assets("singleinstallbtn.png"))
updateblebtn_img = PhotoImage(file=relative_to_assets("Updateblebtn.png"))
update_allbtn_img = PhotoImage(file=relative_to_assets("Update_allbtn.png"))
installedbtn_img = PhotoImage(file=relative_to_assets("Installedbtn.png"))
updatebtn_img = PhotoImage(file=relative_to_assets("Updatebtn.png"))
activedot_img = PhotoImage(file=relative_to_assets("activedot.png"))
infoscreen_img = PhotoImage(file=relative_to_assets("infobg.png"))
backbtn_img = PhotoImage(file=relative_to_assets("backbtn.png"))
Followbtn_GitHub_img = PhotoImage(file=relative_to_assets("GitHubButton.png"))
Followbtn_Youtube_img = PhotoImage(file=relative_to_assets("YouTubeButton.png"))
Followbtn_Kofi_img = PhotoImage(file=relative_to_assets("KofiButton.png"))
Tutorialbg1_img = PhotoImage(file=relative_to_assets("Tutorialbg1.png"))
Tutorialbg2_img = PhotoImage(file=relative_to_assets("Tutorialbg2.png"))
Tutorialbg3_img = PhotoImage(file=relative_to_assets("Tutorialbg3.png"))
Tutorialbg4_img = PhotoImage(file=relative_to_assets("Tutorialbg4.png"))
Tutorialbg5_img = PhotoImage(file=relative_to_assets("Tutorialbg5.png"))
Tutorialbg6_img = PhotoImage(file=relative_to_assets("Tutorialbg6.png"))
Tutorialbg7_img = PhotoImage(file=relative_to_assets("Tutorialbg7.png"))
TutorialBackButton_img = PhotoImage(file=relative_to_assets("TutorialBackButton.png"))
TutorialForwardButton_img = PhotoImage(file=relative_to_assets("TutorialForwardButton.png"))
TutorialBackButtonDisabled_img = PhotoImage(file=relative_to_assets("TutorialBackButtonDisabeld.png"))
TutorialForwardButtonDisabled_img = PhotoImage(file=relative_to_assets("TutorialForwardButtonDisabeld.png"))

silent_checkbox = Checkbutton(window, text="Silent Install", variable=silent_install_var, bg="#2c2c2c", fg="#ffffff", font=("Segoe UI", 12), activebackground="#2c2c2c", activeforeground="#ffffff", selectcolor="#2c2c2c")
cmdline_func = Entry(window, bd=0, bg="#000000", fg="#ffffff", highlightthickness=0)
output_func = Text(window, bd=0, bg="#000000", fg="#ffffff", highlightthickness=0, state='disabled')
tutorialbutton = Button(window, image=tutorialbutton_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: tutorialbtn(), relief="flat")
infobutton = Button(window, image=infobutton_img, borderwidth=0, highlightthickness=0, background="#1e1e1e", activebackground="#1e1e1e", command=lambda: infobtn(), relief="flat")
setpath = Button(window, image=setpath_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: setpathbtn(), relief="flat")
listswitch = Button(window, image=listswitch_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: listswitchbtn(), relief="flat")
singleswitch = Button(window, image=singleswitch_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: singleswitchbtn(), relief="flat")
listsearch = Button(window, image=listsearch_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: listsearchbtn(), relief="flat")
listinstall = Button(window, image=listinstall_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: listinstallbtn(), relief="flat")
singlesearch = Button(window, image=singlesearch_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: singlesearchbtn(), relief="flat")
singleinstall = Button(window, image=singleinstall_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: singleinstallbtn(), relief="flat")
updateble = Button(window, image=updateblebtn_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: listupdateble(), relief="flat")
update_all = Button(window, image=update_allbtn_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: update_all_func(), relief="flat")
installed = Button(window, image=installedbtn_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: listinstalled(), relief="flat")
update = Button(window, image=updatebtn_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: updatespecific(), relief="flat")
backbutton = Button(window, image=backbtn_img, borderwidth=0, highlightthickness=0, background="#1e1e1e", activebackground="#1e1e1e", command=lambda: backbtn(), relief="flat")
Followbtn_GitHub = Button(window, image=Followbtn_GitHub_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: Followbtn_Github(), relief="flat")
Followbtn_YouTube = Button(window, image=Followbtn_Youtube_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: Followbtn_YouTube_func(), relief="flat")
Followbtn_Kofi = Button(window, image=Followbtn_Kofi_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: Followbtn_Kofi_func(), relief="flat")
TutorialBackButton = Button(window, image=TutorialBackButton_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: TutorialBackbtn(), relief="flat")
TutorialForwardButton = Button(window, image=TutorialForwardButton_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: TutorialForwardbtn(), relief="flat")
TutorialBackButtonDisabled = Button(window, image=TutorialBackButtonDisabled_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: print("Nothing happend"), relief="flat")
TutorialForwardButtonDisabled = Button(window, image=TutorialForwardButtonDisabled_img, borderwidth=0, highlightthickness=0, background="#2c2c2c", activebackground="#2c2c2c", command=lambda: print("Nothing Happend"), relief="flat")

window.bind("<Return>", lambda event: setpathbtn())

image_1 = canvas.create_image(679.0, 382.0, image=image_image_1)
cmdline = canvas.create_image(547.5, 260.0, image=cmdline_img)
output = canvas.create_image(547.5, 532.5, image=output_img)
cmdline_func.place(x=146.0, y=268.0, width=803.0, height=46.0)
output_func.place(x=146.0, y=414.0, width=803.0, height=299.0)
silent_checkbox.place(x=126.0, y=328.0)
tutorialbutton.place(x=130.0, y=191.0, width=155.0, height=36.0)
infobutton.place(x=1284.0, y=47.0, width=50.0, height=50.0)
setpath.place(x=924.0, y=268.0, width=161.0, height=48.0)
listswitch.place(x=976.0, y=414.0, width=155.0, height=36.0)
singleswitch.place(x=976.0, y=576.0, width=155.0, height=36.0)
listsearch.place(x=1038.0, y=468.0, width=155.0, height=36.0)
listinstall.place(x=1038.0, y=522.0, width=155.0, height=36.0)
singlesearch.place(x=1042.0, y=630.0, width=155.0, height=36.0)
singleinstall.place(x=1042.0, y=684.0, width=155.0, height=36.0)
update.place(x=769.0, y=224.0, width=155.0, height=36.0)
installed.place(x=769.0, y=179.0, width=155.0, height=36.0)
update_all.place(x=576.0, y=224.0, width=179.0, height=36.0)
updateble.place(x=576.0, y=179.0, width=179.0, height=36.0)
Followbtn_GitHub.place(x=1157.0, y=643.0, width=88.0, height=88.0)
Followbtn_YouTube.place(x=1015.0, y=648.0, width=118.0, height=81.0)
Followbtn_Kofi.place(x=903.0, y=643.0, width=88.0, height=88.0)
activedot_listsearch = canvas.create_image(1016.0, 453.0, image=activedot_img)
activedot_listinstall = canvas.create_image(1016.0, 507.0, image=activedot_img)
activedot_singlesearch = canvas.create_image(1016.0, 615.0, image=activedot_img)
activedot_singleinstall = canvas.create_image(1016.0, 669.0, image=activedot_img)
Tutorialbg1 = canvas.create_image(679.0, 382.0, image=Tutorialbg1_img)
Tutorialbg2 = canvas.create_image(679.0, 382.0, image=Tutorialbg2_img)
Tutorialbg3 = canvas.create_image(679.0, 382.0, image=Tutorialbg3_img)
Tutorialbg4 = canvas.create_image(679.0, 382.0, image=Tutorialbg4_img)
Tutorialbg5 = canvas.create_image(679.0, 382.0, image=Tutorialbg5_img)
Tutorialbg6 = canvas.create_image(679.0, 382.0, image=Tutorialbg6_img)
Tutorialbg7 = canvas.create_image(679.0, 382.0, image=Tutorialbg7_img)
TutorialBackButton.place(x=607.0, y=621.0, width=50.0, height=50.0)
TutorialForwardButton.place(x=657.0, y=621.0, width=50.0, height=50.0)
TutorialBackButtonDisabled.place(x=607.0, y=621.0, width=50.0, height=50.0)
TutorialForwardButtonDisabled.place(x=657.0, y=621.0, width=50.0, height=50.0)
backbutton.place(x=1284.0, y=48.0, width=50.0, height=50.0)
infogb = canvas.create_image(679.0, 382.0, image=infoscreen_img)

canvas.itemconfig(infogb, state="hidden")
backbutton.place_forget()
Followbtn_GitHub.place_forget()
Followbtn_YouTube.place_forget()
Followbtn_Kofi.place_forget()
canvas.itemconfig(activedot_listsearch, state="hidden")
canvas.itemconfig(activedot_listinstall, state="hidden")
canvas.itemconfig(activedot_singlesearch, state="hidden")
canvas.itemconfig(activedot_singleinstall, state="hidden")
canvas.itemconfig(Tutorialbg1, state="hidden")
canvas.itemconfig(Tutorialbg2, state="hidden")
canvas.itemconfig(Tutorialbg3, state="hidden")
canvas.itemconfig(Tutorialbg4, state="hidden")
canvas.itemconfig(Tutorialbg5, state="hidden")
canvas.itemconfig(Tutorialbg6, state="hidden")
canvas.itemconfig(Tutorialbg7, state="hidden")
TutorialBackButton.place_forget()
TutorialForwardButton.place_forget()
TutorialBackButtonDisabled.place_forget()
TutorialForwardButtonDisabled.place_forget()

#Functions-------------------------------------------------------------------------------------------------------------------------------------------
def listinstalled():
    print("List Installed Button clicked")
    try:
        result = subprocess.run("winget list", shell=True, capture_output=True, text=True)
        output_func.config(state='normal')
        output_func.delete("1.0", "end")
        output_func.insert("1.0", result.stdout if result.stdout else result.stderr)
        output_func.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Fehler beim Abrufen der installierten Programme: {e}")
        
def listupdateble():
    print("List Updateable Button clicked")
    try:
        result = subprocess.run("winget ls --upgrade-available", shell=True, capture_output=True, text=True)
        output_func.config(state='normal')
        output_func.delete("1.0", "end")
        output_func.insert("1.0", result.stdout if result.stdout else result.stderr)
        output_func.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Fehler beim Abrufen der aktualisierbaren Programme: {e}")
        
def update_all_func():
    print("Update All Button clicked")
    try:
        result = subprocess.run("winget upgrade --all", shell=True, capture_output=True, text=True)
        output_func.config(state='normal')
        output_func.delete("1.0", "end")
        output_func.insert("1.0", result.stdout if result.stdout else result.stderr)
        output_func.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Fehler beim Aktualisieren aller Programme: {e}")

def setpathbtn():
    global cmdline_input
    global adminchek
    cmdline_input = cmdline_func.get()
    
    #--------------------------------------------
    
    output = ""
    
    if cmdline_input == "/exit":
        window.destroy()
    elif mode == "None":
        messagebox.showerror("Error", "Please select a mode (List, Single or Update) before executing.")
    elif cmdline_input == "":
        messagebox.showerror("Error", "Please enter a Package or enter a filepath.")
    elif mode == "Listsearch" and not cmdline_input == "":
        try:
            with open(cmdline_input, 'r') as file:
                for line in file:
                    result = subprocess.run("winget search " + line.strip(), shell=True, capture_output=True, text=True)
                    output += result.stdout if result.stdout else result.stderr
        except Exception as e:
            output += f"Fehler: {e}"
    elif mode == "Listinstall" and not cmdline_input == "":
        try:
            with open(cmdline_input, 'r') as file:
                for line in file:
                    result = subprocess.run("winget install " + line.strip(), shell=True, capture_output=True, text=True)
                    output += result.stdout if result.stdout else result.stderr
        except Exception as e:
            output += f"Fehler: {e}"
    elif mode == "Singlesearch" and not cmdline_input == "":
        try:
            result = subprocess.run("winget search " + cmdline_input, shell=True, capture_output=True, text=True)
            output += result.stdout if result.stdout else result.stderr
        except Exception as e:
            output += f"Fehler: {e}"
    elif mode == "Singleinstall" and not cmdline_input == "":
        try:
            result = subprocess.run("winget install " + cmdline_input, shell=True, capture_output=True, text=True)
            output += result.stdout if result.stdout else result.stderr
        except Exception as e:
            output += f"Fehler: {e}"
    elif mode == "Update" and not cmdline_input == "":
        try:
            result = subprocess.run("winget update " + cmdline_input, shell=True, capture_output=True, text=True)
            output += result.stdout if result.stdout else result.stderr
        except Exception as e:
            output += f"Fehler: {e}"
    
    output_func.config(state='normal')
    output_func.delete("1.0", "end")
    output_func.insert("1.0", output)
    output_func.config(state='disabled')
    
#Button Functions for List and Single Mode

def listswitchbtn():
    print("List Switch Button clicked")
    listswitch.config(image=listswitchactive_img)
    singleswitch.config(image=singleswitch_img)
    update.config(image=updatebtn_img)
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="hidden")
    
def singleswitchbtn():
    print("Single Switch Button clicked")
    singleswitch.config(image=singleswitchactive_img)
    listswitch.config(image=listswitch_img)
    update.config(image=updatebtn_img)
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="hidden")    
    
def listsearchbtn():
    print("List Search Button clicked")
    canvas.itemconfig(activedot_listsearch, state="normal")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="hidden")
    listswitch.config(image=listswitchactive_img)
    update.config(image=updatebtn_img)
    singleswitch.config(image=singleswitch_img)
    global mode
    mode = "Listsearch"
    
def listinstallbtn():
    print("List Install Button clicked")
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="normal")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="hidden")
    listswitch.config(image=listswitchactive_img)
    update.config(image=updatebtn_img)
    singleswitch.config(image=singleswitch_img)
    global mode
    mode = "Listinstall"

def singlesearchbtn():
    print("Single Search Button clicked")
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="normal")
    canvas.itemconfig(activedot_singleinstall, state="hidden")
    singleswitch.config(image=singleswitchactive_img)
    update.config(image=updatebtn_img)
    listswitch.config(image=listswitch_img)
    global mode
    mode = "Singlesearch"
    
def singleinstallbtn():
    print("Single Install Button clicked")
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="normal")
    singleswitch.config(image=singleswitchactive_img)
    update.config(image=updatebtn_img)
    listswitch.config(image=listswitch_img)
    global mode
    mode = "Singleinstall"
    
def updatespecific():
    print("Update Specific Button clicked")
    listswitch.config(image=listswitch_img)
    singleswitch.config(image=singleswitch_img)
    update.config(image=updateactive_img)
    canvas.itemconfig(activedot_listsearch, state="hidden")
    canvas.itemconfig(activedot_listinstall, state="hidden")
    canvas.itemconfig(activedot_singlesearch, state="hidden")
    canvas.itemconfig(activedot_singleinstall, state="hidden")
    global mode
    mode = "Update"
    
#Turotial Button Functions
    
def tutorialbtn():
    print("Tutorial Button clicked")
    global TutorialPage
    
    TutorialPage = 1
    
    canvas.itemconfig(image_1, state="hidden")
    canvas.itemconfig(cmdline, state="hidden")
    canvas.itemconfig(output, state="hidden")
    cmdline_func.place_forget()
    output_func.place_forget()
    
    listswitch.place_forget()
    singleswitch.place_forget()
    listsearch.place_forget()
    listinstall.place_forget()
    singlesearch.place_forget()
    singleinstall.place_forget()
    setpath.place_forget()
    tutorialbutton.place_forget()
    silent_checkbox.place_forget()
    update.place_forget()
    installed.place_forget()
    update_all.place_forget()
    updateble.place_forget()
    
    #---------------------------------------------
    
    backbutton.place(x=1284.0, y=48.0, width=50.0, height=50.0)
    TutorialForwardButton.place(x=657.0, y=621.0, width=50.0, height=50.0)
    TutorialBackButtonDisabled.place(x=607.0, y=621.0, width=50.0, height=50.0)
    canvas.itemconfig(Tutorialbg1, state="normal")
    
def TutorialBackbtn():
    print("Tutorial Back Button clicked")
    global TutorialPage
    
    if TutorialPage == 2:
        canvas.itemconfig(Tutorialbg2, state="hidden")
        canvas.itemconfig(Tutorialbg1, state="normal")
        TutorialBackButton.place_forget()
        TutorialBackButtonDisabled.place(x=607.0, y=621.0, width=50.0, height=50.0)
        
        TutorialPage -= 1
    elif TutorialPage == 3:
        canvas.itemconfig(Tutorialbg3, state="hidden")
        canvas.itemconfig(Tutorialbg2, state="normal")
        
        TutorialPage -= 1
    elif TutorialPage == 4:
        canvas.itemconfig(Tutorialbg4, state="hidden")
        canvas.itemconfig(Tutorialbg3, state="normal")
        
        TutorialPage -= 1
    elif TutorialPage == 5:
        canvas.itemconfig(Tutorialbg5, state="hidden")
        canvas.itemconfig(Tutorialbg4, state="normal")
        
        TutorialPage -= 1
    elif TutorialPage == 6:
        canvas.itemconfig(Tutorialbg6, state="hidden")
        canvas.itemconfig(Tutorialbg5, state="normal")
        
        TutorialPage -= 1
    elif TutorialPage == 7:
        canvas.itemconfig(Tutorialbg7, state="hidden")
        canvas.itemconfig(Tutorialbg6, state="normal")
        
        TutorialForwardButton.place(x=657.0, y=621.0, width=50.0, height=50.0)
        TutorialForwardButtonDisabled.place_forget()
        
        TutorialPage -= 1
    else:
        print("Invalid Tutorial Page")
    
def TutorialForwardbtn():
    print("Tutorial Forward Button clicked")
    global TutorialPage
    
    if TutorialPage == 1:
        
        canvas.itemconfig(Tutorialbg1, state="hidden")
        canvas.itemconfig(Tutorialbg2, state="normal")
        
        TutorialBackButtonDisabled.place_forget()
        TutorialBackButton.place(x=607.0, y=621.0, width=50.0, height=50.0)
        
        TutorialPage += 1
    elif TutorialPage == 2:
        canvas.itemconfig(Tutorialbg2, state="hidden")
        canvas.itemconfig(Tutorialbg3, state="normal")
        
        TutorialPage += 1
    elif TutorialPage == 3:
        canvas.itemconfig(Tutorialbg3, state="hidden")
        canvas.itemconfig(Tutorialbg4, state="normal")
        
        TutorialPage += 1
    elif TutorialPage == 4:
        canvas.itemconfig(Tutorialbg4, state="hidden")
        canvas.itemconfig(Tutorialbg5, state="normal")
        
        TutorialPage += 1
    elif TutorialPage == 5:
        canvas.itemconfig(Tutorialbg5, state="hidden")
        canvas.itemconfig(Tutorialbg6, state="normal")
        
        TutorialPage += 1
    elif TutorialPage == 6:
        canvas.itemconfig(Tutorialbg6, state="hidden")
        canvas.itemconfig(Tutorialbg7, state="normal")
        
        TutorialForwardButton.place_forget()
        TutorialForwardButtonDisabled.place(x=657.0, y=621.0, width=50.0, height=50.0)
        
        TutorialPage += 1
    else:
        print("Invalid Tutorial Page")
    
#Follow Button Functions
    
def Followbtn_Github():
    print("Follow GitHub Button clicked")
    webbrowser.open_new_tab('https://github.com/MisterXlus')
    
def Followbtn_YouTube_func():
    print("Follow YouTube Button clicked")
    webbrowser.open_new_tab('https://www.youtube.com/@MisterXlus')
    
def Followbtn_Kofi_func():
    print("Follow Kofi Button Clicked")
    webbrowser.open_new_tab('https://ko-fi.com/misterxlus')
    
def infobtn():
    print("Info Button clicked")
    
    canvas.itemconfig(image_1, state="hidden")
    canvas.itemconfig(cmdline, state="hidden")
    canvas.itemconfig(output, state="hidden")
    cmdline_func.place_forget()
    output_func.place_forget()
    
    listswitch.place_forget()
    singleswitch.place_forget()
    listsearch.place_forget()
    listinstall.place_forget()
    singlesearch.place_forget()
    singleinstall.place_forget()
    setpath.place_forget()
    tutorialbutton.place_forget()
    silent_checkbox.place_forget()
    update.place_forget()
    installed.place_forget()
    update_all.place_forget()
    updateble.place_forget()
    
    #---------------------------------------------
    
    infobutton.place_forget()
    
    Followbtn_GitHub.place(x=1157.0, y=643.0, width=88.0, height=88.0)
    Followbtn_YouTube.place(x=1015.0, y=648.0, width=118.0, height=81.0)
    Followbtn_Kofi.place(x=903.0, y=643.0, width=88.0, height=88.0)
    backbutton.place(x=1284.0, y=48.0, width=50.0, height=50.0)
    canvas.itemconfig(infogb, state="normal")

#Back Button Function

def backbtn():
    print("Back Button clicked")
    
    backbutton.place_forget()
    Followbtn_GitHub.place_forget()
    Followbtn_YouTube.place_forget()
    Followbtn_Kofi.place_forget()
    canvas.itemconfig(infogb, state="hidden")
    
    canvas.itemconfig(Tutorialbg1, state="hidden")
    canvas.itemconfig(Tutorialbg2, state="hidden")
    canvas.itemconfig(Tutorialbg3, state="hidden")
    canvas.itemconfig(Tutorialbg4, state="hidden")
    canvas.itemconfig(Tutorialbg5, state="hidden")
    canvas.itemconfig(Tutorialbg6, state="hidden")
    canvas.itemconfig(Tutorialbg7, state="hidden")
    TutorialBackButton.place_forget()
    TutorialForwardButton.place_forget()
    TutorialBackButtonDisabled.place_forget()
    TutorialForwardButtonDisabled.place_forget()
    
    #---------------------------------------------
    
    canvas.itemconfig(image_1, state="normal")
    canvas.itemconfig(cmdline, state="normal")
    canvas.itemconfig(output, state="normal")
    cmdline_func.place(x=146.0, y=268.0, width=803.0, height=46.0)
    output_func.place(x=146.0, y=414.0, width=803.0, height=299.0)

    setpath.place(x=924.0, y=268.0, width=161.0, height=48.0)
    listswitch.place(x=976.0, y=414.0, width=155.0, height=36.0)
    singleswitch.place(x=976.0, y=587.0, width=155.0, height=36.0)
    listsearch.place(x=1038.0, y=468.0, width=155.0, height=36.0)
    listinstall.place(x=1038.0, y=522.0, width=155.0, height=36.0)
    singlesearch.place(x=1042.0, y=630.0, width=155.0, height=36.0)
    singleinstall.place(x=1042.0, y=684.0, width=155.0, height=36.0)
    silent_checkbox.place(x=126.0, y=328.0)
    update.place(x=769.0, y=224.0, width=155.0, height=36.0)
    installed.place(x=769.0, y=179.0, width=155.0, height=36.0)
    update_all.place(x=576.0, y=224.0, width=179.0, height=36.0)
    updateble.place(x=576.0, y=179.0, width=179.0, height=36.0)

    tutorialbutton.place(x=130.0, y=191.0, width=155.0, height=36.0)
    infobutton.place(x=1284.0, y=47.0, width=50.0, height=50.0)


#Programm End----------------------------------------------------------------------------------------------------------------------------------------
titlebar.bind("<Button-1>", start_move)
titlebar.bind("<B1-Motion>", move_window)
title_label.bind("<Button-1>", start_move)
title_label.bind("<B1-Motion>", move_window)
window.mainloop()