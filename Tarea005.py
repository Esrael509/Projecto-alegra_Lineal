from Matriz import Matriz

def main()-> None:
    fil: int
    col: int
    alfa: int
    op: int = 1
    M1: Matriz = None
    M2: Matriz = None
    M3: Matriz = None
    
    while op > 0 and op <= 11:
        print("\tOperaciones con matrices\n"
              "0)Matriz nula\n"
              "1)Suma\n"
              "2)Resta\n"
              "3)Producto\n"
              "4)Matriz Triangular Superior\n"
              "5)Matriz Triangular Inferior\n"
              "6)Matriz Diagonal\n"
              "7)Matriz Identidad\n"
              "8)Matriz Transpuesta\n"
              "9)Determinar si una matriz es simétrica\n"
              "10)Producto escalar\n"
              "11)Matriz opuesta\n"
              "12)Salir\n")
        op = int(input("Opcion: "))
        
        if op < 0 or op > 11: break

        if op:
            if M1 == None:
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M1 = Matriz(fil, col)
                M1.llenaMat()
        
        match op:
            case 0:
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M1 = Matriz(fil, col)
                print("\tMatriz:")
                M1.mostrar()
            case 1:
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M2 = Matriz(fil, col)
                M2.llenaMat()
                print("\tMatriz 1:")
                M1.mostrar()
                print("\tMatriz 2:")
                M2.mostrar()
                print("\tSuma de matrices:")
                M3 = Matriz.sumaMat(M1, M2)
                    
            case 2:
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M1 = Matriz(fil, col)
                M1.llenaMat()
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M2 = Matriz(fil, col)
                M2.llenaMat()
                print("\tMatriz 1:")
                M1.mostrar()
                print("\tMatriz 2:")
                M2.mostrar()
                print("\tResta de matrices:")
                M3 = Matriz.restaMat(M1, M2)
                    
            case 3:
                fil = int(input("Filas: "))
                col = int(input("Columnas: "))
                M2 = Matriz(fil, col)
                M2.llenaMat()
                print("\tMatriz 1:")
                M1.mostrar()
                print("\tMatriz 2:")
                M2.mostrar()
                print("\tProducto de matrices:")
                M3 = Matriz.productoM(M1, M2)
            
            case 4:
                print("Matriz:")
                if M1 != None: M1.mostrar()
                print("\tTriangular superior:")
                M3 = Matriz.trianSup(M1)
            
            case 5:
                print("Matriz:")
                if M1 != None: M1.mostrar()
                print("\tTriangular inferior:")
                M3 = Matriz.trianInf(M1)
                    
            case 6:
                print("Matriz:")
                if M1 != None: M1.mostrar()
                print("\tDiagonal:")
                M3 = Matriz.diago(M1)
                    
            case 7:
                if M1 != None: M1.mostrar()
                print("\tMatriz identidad:")
                M3 = Matriz.iden(M1)
            
            case 8:
                print("\tMatriz:")
                if M1 != None: M1.mostrar()
                print("\tMatriz transpuesta")
                M3 = Matriz.matrizT(M1)
            
            case 9:
                print("\tMatriz:")
                if M1 != None: M1.mostrar()
                if M1.simetrica():
                    print("La matriz es simetrica")
                else:
                    print("La matriz no es simétrica")

            case 10:
                alfa = int(input("Valor de alfa: "))
                print("\tProducto escalar de ",alfa,":")
                M1.pEscalar(alfa)
                M1.mostrar()

            case 11:
                M3 = Matriz.opuesta(M1)
                print("\tMatriz:")
                if M1 != None: M1.mostrar()
                print("\tMatriz opuesta:")
            
        if M3 != None:
            M3.mostrar()
            
        op = int(input("1 para continuar. 0 para salir: "))      
    
main()