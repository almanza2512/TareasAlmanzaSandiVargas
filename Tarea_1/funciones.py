

def basic_operations(Op1, Op2, Op):
    #la funcion isinstance() verifica que los parametros de entrada sean del typo int()
    if isinstance(Op1, int) & isinstance(Op2, int) & isinstance(Op, int):
        if Op == 1:
            return Op1 + Op2
        elif Op == 2:
            return Op1 - Op2
        elif Op == 3:
            #verifica que el opreando 2 no sea 0
            if Op2 == 0:
                return 3312
            else:
                return Op1/Op2
        else:
            return 777
    else:
        return 420


def count_char(word):
    if isinstance(word, str):
        return len(word)
    else:
        return 1314
