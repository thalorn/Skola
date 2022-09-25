from __future__ import print_function
from numpy.lib.scimath import log2
from operator import itemgetter
import math
import time
Shannon_Fano_dict={}
Huffman_dict = {}
equable_dict ={}
def get_seq():
    message = "ahahashiodhaoidsasdoianiodnasiond oadioadoi asdloalod alod uoafuid fowq wuic w"
    return message

def read_in_chunks(file_object, chunk_size=1048576):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def Shannon_Fano_coding(seq, code):
    a = {}
    b = {}
    if len(seq) == 1:
        Shannon_Fano_dict[seq.popitem()[0]] = code
        return 0
    for i in sorted(seq.items(), key=itemgetter(1), reverse=True):
        if sum(a.values()) < sum(b.values()):
            a[i[0]] = seq[i[0]]
        else:
            b[i[0]] = seq[i[0]]
    Shannon_Fano_coding(a, code + "0")
    Shannon_Fano_coding(b, code + "1")

def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text


def get_byte_array(padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b

start = time.time()
with open("data2500k.csv", 'r+') as datafile, open("encoded_shafano_data_fin2.bin", 'ab') as output:
    mbs = 0
    for message in read_in_chunks(datafile):
        
        count = {}
        for c in message:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        Shannon_Fano_coding(count, "")
        encoded_text = ""
        for i in message:
            encoded_text += Shannon_Fano_dict[i]
        padded_encoded_text = pad_encoded_text(encoded_text)
        byte_arr = get_byte_array(padded_encoded_text)
        output.write(bytes(byte_arr))
        print("Compressed MBs: " + str(mbs))
        mbs += 1
    
print("Komprese trvala " + str(time.time()-start) + " vterin.")