import argparse
import time
from struct import node, stack, queue

def main(struct, input_file, output_file):
    if struct == 'queue':
        test = queue()
    else:
        test = stack()
#####
    f = open(input_file)
    input = f.readlines()
    for i in range(len(input)):
        word = input[i]
        if word[1] == 'U' and struct == 'queue':
            test.push(node(int(word[5:])))
            test.printqueue()

        elif struct == 'queue':
            test.pop()
            test.printqueue()

        elif word[1] == 'U' and struct == 'stack':
            test.push(node(int(word[5:])))
            test.printstack()

        else:
            test.pop()
            test.printstack()
#####
    #output = open(output_file, 'a') 直接寫在struct裡面的printstack or printqueue，多次測試input會續寫到output中。
    
if __name__ == '__main__':
    # Do Not Change the code here
    parser = argparse.ArgumentParser()
    parser.add_argument('--structure', choices=['queue', 'stack'], default='stack')
    parser.add_argument('--input', default='./input.txt')
    parser.add_argument('--output', default='./output.txt')
    args = parser.parse_args()
    ts = time.time()
    main(args.structure, args.input, args.output)
    te = time.time()
    print('Ruun Time: {:.5f}s'.format(te-ts))
