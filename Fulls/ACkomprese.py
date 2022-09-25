import time
from collections import defaultdict
from fractions import Fraction

def frac_prob(codes):
    count = defaultdict(int)
    for code in codes:
        count[code] += 1
        
    count[256] = 1
    
    prob = {}
    length = len(codes)
    cum_count = 0
    
    for code in sorted(count, key=count.get, reverse=True):
        curr_count = count[code]
        prob_pair = Fraction(cum_count, length), Fraction(curr_count, length)
        prob[code] = prob_pair
        cum_count += curr_count
    return prob

def encode_fraction_range(input_codes, input_prob):
    start = Fraction(0, 1)
    width = Fraction(1, 1)

    for code in input_codes:
        d_start, d_width = input_prob[code]
        start += d_start * width
        width *= d_width

    return start, start + width

def find_binary_fraction(input_start, input_end):
    output_fraction = Fraction(0, 1)
    output_denominator = 1

    while not (input_start <= output_fraction < input_end):
        output_numerator = 1 + ((input_start.numerator * output_denominator) // input_start.denominator)
        output_fraction = Fraction(output_numerator, output_denominator)
        output_denominator *= 2

    return output_fraction

def readChunk(file_object, size = 1024):
    while True:
        data = file_object.read(size)
        if not data:
            break
        yield data

def readByChunk():
    with open("data250.csv","r+") as datafile, open("encoded_AC_data_fin4.txt","ab") as output:
        i = 0
        for data in readChunk(datafile, 1024):
            codes =  [ord(char) for char in data] + [256]
            prob = frac_prob(codes)
            #print('gg')
            
            fraction_range = encode_fraction_range(codes, prob)
            #print('fraction_range:', repr(fraction_range))

            binary_fraction = find_binary_fraction(fraction_range[0], fraction_range[1])
            #print('binary_fraction:', repr(binary_fraction))
            
            #compressed_chunk = compress(data)
            output.write(binary_fraction)
            print("kBs compressed: " + str(i))
            i += 1

start = time.time()

readByChunk()
print ("Uplynulý čas: " + str(time.time() - start))