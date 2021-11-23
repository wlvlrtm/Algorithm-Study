from __future__ import annotations
from typing import Any, Type
from enum import Enum


class Node :
    """ Node for Linked List """
    
    def __init__(self, data: Any = None, next: Node = None) :
        """ Initializing """
        
        self.data = data    ## Data Field
        self.next = next    ## Link Field



class LinkedList :
    """ Linked List """

    def __init__(self) -> None :
        """ Initializing """

        self.ln = 0             ## Count of Nodes; Len of List
        self.head = None        ## Head Node
        self.current = None     ## Current Node


    def __len__(self) -> int :
        """ Return the Count of Nodes; Len of List """
        
        return self.ln


    def search(self, data: Any) -> int :
        """ Search for Node with the same Va. as the data Filed """

        cnt = 0             ## Counter; (True: >=0) (False: -1)
        ptr = self.head     ## Pointer
        
        while (ptr is not None) :   ## If, Head is NOT None
            ## Searched ##
            if (ptr.data == data) : 
                self.current = ptr
                return cnt
            ## END Searched END ##
            
            ## Searching ##
            cnt += 1
            ptr = ptr.next
            ## END Searching END ##

        return -1   ## Search Fail


    def __contains__(self, data: Any) -> bool :
        """ Check for Linked List has data """

        return self.search(data) >= 0


    def add_First(self, data: Any) -> None :
        """ Add a new node at the Head """

        ptr = self.head                                 ## Pointer; Initial = Head Node
        self.head = self.current = Node(data, ptr)      ## Head -> new Node
        self.ln += 1                                    ## Len of List += 1
    

    def add_Last(self, data: Any) -> None :
        """ Add a new node at the End """

        if (self.head is None) :    ## If List is EMPTY
            self.add_First(data)    ## Add a new Node; Head
        else :
            ptr = self.head
            
            while (ptr.next is not None) :              ## IF, ptr is NOT a Last Node
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)  ## Add a new Node; Tail


    def remove_First(self) -> None :
        """ Remove the First Node """

        if (self.head is not None) :                    ## If, List is NOT Empty
            self.head = self.head.next = self.current   ## head -> head.next
        self.ln -= 1


    def remove_Last(self) -> None :
        """ Remove the Last Node """

        if (self.head.next is None) :    ## If, Len of List is JUST '1' 
            self.remove_First()          ## Remove the Head Node
        else : 
            ptr = self.head

            while (ptr.next is not None) :  ## If, ptr is NOT Last Node
                pre = ptr
                ptr = ptr.next

            ## IF, ptr is Last Node
            pre.next = None
            self.current = pre
            self.ln -= 1


    def remove(self, p: Node) -> None :
        """ Node p Del """

        if (self.head is not None) :
            if (p is self.head) :
                self.remove_First()
            else :
                ptr = self.head
                
                while (ptr.next is not p) :
                    ptr = ptr.next
                    if (ptr is None) :  ## p node Search Failed
                        return

                ptr.next = p.next
                self.current = ptr
                self.no -= 1


    def remove_current(self) -> None :
        """ Remove the Current Node """

        self.remove(self.current)


    def clear(self) -> None :
        """ Remove ALL """

        while (self.head is not None) :
            self.remove_First()       ## Remove Head Node

        self.current = None
        self.ln = 0


    def next(self) -> bool :
        """ Move the current Node to the next place """

        if (self.current is None or slef.current.next is None) :    ## CANNOT move
            return False

        self.current = self.current.next
        return True


    def print_current(self) -> None :
        """ Print the Current Node """

        if (self.current is None) :
            print("Current Node is None")
        else :
            print(self.current.data)


    def print_all(self) -> None :
        """ Print the List; ALL """

        ptr = self.head

        while (ptr is not None) :
            print(ptr.data)
            ptr = ptr.next


    def __iter__(self) -> LinkedListIterator :
        """ Return the Iterator """

        return LinkedListIterator(self.head)



class LinkedListIterator :
    """ Iterator Class for LinkedList Class """

    def __init__(self, head: Node) :
        self.current = head


    def __iter__(self) -> LinkedListIterator :
        return self


    def __next__(self) -> Any :
        if (self.current is None) :
            raise StopIteration
        else :
            data = self.current.data
            self.current = self.current.next
            return data



if __name__ == "__main__" :
    Menu = Enum("Menu", ["InputHead", "InputTail", "RemoveHead", "RemoveTail", "PrintCurrent", "MoveCurrent", "RemoveCurrent", "RemoveALL", "Search", "CheckMembership", "PrintAll", "Scan", "End"])


    def select_Menu() -> Menu :
        """ Select Menu """

        s = [f"({m.value}){m.name}" for m in Menu]

        while True :
            print(*s, sep = " ", end="")
            n = int(input(": "))

            if (1 <= n <= len(Menu)) :
                return Menu(n)

    lst = LinkedList()

    while True :
        menu = select_Menu()

        if (menu == Menu.InputHead) :
            lst.add_First(int(input("Input Num(Head): ")))

        elif (menu == Menu.InputTail) :
            lst.add_Last(int(input("Input Num(Tail): ")))

        elif (menu == Menu.RemoveHead) :
            lst.remove_First()

        elif (menu == Menu.RemoveTail) :
            lst.remove_Last()

        elif (menu == Menu.PrintCurrent) :
            lst.print_current()

        elif (menu == Menu.MoveCurrent) :
            lst.next()

        elif (menu == Menu.RemoveCurrent) :
            lst.remove_current()

        elif (menu == Menu.RemoveALL) :
            lst.clear()

        elif (menu == Menu.Search) :
            pos = lst.search(int(input("Input num(Search): ")))

            if (pos >= 0) :
                print(f"Data index: {pos+1}")
            else :
                print(f"Search Failed")

        elif (menu == Menu.CheckMembership) :
            print("The data for that value is " + "included." if int(input("Input Num(CheckMembership): ")) in lst else "NOT included.")

        elif (menu == Menu.PrintAll) :
            lst.print_all()

        elif (menu == Menu.Scan) :
            for i in lst :
                print(i)

        else :
            break