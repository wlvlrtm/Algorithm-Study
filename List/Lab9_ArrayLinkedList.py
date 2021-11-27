from __future__ import annotations
from typing import Any, Type
from enum import Enum


Null = -1

class Node :
    """ Node Class for Array Linked List """

    def __init__(self, data = Null, next = Null, dnext = Null) :
        self.data = data    ## data
        self.next = next    ## next pointer of List
        self.dnext = dnext  ## next pointer of Free List


class ArrayLinkedList :
    """ Array Linked List """

    def __init__(self, capacity: int) :
        self.head = Null                    ## Head Node
        self.current = Null                 ## Current Node
        self.max = Null                     ## Using Tail Record
        self.deleted = Null                 ## Head Node of Free List
        self.capacity = capacity            ## Size of List
        self.n = [Node()] * self.capacity   ## Body of List
        self.no = 0                         ## Len of List


    def __len__(self) -> int :
        """ Return the Len of List """

        return self.no


    def get_insert_index(self) :
        """ Find the Next index of Record for insert """

        if (self.deleted == Null) :
            if (self.max + 1 < self.capacity) :
                self.max += 1
                return self.max     ## Use a new Record
            else :
                return Null         ## Out Of Size
        else :
            rec = self.deleted
            self.deleted = self.n[rec].dnext    ## Take the First rec to the Free List
            return rec


    def delete_index(self, idx: int) -> None :
        """ Sign the idx Record at the Free List """

        if (self.deleted == Null) :
            self.deleted = idx
            self.n[idx].dnext = Null    ## Sign the idx at the First of Free List
        else :
            rec = self.deleted
            self.deleted = idx          ## Input the idx at the First of Free List
            self.n[idx].dnext = rec


    def search(self, data: Any) -> int :
        """ Search data """

        cnt = 0
        ptr = self.head

        while (ptr != Null) :
            if (self.n[ptr].data == data) :
                self.current = ptr
                return cnt          ## Search Complite

            cnt += 1
            ptr = self.n[ptr].next
        return Null                 ## Search Failed


    def __contains__(self, data: Any) -> bool :
        """ Check of List has a data """

        return self.search(data) >= 0


    def add_first(self, data: Any) :
        """ Input data in the Head Node """

        ptr = self.head     ## Head Node; Before add
        rec = self.get_insert_index()

        if (rec != Null) :
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1


    def add_last(self, data: Any) -> None :
        """ Input data in the Tail Node """

        if (self.head == Null) :
            self.add_first(data)
        else :
            ptr = self.head
            
            while (self.n[ptr].next != Null) :
                ptr = self.n[ptr].next

            rec = self.get_insert_index()


            if (rec != Null) :
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1


    def remove_first(self) -> None :
        """ Remove Head Node """

        if (self.head != Null) :
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1


    def remove_last(self) -> None :
        """ Remove Tail Node """

        if (self.head != Null) :
            if (self.n[self.head].next == Null) :
                self.remove_first()

            else :
                ptr = self.head
                pre = self.head

                while (self.n[ptr].next != Null) :
                    pre = ptr
                    ptr = self.n[ptr].next

                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre

                self.no -= 1


    def remove(self, p: int) -> None :
        """ Remove Record p """

        if (self.head != Null) :
            if (p == self.head) :
                self.remove_first()
            else :
                ptr = self.head


                while (self.n[ptr].next != p) :
                    ptr = self.n[ptr].next

                    if (ptr == Null) :
                        return

                self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1



    def remove_current_node(self) -> None :
        """ Remove Current Node """

        self.remove(self.current)


    def clear(self) -> None :
        """ Remove All Nodes """

        while (self.head != Null) :
            self.remove_first()

        self.current = Null

    
    def next(self) -> bool :
        """ Move the Current Node to the next """
        
        if (self.current == Null or self.n[self.current].next == Null) :
            return False

        self.current = self.n[self.current].next

        return True


    def print_current_node(self) -> None :
        """ Print the Current Node """

        if (self.current == Null) :
            print("Search Failed")

        else :
            print(self.n[self.current].data)


    def print(self) -> None :
        """ Print ALL """

        ptr = self.head

        while (ptr != Null) :
            print(self.n[ptr].data)
            ptr = self.n[ptr].next


    def dump(self) -> None :
        """ List Dump """

        for i in self.n :
            print(f"[{i}] {i.data} {i.next} {i.dnext}")


    def __iter__(self) -> ArrayLinkedListIterator :
        """ Return Iterator """

        return ArrayLinkedListIterator(self.n, self.head)



class ArrayLinkedListIterator :
    """ Iterator Class of Array Linked List """

    def __init__(self, n: int, head: int) :
        self.n = n
        self.current = head


    def __iter__(self) -> ArrayLinkedListIterator :
        return self


    def __next__(self) -> Any :
        if (self.current == Null) :
            raise StopIteration
        else :
            data = self.n[self.current].data
            self.current = self.n[self.current].next

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

    lst = ArrayLinkedList(100)

    while True :
        menu = select_Menu()

        if (menu == Menu.InputHead) :
            lst.add_first(int(input("Input Num(Head): ")))

        elif (menu == Menu.InputTail) :
            lst.add_last(int(input("Input Num(Tail): ")))

        elif (menu == Menu.RemoveHead) :
            lst.remove_first()

        elif (menu == Menu.RemoveTail) :
            lst.remove_last()

        elif (menu == Menu.PrintCurrent) :
            lst.print_current_node()

        elif (menu == Menu.MoveCurrent) :
            lst.next()

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

        elif (menu == Menu.Scan) :
            for i in lst :
                print(i)

        else :
            break