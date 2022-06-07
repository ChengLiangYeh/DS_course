import argparse
import time
import numpy as np

def pattern_match(text, pattern):
    # hint: Use dynamic programming to achieve O(T*P)
    DPchart = np.zeros( ( len(text)+1, len(pattern)+1 ) )
    DPchart[0][0] = True

    for j in range(1,len(pattern)+1):  #*在aa a*時出狀況 => DPchart第一排要小心
        if pattern[j-1] == '*':
            DPchart[0][j] = DPchart[0][j-2]

    for i in range(1,len(text)+1):
        #print(i)
        for j in range(1,len(pattern)+1):
            #print(j)
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                DPchart[i][j] = DPchart[i-1][j-1]
            elif pattern[j-1] == '*':
                DPchart[i][j] = DPchart[i][j-2]   #*出現0次的情況
                if text[i-1] == pattern[j-2] or pattern[j-2] == '.':  #*出現大於0次的情況
                    DPchart[i][j] = DPchart[i-1][j] or DPchart[i][j]  #判斷以上情形哪一種成立
            else:
                DPchart[i][j] = False
    shape = np.shape(DPchart)
    if DPchart[shape[0]-1][shape[1]-1] == 1:
        return True
    else:
        return False

def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip().split()
            text, pattern = line[0], line[1]
            if pattern_match(text, pattern):
                print('1', file=output)
            else:
                print('0', file=output)
    output.close()

if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input')
    parser.add_argument('--output', default='./output')
    args = parser.parse_args()

    ts = time.time()
    main(args.input, args.output)
    te = time.time()
    print('Run Time: {:.5f}s'.format(te-ts))

