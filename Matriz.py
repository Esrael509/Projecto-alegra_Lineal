class Matriz:
    def __init__(self, fil: int, col: int)-> None:
        self.fil: int = fil
        self.col: int = col
        # Inicializar la matriz con ceros
        self.mat: int = []
        for x in range(fil):
            filas = [0] * col
            self.mat.append(filas)
    
    def getFil(self)-> int:#obtener número de filas
        return self.fil
    
    def getCol(self)-> int:#obtener número de columnas
        return self.col
    
    def llenaMat(self)-> None:#llenar toda la matriz
        for x in range(self.fil):
            for y in range(self.col):
                self.mat[x][y] = int(input("Valor: "))
    
    def mostrar(self)-> None:#Mostrar la matriz
        for x in range(self.fil):
            for y in range(self.col):
                print(self.mat[x][y],end="  ")
            print("")
        print("")
    
    def simetrica(self)-> bool:#determina si la matriz es simétrica
        aux: bool
        if self.col == self.fil:
            for x in range(self.fil):
                for y in range(self.col):
                    if self.mat[x][y] == self.mat[y][x]:
                        aux = True
                    else:
                        aux = False
                        break
        else:
            aux = False
        return aux
                    
                
    
    @staticmethod
    def trianSup(M):
        Mat = Matriz(M.getFil(), M.getCol())
        if Mat.getFil() == Mat.getCol():
            for x in range(M.getFil()):
                for y in range(M.getCol()):
                    if y < x:
                        Mat.mat[x][y] = 0
                    else:
                        Mat.mat[x][y] = M.mat[x][y]
            return Mat
        else:
            print("\nNo se puede obtener el triangular superior")
            return None
    
    
    
    @staticmethod
    def trianInf(M):
        Mat = Matriz(M.getFil(), M.getCol())
        if Mat.getFil() == Mat.getCol():
            for x in range(M.getFil()):
                for y in range(M.getCol()):
                    if y > x:
                        Mat.mat[x][y] = 0
                    else:
                        Mat.mat[x][y] = M.mat[x][y]
            return Mat
        else:
            print("\nNo se puede obtener el triangular inferior")
            return None
    
    @staticmethod
    def diago(M):
        Mat = Matriz(M.getFil(), M.getCol())
        if Mat.getFil() == Mat.getCol():
            for x in range(Mat.getFil()):
                for y in range(Mat.getCol()):
                    Mat.mat[x][y] = M.mat[x][y]
            Mat = Matriz.trianInf(Mat)
            Mat = Matriz.trianSup(Mat)
            return Mat
        else:
            print("\nNo se puede obtener la diagonal")
            return None
    
    @staticmethod
    def iden(M):
        Mat = Matriz(M.getFil(), M.getCol())
        if Mat.getFil() == Mat.getCol():
            for x in range(Mat.getFil()):
                for y in range(Mat.getCol()):
                    Mat.mat[x][y] = 1 if x == y else 0
            return Mat
        else:
            print("La matriz no es cuadrada")
            return None
        
    
    @staticmethod
    def matrizT(M):
        Mat = Matriz(M.getCol(),M.getFil())
        for x in range(M.getFil()):
            for y in range(M.getCol()):
                Mat.mat[y][x] = M.mat[x][y]
        return Mat
    
    @staticmethod
    def sumaMat(M1, M2):
        Mz: Matriz
        if M1.getCol() == M2.getCol() and M1.getFil() == M2.getFil():
            Mz = Matriz(M1.getFil(), M1.getCol())
            for x in range(M1.getFil()):
                for y in range(M1.getCol()):
                    Mz.mat[x][y] = M1.mat[x][y] + M2.mat[x][y]
            return Mz
        else:
            print("\nLas matrices no se pueden sumar")
            return None
    
    @staticmethod
    def restaMat(M1, M2):
        Mz: Matriz
        if M1.getCol() == M2.getCol() and M1.getFil() == M2.getFil():
            Mz = Matriz(M1.getFil(), M1.getCol())
            for x in range(M1.getFil()):
                for y in range(M1.getCol()):
                    Mz.mat[x][y] = M1.mat[x][y] - M2.mat[x][y]
            return Mz
        else:
            print("\n Las matrices no se pueden restar")
            return None
    
    @staticmethod
    def productoM(M1,M2):
        Mz: Matriz
        if M1.getCol() == M2.getFil():
            Mz = Matriz(M1.getFil(), M2.getCol())
            for x in range(M1.getFil()):
                for y in range(M2.getCol()):
                    for z in range(M1.getCol()):
                        Mz.mat[x][y] += M1.mat[x][z] * M2.mat[z][y]
            return Mz
        else:
            print("\nLas matrices no se pueden multiplicar")
            return None