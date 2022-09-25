import csv
import time
#import pandas as ps

# import ahocorasick as ahc
# 
# def create_ac_automata(patterns):
#     A = ahc.Automaton()  # initialize
#     for (key, cat) in patterns:
#         A.add_word(key, (cat, key)) # add keys and categories
#     A.make_automaton() # generate automaton
#     return A
# 
# def find_keywords(line, A, countPats):
#     for end_index, (cat, keyw) in A.iter(line):
#         countPats[keyw] += 1 

class ac_node:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None

def create_ac_forest(patterns):
    root = ac_node()
 
    for pat in patterns:
        node = root
        for symbol in pat:
            node = node.goto.setdefault(symbol, ac_node())
        node.out.append(pat)
    return root
 
def create_ac_statemachine(patterns):
    root = create_ac_forest(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root
 
    while len(queue) > 0:
        rnode = queue.pop(0)
 
        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode != None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out
 
    return root
 
 
def search_ac(s, root, count):
    node = root
 
    for i in range(len(s)):
        while node != None and s[i] not in node.goto:
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            count += 1 

start = time.time()
find = [('lobortis',1), ('Suspendisse',1), ('Sus',1)]
countPats = {'lobortis':0, 'Suspendisse':0, 'Sus':0}
#A = create_ac_automata(find)

count = 0
root = create_ac_statemachine(find)

#import datatable as dt
#data = datatable.fread(input_file)

#print(data)
#data = dask.dataframe.read_csv('data100.csv')
#data.apply(search_ac)

with open('data2500k.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    count = 0
    root = create_ac_statemachine(find)
    for row in reader:   
        strRow = ', '.join(row) # Každý řádek spojí do jednoho stringu
        rowLen = len(strRow)
        #find_keywords(strRow,A,countPats)
        search_ac(strRow, root, count)
        
        if reader.line_num % 10000 == 0:
            print("Zkoumám " + str(reader.line_num) + ". řádek.")

    for x in countPats.values():
        count += x
    
    if count == 0:
        print("Výrazy nebyly v datovém souboru nalezeny.")
    else:
        print("Výrazy " + find[0][0] + ", " + find[1][0] + ", " + find[2][0] + " byly v souboru nalezeny " + str(count) + "krát.")
        
end = time.time()
print("Vyhledávání zabralo " + str(end - start) + " vteřin.")