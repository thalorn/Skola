import time

def rle_compression(data):
    
    compressed = ""
    prechar = ""
    count = 1
    
    for char in data:
        if char != prechar:
            if prechar != "":
                compressed += str(count) + prechar
            count = 1
            prechar = char
        else:
            count += 1
    compressed += str(count) + prechar
    return compressed

def read_in_chunks(file_object, chunk_size=1048576):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

start = time.time()
with open("data2500k.csv", 'r+') as datafile, open("encoded_rle_data_fin2.txt", 'a') as output:
    i = 0
    for data in read_in_chunks(datafile):
        
        string = rle_compression(data)
        output.write(string)
        print("Compressed MBs: " + str(i))
        i += 1
        
print("Komprese trvala " + str(time.time()-start) + " vterin.")