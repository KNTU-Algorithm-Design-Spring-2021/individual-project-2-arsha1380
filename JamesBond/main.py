def createDictionary():
    temp = dict()
    f = open("words_alpha.txt", "r")
    myList = (f.read().split("\n"))
    for w in myList:
        temp[w] = True
    return temp

def valid(word):
    return word in myDictionary



def firstAlgorithm(sentence):
    word = sentence
    output = []
    while sentence != "" or word != "":
        word = sentence
        sentence = ""
        length = len(word)
        for _ in range(length):
            if valid(word):
                output.append(word)
                word = ""
                break
            else:
                sentence = word[length - 1] + sentence
                word = word[0:length - 1]
                length -= 1
            pass
    return output

# def secondAlgorithm(sentence):
#     output = []
#     length = len(sentence)
#     array = [[0]*length for _ in range(length)]
#     for i in range(length):
#         for j in range(i,length):
#             if valid(sentence[i:j+1]):
#                 array[i][j] = 1
#     for i in range(length):
#         for j in range(i, length):
#             print(array[i][j]," ",end="")
#         print()
#
#     for i in range(length):
#         if
#
#     return


sentence = input("Please enter your sentence:\n\t").lower()
myDictionary = createDictionary()

print("Your massage is: ",*firstAlgorithm(sentence))
# secondAlgorithm(sentence)
# print("output of Second algorithm: ",secondAlgorithm(sentence))