from tkinter import *
import time
from blockchain import Blockchain, Block

window = Tk()
window.title("Blochchain")
window.minsize(width=500, height=400)

#Text
text = Text(height=30, width=70)
text.insert(END, "")
text.pack() 

#Bouton stop
flag = True
def stop():
    global flag
    print("Stop request")
    flag = False

Button(window,text='  Stop  ',command=stop).pack()


blockchain = Blockchain()
num_block = 0

def update_blockchain():
    global num_block, flag
    num_block += 1
    blockchain.mine(Block("Block " + str(num_block)))
    text.insert(END,str(blockchain.block)+"\n")
    if flag:
        window.after(2000,update_blockchain)
    else:
        print("stop")
        text.insert(END,"\n#### STOP ####")


window.after(500,update_blockchain)
window.mainloop()