from classes import RN, ABR
import numpy as np
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(10000)

def random_list(n):
    # Permutazione casuale dei primi n interi
    A = np.arange(n)
    np.random.shuffle(A)
    return A

def main():
    tree = ABR()
    startInsert = timer()
    for x in range(0, 9990, 1):
        # print(x)
        tree.insert(x)
    endInsert = timer()
    t = endInsert - startInsert
    print("tempo inserimento ordinato %f" % t)

    treeA = ABR()
    A = random_list(9990)
    startInsertRandom = timer()
    for x in A:
        # print(x)
        treeA.insert(x)
    endInsertRandom = timer()
    t = endInsertRandom - startInsertRandom
    print("tempo inserimento random %f" % t)


    treeRNa = RN()
    startInsertRnOrdinato = timer()
    for x in range(0, 9990, 1):
      treeRNa.insert(x)
    endInsertRnOrdinato = timer()
    t = endInsertRnOrdinato - startInsertRnOrdinato
    print("tempo inserimento RN ordinato %f" % t)


    treeRNb = RN()
    A = random_list(9990)
    startInsertRnRandom= timer()
    for x in A:
        treeRNb.insert(x)
    endInsertRnRandom = timer()
    t = endInsertRnRandom - startInsertRnRandom
    print("tempo inserimento RN random %f" % t)





if __name__ == "__main__":
        main()
