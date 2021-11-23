from __future__ import annotations
from typing import Any, Type
from enum import Enum



class Node :
    """ Node Class for Circular Double-Linked List """

    def __init__ (self, data: Any = None, prev: Node = None, next: Node = None) :
        self.data = data
        self.prev = prev or self
        self.next = next or self



class DoubleLinkedList :
    """ Circular Double-Linked List """

    def __init__(self) :
        self.head = self.current = Node()
        self.no = 0


    def __len__(self) -> int :
        """ Return the Len of List """

        return self.no


    def is_Empty(self) -> bool :
        """ IS List Empty? """

        return self.head.next is self.head


    def search(self, data: Any) -> Any :
        """ Seach the Same node as data """

        cnt = 0
        ptr = self.head.next

        while (ptr is not self.head) :
            if (data == ptr.data) :
                self.current = ptr
                return cnt
            
            cnt += 1
            ptr = ptr.next
        return -1


    def __contains__(self, data: Any) -> bool :
        """ Check if the list has the data """
        
        return self.search(data) >= 0


    def print_current_node(self) -> None :
        """ Print current Node """

        if (self.is_Empty()) :
            print("Search Faild")
        else :
            print(self.current.data)


    def print(self) -> None :
        """ Print ALL """

        ptr = self.head.next

        while (ptr is not self.head) :
            print(ptr.data)
            ptr = ptr.next


    def print_reverse(self) -> None :
        """ Print ALL; Reverse """

        ptr = self.head.prev
        
        while (ptr is not self.head) :
            print(ptr.data)
            ptr= tpr.prev


    def next(self) -> bool :
        """ Move the current to the next """
        
        if (self.is_Empty() or self.current.next is self.head) :
            return False

        self.currnet = self.current.next
        
        return True

    
    def prev(self) -> bool :
        """ Move the current to the prev """

        if (self.is_Empty() or self.current.prev is self.head) :
            return False

        self.current = sel.fcurrent.prev

        return True


    def add(self, data: Any) -> None :
        """ Add a new Node at the behind the current node """

        node = Node(data, self.current, self.current.next)
        
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1


    def add_first(self, data: Any) -> None :
        """ Add a new Node at the First """

        self.current = self.head
        self.add(data)


    def add_last(self, data: Any) -> None :
        """ Add a new Node at the Last """

        self.current = self.head.prev
        self.add(data)


    def remove_current_node(self) -> None :
        """ Remove the Current Node """

        if not (self.is_Empty()) :
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1

            if (self.current is self.head) :
                self.current = self.head.next


    def remove(self, p: Node) -> None :
        """ Remove Node p """

        ptr = self.head.next

        while (ptr is not self.head) :
            if (ptr is p) :
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next


    def remove_First(self) -> None :
        """ Remove Head Node """
        
        self.current = self.head.next
        self.remove_current_node()


    def remove_Last(self) -> None :
        """ Remove Tail Node """

        self.current = self.head.prev
        self.remove_current_node()


    def clear(self) -> None :
        """ Remove All """

        while not (self.is_Empty()) :
            self.remove_First()

        self.no = 0


    def __iter__(self) -> DoubleLinkedListIterator :
        """ Return Iterator """

        return DoubleLinkedListIterator(self.head)


    def __reversed__(self) -> DoubleLinkedListReverseIterator :
        """ Return Reverse Iterator """

        return DoubleLinkedListReverseIterator(self.head)



class DoubleLinkedListIterator :
    """ Iterator Class for Double Linked List """

    def __init__(self, head: Node) :
        self.head = head
        self.current = head.next


    def __iter__(self) -> DoubleLinkedListIterator :
        return self

    def __next__(self) -> Any :
        if (self.current is self.head) :
            raise StopIteration
        else :
            data = self.current.data
            self.current = self.current.next
            return data


class DoubleLinkedListReverseIterator :
    """ Iterator Class for Double Linked List; REVERSE """

    def __init__(self, head: Node) :
        self.head = head
        self.current = head.prev


    def __iter__(self) -> DoubleLinkedListIterator :
        return self

    def __next__(self) -> Any :
        if (self.current is self.head) :
            raise StopIteration
        else :
            data = self.current.data
            self.current = self.current.prev
            return data
    


if __name__ == "__main__" :
    Menu = Enum("Menu", ["InputHead", "InputTail", "RemoveHead", "RemoveTail", "PrintCurrent", "MoveCurrent", "MoveCurrentRe", "RemoveCurrent", "RemoveALL", "Search", "CheckMembership", "PrintAll", "PrintAllRe", "ScanAll", "ScanAllRe", "End"])

    def select_Menu() -> Menu :
        """ Select Menu """

        s = [f"({m.value}){m.name}" for m in Menu]

        while True :
            print(*s, sep = " ", end="")
            n = int(input(": "))

            if (1 <= n <= len(Menu)) :
                return Menu(n)

    lst = DoubleLinkedList()

    while True :
        menu = select_Menu()

        if (menu == Menu.InputHead) :
            lst.add_first(int(input("Input Num(Head): ")))

        elif (menu == Menu.InputTail) :
            lst.add_last(int(input("Input Num(Tail): ")))

        elif (menu == Menu.RemoveHead) :
            lst.remove_First()

        elif (menu == Menu.RemoveTail) :
            lst.remove_Last()

        elif (menu == Menu.PrintCurrent) :
            lst.print_current_node()

        elif (menu == Menu.MoveCurrent) :
            lst.next()

        elif (menu == Menu.MoveCurrentRe) :
            lst.prev()

        elif (menu == Menu.RemoveCurrent) :
            lst.remove_current_node()

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
            lst.print()

        elif (menu == Menu.PrintAllRe) :
            lst.print_reverse()

        elif (menu == Menu.ScanAll) :
            for i in lst :
                print(i)

        elif (menu == Menu.ScanAllRe) :
            for i in reversed(lst) :
                print(i)

        else :
            break