################################################################
## Richard Jansen HAN University of Applied Sciences Nijmegen ##
## Afvinkopdracht 6 Blok 3a 24########################
################################################################

import sys
sys.setrecursionlimit(1500)
from tkinter import *
from tkinter import filedialog
niets=Tk()
file = filedialog.askopenfile()
niets.destroy()
niets.mainloop()

raw_data = ""
startReading = False
for regel in file:
    if startReading:
        raw_data += regel[10:]
    if "ORIGIN" in regel:
        startReading = True
sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')

def main():
    x = sequence.index("atg")        
    seq = sequence[x:]               
    x = 0                       
    seq = sequence[x:]
    dna = True                  
    recursie(x, seq, dna)

def recursie(x, a, dna):
    totaal = len(a)             
    nuc = ["a", "t", "c", "g"]  
    if x > totaal:              
        seq = a[0]                
        if sequence not in nuc:        
            dna = False
            return recursie(x,a[1:], dna)
    else:
        print("DNA: " + str(dna))

main()