import csv
import time

# preprocessing for bad character rule
def preprocess_bad_char(pat, m):  
    # Initialize all occurrence as -1 
    badChar = [-1]*256 
  
    # Fill the actual value of last occurrence 
    for i in range(m): 
        badChar[ord(pat[i])] = i; 
  
    # retun initialized list 
    return badChar 

# preprocessing for strong good suffix rule 
def preprocess_strong_suffix(shift, bpos, pat, m):
    i = m 
    j = m + 1
    bpos[i] = j 
  
    while i > 0: 
        while j <= m and pat[i - 1] != pat[j - 1]: 
            if shift[j] == 0: 
                shift[j] = j - i
                # Update the position of next border 
            j = bpos[j] 
        i -= 1
        j -= 1
        bpos[i] = j 
  
# preprocessing for partial suffix rule
def preprocess_partial_suffix(shift, bpos, pat, m): 
    j = bpos[0] 
    for i in range(m + 1): 
        if shift[i] == 0: 
            shift[i] = j 
        if i == j: 
            j = bpos[j] 
  
def BMsearch(text, pat): 
    count = 0
    s = 0 #shift
    m = len(pat) 
    n = len(text) 
  
    bpos = [0] * (m + 1) 
    shift = [0] * (m + 1) 
  
    # do preprocessing
    badChar = preprocess_bad_char(pat,m)
    preprocess_strong_suffix(shift, bpos, pat, m) 
    preprocess_partial_suffix(shift, bpos, pat, m) 
  
    while s <= n - m: 
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]: 
            j -= 1
        if j < 0: 
            #print("Shoda nalezena na řádku " + str(row) + " s posunem " + str(s))
            count += 1
            if s+m < n:
                s += max(m-badChar[ord(text[s+m])],shift[0])
            else:
                s += 1
        else: 
            s += max(shift[j + 1],j-badChar[ord(text[s+j])])
    return count

start = time.time()

find = "Suspendisse"

with open('data2500k.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    flag = False
    i = 0
    count = 0
    
    for row in reader:   
        strRow = ', '.join(row) # Každý řádek spojí do jednoho stringu
        rowLen = len(strRow)
        count += BMsearch(strRow,find) 
        i += 1
        if i % 10000 == 0:
            print("Zkoumám " + str(i) + ". řádek.")
    
    if count == 0:
        print("Výraz " + find + " nebyl v datovém souboru nalezen.")
    else:
        print("Výraz " + find + " byl v souboru nalezen " + str(count) + "krát.")
        
end = time.time()
print("Vyhledávání zabralo " + str(end - start) + " vteřin.")

