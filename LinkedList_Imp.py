class Node:
    def __init__(self,value):
        self.value=value,
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node

    def append(self,value):
        append_node=Node(value)
        self.tail.next=append_node
        self.tail=append_node

    def prepend(self,value):
        prepend_node=Node(value)
        prepend_node.next=self.head
        self.head=prepend_node

    def insert(self,value,index):
        if index==0:
            self.prepend(value)
        insert_node=Node(value)
        cur=self.head
        i=0
        while(cur!=None):
            if i==index-1:
                insert_node.next=cur.next
                cur.next=insert_node

            i+=1
            cur=cur.next

    def delete(self,index):
        i=0                                                                                                                                                                                                     
        cur=self.head
        if index==0:
            self.head=cur.next
            cur.next=None
        while(cur!=None):
            if i==index-1:
                cur1=cur.next
                cur.next=cur1.next
                cur1.next=None
            i+=1
            cur=cur.next

    def print_list(self):
        cur=self.head
        while(cur!=None):
            print(cur.value)
            cur=cur.next


ll=LinkedList(5)
ll.append(6)
ll.prepend(4)
ll.print_list()
print("-------")
ll.insert(9,0)
ll.print_list()
print("-------")
ll.delete(1)
ll.print_list()
print("-------")
