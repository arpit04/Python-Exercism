class Matrix:
    
    def row(X,Y):
        for i in range(len(X)):
            
            for j in range(len(X[0])):
                X[i][j]
                
        print("Row Matrix")
        
        for r in X:
            print(r)

    def column(X,Y):
        for i in range(len(X)):
            
            for j in range(len(X[0])):
                Y[j][i] = X[i][j]
                
        print("Column Matrix")
        
        for r in Y:
            print(r)
    
if __name__ == "__main__": 

    X = [[6, 7, 9]
        ,[4, 5, 1]
        ,[3, 8, 2]]
    
    Y = [[0, 0, 0]
        ,[0, 0, 0]
        ,[0, 0, 0]]
    
    #object of class
    obj = Matrix
    
    #function call
    obj.row(X,Y)
    obj.column(X,Y)



