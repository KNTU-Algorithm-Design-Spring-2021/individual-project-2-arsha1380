import math

def printSolution(p, n, temp):
    k = 0
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, (p[n] - 1), temp) + 1
    print('Line ', k, ":", end=" ")
    for i in range(p[n], n+1):
        print(temp[i-1],end=" ")
    print("\t",p[n],"to", n)

    return k


def solveWordWrap(myList, n, m, temp):

    extraSpace = [[0 for i in range(n + 1)] for i in range(n + 1)]

    costOfLine = [[0 for i in range(n + 1)] for i in range(n + 1)]

    totalCost = [0 for i in range(n + 1)]

    p = [0 for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(i , n + 1):
            if i == j:
                extraSpace[i][j] = m - myList[i - 1]
            else:
                extraSpace[i][j] = (extraSpace[i][j - 1] - myList[j - 1] - 1)

            if extraSpace[i][j] < 0:
                costOfLine[i][j] = math.inf
            elif j == n and extraSpace[i][j] >= 0:
                costOfLine[i][j] = 0
            else:
                costOfLine[i][j] = (extraSpace[i][j] * extraSpace[i][j])


    totalCost[0] = 0
    for j in range(1, n + 1):
        totalCost[j] = math.inf
        for i in range(1, j + 1):
            if (totalCost[i - 1] != math.inf and costOfLine[i][j] != math.inf and ((totalCost[i - 1] + costOfLine[i][j]) < totalCost[j])):
                totalCost[j] = totalCost[i-1] + costOfLine[i][j]
                p[j] = i
    printSolution(p, n, temp)



# Driver Code
temp = input("Please enter your paragraph:\n\t").split()
myList = []
for i in temp:
    myList.append(len(i))
n = len(myList)
m = int(input("Please enter line length: "))
while m < max(myList):
    m = int(input("Please enter bigger number(line length): "))
solveWordWrap(myList, n, m, temp)
