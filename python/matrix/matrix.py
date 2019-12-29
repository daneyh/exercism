class Matrix:
    def __init__(self, matrix_string):
        self.matrixList = matrix_string.splitlines()

    def row(self, index):
        intMatrix = []
        for x in self.matrixList[index-1].split():
            x = int(x)
            intMatrix.append(x)
        return intMatrix
        


    def column(self, index):
        intMatrix = []
        for x in self.matrixList:
            intMatrix.append(x.split())
        return [[int(row[i]) for row in intMatrix] for i in range(len(intMatrix[0]))][index-1]

#matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
