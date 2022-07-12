#Function defined to do a binary search recursively for an element in a list and determine whether element is present in list or not
def binary_search(list,first,last,element):
    if last < first:
        return False
    else:
        mid = (first+last)//2
        if list[mid] == element:
            return True
        elif element < list[mid]:
            return binary_search(list,first,mid-1,element)
        else:
            return binary_search(list,mid+1,last,element)

#Class defined to encapsulate the secret word and interpret the user's input
class Secret:
    def __init__(self,word):
        self.word = word
        self.w_list = list(self.word)

    def output(self,input):      #Function which will read the user's input and give an output according to correct letters' position.
        output = ''
        for i in range (0,len(input)):
            if input[i] == self.w_list[i]:
                output += '2'
            elif input[i] in self.w_list:
                output += '1'
            else:
                output += '0'
        return output

    def output_2(self,input,prev_input,prev_ouput):   #Function which will tell whether the user input is a valid input keeping in mind the user input initially
        l_input = list(input)
        for i in range (0,len(prev_ouput)):
            if prev_ouput[i] == '2':
                if input[i] != prev_input[i]:
                    return 'Not a Valid Attempt!'
            if prev_ouput[i] == '1':
                if prev_input[i] in l_input:
                    continue
                else:
                    return 'Not a Valid Attempt!'
        return True

#Class defined to store the dictionary of words.
class Dictionary:
    def __init__(self,list):
        list.sort()
        self.words = list
    def valid_attempt(self,input):    #Function which will check whether every user input is a word in dictionary or not.
        return binary_search(self.words,0,len(self.words),input)

with open('words.txt') as f:
    lines = f.read().split('\n') # read all lines into a list of strings

dictionary = Dictionary(lines)
n = len(dictionary.words)
import random
number = random.randrange(n)
secret = Secret(dictionary.words[number])

for i in range (1,7):
    print('Enter Attempt',i)
    input_w = str(input())
    if dictionary.valid_attempt(input_w) is False:
        print('Not a Valid Attempt')
        continue
    else:
        if i == 1:
            if secret.output(input_w) == '22222':
                print('YOU WIN')
                break
            else:
                print(secret.output(input_w))
                prev_input = input_w
                prev_output = secret.output(input_w)
        else:
            if secret.output_2(input_w,prev_input,prev_output) is True:
                if secret.output(input_w) == '22222':
                    print('YOU WIN!')
                    break
                else:
                    if i == 6:
                        print('YOU LOSE','and the word was',secret.word)
                    else:
                        print(secret.output(input_w))
                        prev_input = input_w
                        prev_output = secret.output(input_w)
            else:
                if i == 6:
                        print('YOU LOSE','and the word was',secret.word)
                else:
                    print('Not a Valid Attempt')
                    continue
