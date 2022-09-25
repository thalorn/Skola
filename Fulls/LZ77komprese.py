import time
import struct
import sys
import math

def LZ77_search(search, look_ahead):

     ls = len(search)
     llh = len(look_ahead)
 
     if(ls==0):
        return (0,0, look_ahead[0])
     
     if(llh)==0:
        return (-1,-1,"")

     best_length=0
     best_offset=0 
     buf = search + look_ahead

     search_pointer = ls    
     for i in range(0,ls):
        length = 0
        while buf[i+length] == buf[search_pointer +length]:
            length = length + 1
            if search_pointer+length == len(buf):
                length = length - 1
                break
            if i+length >= search_pointer:
                break    
        if length > best_length:
            best_offset = i
            best_length = length

     return (best_offset, best_length, buf[search_pointer+best_length])

def read_in_chunks(file_object, chunk_size=1048576):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


x = 16
MAXSEARCH = int(1024)
MAXLH =  int(math.pow(2, (x  - (math.log(MAXSEARCH, 2))))) 

start = time.time()
with open("data25k.csv", 'r+') as datafile, open("encoded_lz77_data_fin4.bin", 'ab') as output:
    
    mbs = 0
    #for data in read_in_chunks(datafile):
    data = datafile.read()
    searchiterator = 0;
    lhiterator = 0;

    while lhiterator<len(data):
        search = data[searchiterator:lhiterator]
        look_ahead = data[lhiterator:lhiterator+MAXLH]
        (offset, length, char) = LZ77_search(search, look_ahead)
        #print (offset, length, char)
        
        shifted_offset = offset << 6
        offset_and_length = shifted_offset+length 
        ol_bytes = struct.pack(">Hc",offset_and_length,char.encode('utf-8'))  
        output.write(ol_bytes) 
         

        lhiterator = lhiterator + length+1
        searchiterator = lhiterator - MAXSEARCH

        if searchiterator<0:
            searchiterator=0
        
        if (mbs % 10000 == 0):
            print(lhiterator,len(data))
        mbs += 1
   
        #print("Compressed MBs: " + str(i))
        #i += 1
print("Komprese trvala " + str(time.time()-start) + " vterin.")