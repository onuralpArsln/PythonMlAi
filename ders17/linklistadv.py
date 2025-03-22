class Node:
    val:int
    nextNode:"Node" = None


if __name__ == "__main__":

    rootNode= Node()
    rootNode.val=0
    currentNode=rootNode


    for i in range(9):
        tempNode=Node()
        tempNode.val=i+1
        currentNode.nextNode=tempNode
        currentNode=tempNode

    currentNode=rootNode
    while currentNode is not None:
        print(currentNode.val)
        currentNode=currentNode.nextNode