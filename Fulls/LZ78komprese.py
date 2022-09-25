import time

def readChunk(file_object, size = 1024):
    while True:
        data = file_object.read(size)
        if not data:
            break
        yield data

def readByChunk():
    with open("data2500k.csv", 'r+') as datafile, open("encoded_lz78_data_big_fin5.txt", 'a') as output:
        i = 0
        for data in readChunk(datafile, 1048576):
            compressed_chunk = encodeLZ(data)
            #compressed_chunk = map(lambda a : str(a), compressed_chunk)
            output.write("".join(compressed_chunk))
            print("Chunk number " + str(i))
            i += 1

def encodeLZ(text_from_file):
    
    #encoded_file.write('0' + text_from_file[0])
    #print('0' + text_from_file[0])
    encoded_chunk = '0' + text_from_file[0]
    dict_of_codes = {text_from_file[0]: '1'}
    text_from_file = text_from_file[1:]
    encoded_chunk = ''
    combination = ''
    code = 2
    for char in text_from_file:
        combination += char
        if combination not in dict_of_codes:
            dict_of_codes[combination] = str(code)
            if len(combination) == 1:
                #encoded_file.write('0' + combination)
                #print('0' + combination)
                encoded_chunk += '0' + combination
            else:
                #encoded_file.write(dict_of_codes[combination[0:-1]] + combination[-1])
                #print(dict_of_codes[combination[0:-1]] + combination[-1])
                encoded_chunk += dict_of_codes[combination[0:-1]] + combination[-1]
            code += 1
            combination = ''
    return encoded_chunk


def decodeLZ(FileIn, FileOut):
    coded_file = open(FileIn, 'r')
    decoded_file = open(FileOut, 'w')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    for char in text_from_file:
        if char in '1234567890':
            combination += char
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()
    
start = time.time()
readByChunk()
#print(encodeLZ("ggwpveryggasdododkpsodnfpinspppgofoegfookemkerefer"))
#encodeLZ("data10kk.csv","encoded_lz88_data_big.bin")
print("Komprese trvala " + str(time.time()-start) + " vteřin.")