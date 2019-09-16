from classes import RN, ABR
import numpy as np

def random_list(n):
    # Permutazione casuale dei primi n interi
    A = np.arange(n)
    np.random.shuffle(A)
    return A

def main():
    tree = ABR()
    tree.insert(4)
    tree.insert(5)

    A = random_list(100)
    for x in A:
        tree.insert(x)

    #for x in range(20, 10, -1):
     #   tree.insert(x)

    print(tree.find(5))
    print(tree.find(2))
    print(tree.findMax(tree.root))
    tree.inorder()

    treeRN = RN()
    treeRN.insert(5)
    treeRN.insert(4)

    #treeRN.insert(3)
   # treeRN.insert(1)
   # treeRN.insert(19)



    for x in range(20, 10, -1):
      treeRN.insert(x)


    print(treeRN.find(5))
    print(treeRN.find(2))
    print(treeRN.findMax(treeRN.root))
    treeRN.inorder()



if __name__ == "__main__":
        main()
