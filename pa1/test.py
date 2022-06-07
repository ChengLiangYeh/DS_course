from struct import node, stack, queue

#導入input.txt到struct裡面，stack、queue 2選1 
#test = queue()
test = queue()
struct ='queue'

f = open('./input.txt','r')
input = f.readlines()
#print(input[0]) #-> PUSH 10
#print(len(input)) #-> 25 (index:0~24)
for i in range(len(input)):
    word = input[i]
    #print('word=',word)
    #print(word[1])
    #print(type(word[5:]))
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