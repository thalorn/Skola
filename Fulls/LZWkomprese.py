import time

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    #dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3:
    dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()

def readChunk(file_object, size = 1024):
    while True:
        data = file_object.read(size)
        if not data:
            break
        yield data

def readByChunk():
    with open("data250k.csv", 'r+') as datafile, open("encoded_lzw_data_fin1.bin", 'a') as output:
        i = 0
        for data in readChunk(datafile, 1048576):
            compressed_chunk = compress(data)
            compressed_chunk = map(lambda a : str(a), compressed_chunk)
            output.write(" ".join(compressed_chunk))
            print("Chunk number " + str(i))
            i += 1
start = time.time()
#readByChunk()
with open("data250k.csv", 'r+') as datafile, open("encoded_lzw_data_fin5.bin", 'a') as output:
        compressed_chunk = compress(datafile.read())
        compressed_chunk = map(lambda a : str(a), compressed_chunk)
        output.write("".join(compressed_chunk))
        print("gg")
# How to use:
print ("Uplynulý čas: " + str(time.time() - start))