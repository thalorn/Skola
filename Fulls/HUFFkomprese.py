import heapq
import time

codes = {}
reverse_code = {}

class HuffNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq


def frequency_dict(data):
    frequency = {}
    for char in data:
        if not char in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def make_heap(freq):
    heap = []
    for key in freq:
        node = HuffNode(key, freq[key])
        heapq.heappush(heap,node)
    return heap

def node_merging(heap):
    while (len(heap)>1):
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merge = HuffNode(None, node1.freq + node2.freq)
        merge.left = node1
        merge.right = node2
        
        heapq.heappush(heap,merge)
    return heap
    
    
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

def read_in_chunks(file_object, chunk_size=1048576):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
        
def huff_compression():
    
    
    with open("data2500k.csv", 'r+') as datafile, open("encoded_huffman_data_fin2.bin", 'ab') as output:
        
        i = 0
        for data in read_in_chunks(datafile):
            
            freq = frequency_dict(data)
            heap = make_heap(freq)
            heap = node_merging(heap)
            
            root = heapq.heappop(heap)
            current_code = ""
            make_codes(root, current_code)
            
            encoded_text = ""
            for char in data:
                encoded_text += codes[char]
            padded_encoded_text = pad_encoded_text(encoded_text)
            byte_arr = get_byte_array(padded_encoded_text)
        
            output.write(bytes(byte_arr))
            print("Compressed MBs: " + str(i))
            i += 1
        
def make_codes(root, current_code):
    global codes
    global reverse_code
    
    if(root == None):
        return
    if(root.char != None):
        codes[root.char] = current_code
        reverse_code[current_code] = root.char
        return

    make_codes(root.left, current_code + "0")
    make_codes(root.right, current_code + "1")        

start = time.time()
huff_compression()
print("Komprese trvala " + str(time.time()-start) + " vterin.")
