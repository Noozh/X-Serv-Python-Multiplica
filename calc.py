#!/usr/bin/python3

import operator as op
import sys

def main(op1,op2):
    dicc = {'suma':op.add,'resta':op.sub,'multiplica':op.mul, 'divide':op.truediv}
    try:
        print(dicc[sys.argv[1]](op1, op2))
    except ZeroDivisionError:
        print("Se dividio por 0")


if __name__ == "__main__":
    if len(sys.argv) > 4:
        sys.exit("Uso: ./calculadora.py funcion op1 op2")
    try:
        op1 = float(sys.argv[2])
        op2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Alguno de los operandos es erroneo")
    main(op1,op2)
