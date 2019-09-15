from classes import RN, ABR

def main():
    tree = ABR()
    tree.insert(4)
    tree.insert(5)

    for x in range(20, 10, -1):
        tree.insert(x)

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
