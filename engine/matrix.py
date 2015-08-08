def maptoMatrix(f):
    matrix =[]
    linea = []
    orig = '../resources/maps/' + f 
    string = open(orig, 'r')
    
    for line in string.readlines():
        for a in line:
            if a != '\n':
                linea.append(a)
        matrix.append(linea)
        linea = []

    return matrix








			

	
