import argparse
import math
import random
import sys


def generate_file(file_name):
    """
    Here's my docstring for my generate file. If this doesn't get filled in I get - 5.
                
    Positional Arguments: Parameters required include an input file, type of encoding, and number of bytes to read
                       
    Side Effects: Entropy can be affected by number of bytes to read and type of encoding(utf-8 requires 3 bytes for some characters that only require 2 bytes for utf-16)
    """
    with open(file_name, "w", encoding = "utf-8") as f:
        byte = int(input('Enter number of bytes: '))

        for i in range (0, byte):
            f.write("{}".format(chr(random.randint(0,256))))

    print ('Generate file: ', file_name)



def calculate_entropy(file_name):
    """
    Here's my docstring for my calculate entropy. If this doesn't get filled in I get - 5.
                                                   
    Positional Arguments: Parameter required include the generated file from the first part of this code
                                                          
    Side Effects: Different character counts in array and different file size will affect entropy value 
    """

    f = open(file_name,'rb')
    test_file = bytearray(f.read())
    f.close()

    array = [0] * 257
    total_count = 0

    for k in test_file:
        array[k]+=1
        total_count+=1

    entropy = 0.0 
    for freq in array:
        if freq > 0: 
            #Shannon's entropy formula referred from Cisco blog
            prob = float(freq) / total_count
            entropy += prob * math.log(1/prob, 2)

    print ('Shannon Entropy: ', entropy)
    print ('Minimum number of bits required to encode each symbol: ', (math.ceil(entropy))) 



## DO NOT NEED TO EDIT ANYTHING UNDER HERE
# setup command line options
parser = argparse.ArgumentParser(description='Generate a random file and calculate its Shannon Entropy')
parser.add_argument('-e', '--execute', dest='fxn', help='Function to be executed: calcaulte, generate, main')
parser.add_argument('-f', '--file', default='lab6.txt', dest='file_name', help='File to either calculate entropy or generate into')

args = parser.parse_args()

if args.fxn == 'generate':
    generate_file(args.file_name)
elif args.fxn == 'calculate':
    calculate_entropy(args.file_name)
elif args.fxn == 'main':
    generate_file(args.file_name)
    calculate_entropy(args.file_name)
else:
    parser.print_help()
