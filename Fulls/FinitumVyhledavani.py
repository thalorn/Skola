import time
import csv
  
def get_next_state(pat, M, state, x):
    if state < M and x == ord(pat[state]): 
        return state+1
  
    i=0  
    for ns in range(state,0,-1): 
        if ord(pat[ns-1]) == x: 
            while(i<ns-1): 
                if pat[i] != pat[state-ns+1+i]: 
                    break
                i+=1
            if i == ns-1: 
                return ns  
    return 0
  
def gen_DFA_table(pat, M): 
    chars = 256
  
    TF = [[0 for i in range(chars)] for _ in range(M+1)] 
  
    for state in range(M+1): 
        for x in range(chars): 
            z = get_next_state(pat, M, state, x) 
            TF[state][x] = z 
  
    return TF 
  
def search_DFA(pat, row, DFA_table, count):

    M = len(pat) 
    N = len(row)     
  
    state=0
    for i in range(N): 
        state = DFA_table[state][ord(row[i])] 
        if state == M:
            count =+ 1
            #print("Pattern found at index: {}".format(i-M+1))
            pass


start = time.time()

find = "Suspendisse"

with open('data2500k.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    flag = False
    i = 0
    count = 0
    DFA_table = gen_DFA_table(find,len(find)) 
    
    for row in reader:   
        strRow = ', '.join(row) # Každý řádek spojí do jednoho stringu
        rowLen = len(strRow)
        search_DFA(find,strRow,DFA_table,count) 
        i += 1
        if i % 10000 == 0:
            print("Zkoumám " + str(i) + ". řádek.")
    
    if count == 0:
        print("Výraz " + find + " nebyl v datovém souboru nalezen.")
    else:
        print("Výraz " + find + " byl v souboru nalezen " + str(count) + "krát.")
        
end = time.time()
print("Vyhledávání zabralo " + str(end - start) + " vteřin.")
