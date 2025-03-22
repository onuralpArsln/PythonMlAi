class Node:
    val:int
    nextNode:"Node" = None

if __name__ == "__main__":
    firstNode=Node()
    firstNode.val=6

    secondNode=Node()
    secondNode.val=7

    thirdNode=Node()
    thirdNode.val=8

    firstNode.nextNode=secondNode
    secondNode.nextNode=thirdNode

    currentNode=firstNode

    while currentNode is not None:
        print(currentNode)
        print(currentNode.val)
        currentNode=currentNode.nextNode

    print("second node silmek")

    firstNode.nextNode=thirdNode

    currentNode=firstNode

    while currentNode is not None:
        print(currentNode.val)
        currentNode=currentNode.nextNode

    print("listede pop yapmak")

    
    firstNode.nextNode=secondNode
    secondNode.nextNode=thirdNode
    # pop() yaptık sonuncu silindi
    secondNode.nextNode=None

    
    currentNode=firstNode

    while currentNode is not None:
        print(currentNode.val)
        currentNode=currentNode.nextNode



