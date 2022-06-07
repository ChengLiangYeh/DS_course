import argparse

class hash_table():
    # TODO
    def __init__(self):
        self.slot = [[] for _ in range(1001)]

    def hash_function(self, input_str):
        #將string轉換成key:
        key = 0
        numbers = len(input_str)
        d = {'a':1, 'A':1, 'b':2, 'B':2, 'c':3, 'C':3, 'd':4, 'D':4, 'e':5, 'E':5, 'f':6, 'F':6, 'g':7, 'G':7, 'h':8, 'H':8, 'i':9, 'I':9, 
            'j':10, 'J':10, 'k':11, 'K':11, 'l':12, 'L':12, 'm':13, 'M':13, 'n':14, 'N':14, 'o':15, 'O':15, 'p':16, 'P':16, 'q':17, 'Q':17, 
            'r':18, 'R':18, 's':19, 'S':19, 't':20, 'T':20, 'u':21, 'U':21, 'v':22, 'V':23, 'w':23, 'W':23, 'x':24, 'X':24, 'y':25, 'Y':25, 
            'z':26, 'Z':26}
        for i in range(len(input_str)):
            #print('i=',i)
            #print('d=',d[ (input_str[i])])
            #print((27**(i+((len(input_str))-(i+1)))))
            
            temp = (d[ (input_str[i]) ]) * (27**(((len(input_str))-(i+1))))
            #print(temp)
            key = key + temp

        slot_location = key % 1001
        return key, slot_location 

    def Insert(self,input_str):
        #print('input_str=',input_str)
        key, slot_location = self.hash_function(input_str)
        #print(key, slot_location)
        self.slot[slot_location].insert(0,input_str)
        
    def Look(self, slot_location, output):
        if (self.slot[slot_location]) == []:
            #print('Null')
            output.write('Null')
            #output.write('\n')
        for i in range(len(self.slot[slot_location])):
            #print((self.slot[slot_location])[i], end=' ')
            word = (self.slot[slot_location])[i]
            output.write(word)
            output.write(' ')
        #print('\n')
        output.write('\n')

    def Delete(self, input_str, output):
        key, slot_location = self.hash_function(input_str)
        #print(key, slot_location)
        find = False
        
        for i in range(len(self.slot[slot_location])):
            if ((self.slot[slot_location])[i]) == input_str:
                (self.slot[slot_location]).pop(i)
                find = True
                break
            else:
                find = False
        if find == False:
            #print('ERROR: Not in the hash table')
            output.write('Error')
            output.write('\n')
            
    def Search(self, input_str, output):
        key, slot_location = self.hash_function(input_str)
        find = False
        for i in range(len(self.slot[slot_location])):
            if ((self.slot[slot_location])[i]) == input_str:
                find = True
                break
            else:
                find = False
        if find == True:
            #print('Yes')
            output.write('Yes')
            output.write('\n')
        else:
            #print('NO')
            output.write('No')
            output.write('\n')
    
    def End(self, output):
        output.close()

        

def main(input_path, output_path):
    output = open(output_path, 'w')
    ###TO DO###
    table = hash_table()
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)
            operation = line.split(' ')[0]
            #print(operation)
            if operation == 'End':
                table.End(output)
                break

            if operation != 'End':
                input_str = (line.split(' ')[1])
                #print(input_str)
            if operation == 'Insert':
                table.Insert(input_str)
            if operation == 'Look':
                table.Look(int(input_str), output)
            if operation == 'Delete':
                table.Delete(input_str, output)
            if operation =='Search':
                table.Search(input_str, output)
    ###########
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

    main(args.input, args.output)
