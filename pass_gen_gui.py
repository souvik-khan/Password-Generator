"""
25-07-2018
Created by Souvik
"""

import tkinter
import pass_gen

#constants
windowTitle = "Password Generator"
windowDim = "250x150"
easyBtnTxt = "Easy"
mediumBtnTxt = "Medium"
hardBtnTxt = "Hard"
showPassLblTxt = "Generated password will be shown here"

def easyBtnFunc():
    showPassLbl.config(text = pass_gen.main(pass_gen.easyConst))
    
def mediumBtnFunc():
    showPassLbl.config(text = pass_gen.main(pass_gen.mediumConst))

def hardBtnFunc():
    showPassLbl.config(text = pass_gen.main(pass_gen.difficultConst))

root = tkinter.Tk()
root.title(windowTitle)
root.geometry(windowDim)
showPassLbl = tkinter.Label(root, text = showPassLblTxt)
easyBtn = tkinter.Button(root, text = easyBtnTxt, command = easyBtnFunc)
easyBtn.pack()
mediumBtn = tkinter.Button(root, text = mediumBtnTxt, command = mediumBtnFunc)
mediumBtn.pack()
hardBtn = tkinter.Button(root, text = hardBtnTxt, command = hardBtnFunc)
hardBtn.pack()
showPassLbl.pack()
root.mainloop()
