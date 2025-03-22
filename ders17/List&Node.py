class Node:
    val:int
    nextNode:"Node" = None

class Liste:
    rootNode:Node = None

    def __init__(self,val:int):
        tempNode=Node()
        tempNode.val=val
        self.rootNode=tempNode

    def add(self, val:int):
        tempNode=Node()
        tempNode.val=val
        # sora sora sonraki nodea git
        # sonraki nodu none diyene yeni nodu ekle 
        currentNode=self.rootNode

        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode #bi adım ileri yürüdün

        currentNode.nextNode = tempNode

    def printAll(self):
        currentNode=self.rootNode
        while currentNode is not None:
            print(currentNode.val)
            currentNode=currentNode.nextNode

    def pop(self):
        currentNode=self.rootNode
        lastVisitedNode=None

        while currentNode.nextNode is not None:
            lastVisitedNode=currentNode
            currentNode=currentNode.nextNode

        print(f"sondan önceki node {lastVisitedNode.val}")
        lastVisitedNode.nextNode=None

    

if __name__=="__main__":
    testList=Liste(0)

    for i in range(5):
        testList.add(val=i+1)

    testList.printAll()
    print("sonu sildim")
    testList.pop()
    testList.printAll()
    print("sonu sildim")
    testList.pop()
    testList.printAll()
         
        
