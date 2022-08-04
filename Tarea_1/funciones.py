
#se define el primer método el cual recibe 3 entradas
def basic_operations(Op1, Op2, Op):
    #la funcion isinstance() verifica que los parametros de entrada sean del typo int()
    if isinstance(Op1, int) & isinstance(Op2, int) & isinstance(Op, int):
        # si parametro de operación es 1 devuelve la suma de los 2 operandos
        if Op == 1: 
            return Op1 + Op2
        # si parametro de operación es 2 devuelve la resta de los 2 operandos
        elif Op == 2:
            return Op1 - Op2
        # si parametro de operación es 3 devuelve la división de los 2 operandos
        elif Op == 3:
            #en este punto, se verifica no sea igual a 0, ya que de ser así, tiraría el error 3312. caso contrario devuelve el resultado de la division 
            if Op2 == 0:
                return 3312
            else:
                return Op1/Op2
        #en caso que la entrada de la operacion no se encuentre dentro del rango de números permitidos, esto se refleja como el error 777    
        else:
            return 777
    # en caso que los parametros de la funcion "basic_operations" no sean del tipo int(), devuelve el error  420
    else:
        return 420

#se define la funcion count_char() la cual recibe un string como entrada
def count_char(word):
    #se verifica que la entrada sea un string y de ser así, la función devuelve la cantidad de caracteres de la entrada por medio del metodo len()
    if isinstance(word, str):
        return len(word)
    #si el parametro de entrada no es un string, devuleve el error 1314
    else:
        return 1314
