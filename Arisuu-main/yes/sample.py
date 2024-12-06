from tkinter import *
from pathlib import Path
def relative_to_assets(path: str) ->Path:
    return ASSETSPATH / Path(path)

OUTPUTPATH = Path(__file__).parent
ASSETSPATH =OUTPUTPATH/Path(r"C:\Users\TaysaMarkAnthony(Stu\.vscode\cli\arisu\idk\yes")


newwindow = Tk()
newwindow.geometry("420x420")
newwindow.title("ARiSu")
icon = PhotoImage(file =relative_to_assets("pngegg.png"))
newwindow.iconphoto(False,icon)
newwindow.mainloop()