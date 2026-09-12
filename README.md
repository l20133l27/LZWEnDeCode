LZWEnDeCode - Robert Wood rwood1@muskingum.edu

Included:
README.md
input0.txt
input1.txt
LZWEnDeCode.py

Programming Language: Python 3
Written With: Thonny IDE, Notepad
Tested Via: Windows 11 Terminal

Program Design: 
	Implements the LZW algorithm with fixed bit-length encoding, where the bit-length is selected by the user. The maximum size of the table is 2^N, where N is the bit-length.

Explanation for files:

	READ_ME.txt:
		This file. It contains an explanation of each file found in the project. 
		
	input0.txt:
		This is sample input that is found in the project, "abbbab", to test the encode and decode commands.
		Expected output for encoding: [97,98,257,256]

	input1.txt:
		This is sample input that you may use to test the encode and decode commands.

	LZWEnDeCode.py:
		Source code file, containing the following functions:
			lzw_encode(text, bit_length):
				Encodes ASCII text into a list of integer LZW codes.
			lzw_decode(codes, bit_length):
				Decodes a list of integer LZW codes into ASCII text.
			read_text_file(NAME):
				Reads an input text file as ASCII.
			read_lzw_file(NAME):
				Reads an encoded .lzw file in binary mode, 2 bytes (16 bits) at a time, and converts it to a list of integer codes.
			write_file(NAME, text):
				Writes decoded ASCII to a file.
			write_lzw_file(NAME, codes):
				Writes encoded codes to a .lzw file.
			make_encoded_filename(in_file):
				Produces the output file name for encoded data.
			make_decoded_filename(in_file):
				Produces the output filename for decoded text.
			main():
			Handles command line arguments, determines running encoding or decoding.

Data Structures Used:
	Dictionary: 
	Used in both the lzw_encode and lzw_decode functions.
		
		lzw_encode:
		Maps strings to integer codes.
		"ab" is 256

		lzw_decode:
		Maps integer codes to strings. 
		256 is "ab"

Working:
	Encoding ASCII
	Producing Integer output (abbbab) -> [97, 98, 257, 256]
	Writing to .lzw files as 2 byte output
	Reading encoded files
	Decoding encoded files to ASCII

Limits:
	Expects all text to be in the ASCII character set
	Does not handle empty files
	Anticipates encoded files be created by this program

To Run:
	Open the terminal in the folder containing LZWEnDeCode.py and your input.

	Encode:
		py LZWEnDeCode.py encode <file_to_encode.txt> <integer_bit_length>
	Decode:
		py LZWEnDeCode.py decode <file_to_decode.lzw> <integer_bit_length>
