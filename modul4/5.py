class node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def cariLinkedList(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next != None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print ("Data ", dicari, "ada dalam linked list")
                    break
            elif curNode.next == None:
                print ("Data ", dicari, "tidak ada dalam linked list")
                break

a = node(13)
menu = a
a.next = node(20)
a = a.next
a.next = node(60)
a = a.next
a.next = node(70)



