import contextlib, sys, time
import arithmeticcoding


# Command line main application function.
def main(arg1, arg2):
    # Handle command line arguments
   
    inputfile = arg1
    outputfile = arg2
    
    # Read input file once to compute symbol frequencies
    freqs = get_frequencies(inputfile)
    freqs.increment(256)  # EOF symbol gets a frequency of 1
    
    # Read input file again, compress with arithmetic coding, and write output file
    with open(inputfile, "rb") as inp, \
            contextlib.closing(arithmeticcoding.BitOutputStream(open(outputfile, "wb"))) as bitout:
        write_frequencies(bitout, freqs)
        compress(freqs, inp, bitout)


# Returns a frequency table based on the bytes in the given file.
# Also contains an extra entry for symbol 256, whose frequency is set to 0.
def get_frequencies(filepath):
    freqs = arithmeticcoding.SimpleFrequencyTable([0] * 257)
    with open(filepath, "rb") as input:
        while True:
            b = input.read(1)
            if len(b) == 0:
                break
            freqs.increment(b[0])
    return freqs


def write_frequencies(bitout, freqs):
    for i in range(256):
        write_int(bitout, 32, freqs.get(i))


def compress(freqs, inp, bitout):
    enc = arithmeticcoding.ArithmeticEncoder(32, bitout)
    while True:
        symbol = inp.read(1)
        if len(symbol) == 0:
            break
        enc.write(freqs, symbol[0])
    enc.write(freqs, 256)  # EOF
    enc.finish()  # Flush remaining code bits


# Writes an unsigned integer of the given bit width to the given stream.
def write_int(bitout, numbits, value):
    for i in reversed(range(numbits)):
        bitout.write((value >> i) & 1)  # Big endian


# Main launcher
if __name__ == "__main__":
    start = time.time()
    main("data100.csv","encoded_AC_big_wtf.txt")
    print ("Uplynulý čas: " + str(time.time() - start))