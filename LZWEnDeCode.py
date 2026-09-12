#LZW Encoder/Decoder RW rwood1@muskingum.edu

import os
import sys

def lzw_encode(text, bit_length):
    MAX_TABLE_SIZE = 2 ** bit_length #MAX_TABLE_SIZE=2^(bit_length)
    #makes a dictionary with every character value from 0 to 255
    TABLE = {chr(i): i for i in range(256)} #initalize TABLE[0 to 255] = code for individual characters
    next_code = 256
    #using string = none doesn't work
    STRING = "" #STRING = null
    out_codes = []
    
    for SYMBOL in text: #while input symbol
        if STRING + SYMBOL in TABLE:
            STRING = STRING + SYMBOL
        else:
            out_codes.append(TABLE[STRING]) #output the code for STRING
            
            if len(TABLE) < MAX_TABLE_SIZE:
                TABLE[STRING + SYMBOL] = next_code
                next_code +=1
                
            STRING = SYMBOL
    if STRING != "":
        out_codes.append(TABLE[STRING]) #output code for string
    return out_codes #return list of codes

def lzw_decode(codes, bit_length):
    MAX_TABLE_SIZE = 2 ** bit_length #MAX_TABLE_SIZE=2^(bit_length)
    #makes a dictionary with every character value from 0 to 255
    TABLE = {i : chr(i) for i in range(256)} #initalize TAB:E[0 to 255] = code for individual characters
    next_code = 256
    
    CODE = codes[0]
    STRING = TABLE[CODE]
    out_txt = [STRING]
    
    for CODE in codes[1:]: #while input code
        if CODE not in TABLE: #if TABLE[CODE] is not defined
            NEW_STRING = STRING + STRING[0]
        else:
            NEW_STRING = TABLE[CODE]
            
        out_txt.append(NEW_STRING)
            
        if len(TABLE) < MAX_TABLE_SIZE:
            TABLE[next_code] = STRING + NEW_STRING[0]
            next_code +=1
                
        STRING = NEW_STRING
    return "".join(out_txt) #return decoded string

def read_lzw_file(NAME):
    codes = []
    #open NAME for reading binary as f
    with open(NAME, "rb") as f:
        #read file 2 bytes (16 bits) at a time
        while True:
            two_bytes = f.read(2)
            
            #stop when no more
            if not two_bytes:
                break
            
            #convert to integer and store
            code = int.from_bytes(two_bytes, byteorder="big")
            codes.append(code)
        return codes

def read_text_file(NAME):
    #open NAME for reading as ASCII as f
    with open(NAME, "r", encoding="ascii") as f:
        #read as string
        return f.read()

def write_lzw_file(NAME, codes):
    #open NAME for writing binary as f
    with open(NAME, "wb") as f:
        for code in codes:
            f.write(code.to_bytes(2, byteorder="big"))

def write_file(NAME, text):
    #open NAME for writing ASCII as f
    with open(NAME, "w", encoding="ascii") as f:
        f.write(text)

def make_encoded_filename(in_file):
    base_name = os.path.splitext(in_file)[0]
    return base_name + ".lzw"

def make_decoded_filename(in_file):
    base_name = os.path.splitext(in_file)[0]
    return base_name + "_decode.txt"

def main():
    #if the arguments aren't the proper size show what we're looking for
    if len(sys.argv) != 4:
        print("Commands:")
        print("python LZWEnDeCode.py encode <inputfile> <bitlength>")
        print("python LZWEnDeCode.py decode <inputfile> <bitlength>")
        sys.exit()
        
    mode = sys.argv[1]
    input_filename = sys.argv[2]
    bit_length = int(sys.argv[3])
    
    #calls encode related functions
    if mode == "encode":
        text = read_text_file(input_filename)
        print("Read:", input_filename)
        print("Bit Length:",bit_length)
        
        codes = lzw_encode(text, bit_length)
        
        print("Encoded Data:")
        print(codes)
        
        out_file = make_encoded_filename(input_filename)
        write_lzw_file(out_file,codes)
        
        print("Wrote:", out_file)
    
    #calls decode related functions
    elif mode == "decode":
        codes = read_lzw_file(input_filename)
        print("Read:", input_filename)
        print("Bit Length:", bit_length)
        
        decoded_txt = lzw_decode(codes, bit_length)
        
        out_file = make_decoded_filename(input_filename)
        write_file(out_file, decoded_txt)
        
        print("Wrote:", out_file)
    
    #safety
    else:
        print("arg1 must be 'encode' or 'decode'")
        
if __name__ == "__main__":
    main()