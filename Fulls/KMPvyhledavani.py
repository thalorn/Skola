import csv
import time



def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
  
    initial_point = []
    m = 0
    n = 0
  
    while m != a:
       
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]
       
        if n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
   
    return initial_point
def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr

def KMPSearch(pat, txt, count): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            #print ("Found pattern at index " + str(i-j) )
            count += 1
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1

def kmp_table(find, findLen, T):
    
    # Vytvoříme pole čísel -
    # každé číslo souvisí se znakem na stejné pozici v hledaném slově
    # Číslo znamená pokud na této pozici algoritmus selže (nenajde stejný znak),
    # tak o tolik znaků se může algoritmus posunout aniž by zameškal něco důležitého
    # a zároveň již tolik znaků má nalezeno v příštím srovnávání stejných znaků
    
    T[0] = 0 #vždy nula
    
    pos = 1 # pozice v hledanem slove
    cnd = 0 # pocet stejnych znaku se zacatkem hledaneho slova
    
    while pos < findLen:
        if find[pos] == find[cnd]: 
            cnd += 1
            T[pos] = cnd
            pos += 1
        else:
            if cnd != 0: # Zkoumáme ještě více předchozí znaky
                cnd -= 1
            else:
                T[pos] = cnd #T[pos] = 0 aneb nenachází se na začátku ani jeho substringu
                pos += 1

start = time.time()

find = "Suspendisse"   # V souboru se nachází
#find = "pegesta"  # V souboru se nenachází

#kmp_table(find, findLen, T)
findLen = len(find)
T = [0] * findLen


with open('data2500k.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    i = 0
    count = 0
    
    for row in reader:   
        strRow = ', '.join(row) # Každý řádek spojí do jednoho stringu
#         KMPSearch(find, strRow, count)
        rowLen = len(strRow)
        initial_index = KMP_String(find, strRow)
        for j in initial_index:
            count += 1
#         j = 0 # index pro strRow
#         u = 0 # index pro find
#         while j < rowLen:
#             if strRow[j] == find[u]:
#                 j += 1
#                 u += 1
#             if u == findLen:
#                 count += 1   # Počet nalezených shod
#                 #print("Výraz " + find + " nalezen  na " + str(i) + " řádku.")
#                 flag = True
#                 u = T[u-1]
#             elif j < rowLen and strRow[j] != find[u]:
#                 if u != 0:
#                     u = T[u-1]
#                 else:
#                     j += 1
        i += 1
        if i % 10000 == 0:
            print("Zkoumám " + str(i) + ". řádek.")
    
    
    if count == 0:
        print("Výraz " + find + " nebyl v datovém souboru nalezen.")
    else:
        print("Výraz " + find + " byl v souboru nalezen " + str(count) + "krát.")

end = time.time()
print("Vyhledávání zabralo " + str(end - start) + " vteřin.")    