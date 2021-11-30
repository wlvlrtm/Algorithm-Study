from __future__ import annotations
from enum import Enum
from typing import Any, Type


class Node :
	""" Node of Binary Search Tree """

	def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None) :
		self.key = key			## key
		self.value = value		## value
		self.left = left		## Left Pointer
		self.right = right		## Right Pointer


class BinarySearchTree :
	""" Binary Search Tree """

	def __init__(self) :
		self.root = None


	def search(self, key: Any) -> Any :
		""" Find Node for key """

		p = self.root	## root Node
		
		while True :
			if (p is None) :		## Search Fail
				return None

			if (key == p.key) :		## Search Complite
				return p.value

			elif (key < p.key) :	## Move to the Left Node
				p = p.left

			else :					## Move to the Right Node
				p = p.right

	
	def add(self, key: Any, value: Any) -> bool :
		""" Node Add; key & value """

		def add_node(node: Node, key: Any, value: Any) -> None :
			""" Add a new Node to the Sub-Tree; Root = node, Key = key, Value = value """

			if (key == node.key) :
				return False

			elif (key < node.key) :
				if (node.left is None) :
					node.left = Node(key, value, None, None)
				
				else :
					add_node(node.left, key, value)

			else :
				if (node.right is None) :
					node.right = Node(key, value, None, None)

				else :
					add_node(node.right, key, value)
			
			return True
		
		if (self.root is None) :
			self.root = Node(key, value, None, None)
			return True
		
		else :
			return add_node(self.root, key, value)


	def remove(self, key: Any) -> bool :
		""" remove Node; Key = key """

		p = self.root			## Scanning Node
		parent = None			## Parent Node of Scanning Node
		is_left_child = True	## Check about is p left child node of parent node

		while True :
			if (p is None) :
				return False

			if (key == p.key) :
				break

			else :
				parent = p

				if (key < p.key) :
					is_left_child = True
					p = p.left
				else :
					is_left_child = False
					p = p.right

			if (p.left is None) :
				if (p is self.root) :
					self.root = p.right

				elif (is_left_child) :
					parent.left = p.right

				else :
					parent.right = p.right

			elif (p.right is None) :
				if (p is self.root) :
					self.root = p.left

				elif (is_left_child) :
					parent.left = p.left

				else :
					parent.right = p.left

			else :
				parent = p
				left = p.left
				is_left_child = True

				while (left.right is not None) :
					parent = left
					left = left.right
					is_left_child = False

				p.key = left.key
				p.value = left.value

				if (is_left_child) :
					parent.left = left.left

				else :
					parent.right = left.left

			return True


	def dump(self) -> None :
		""" DUMP; Print ascending all Nodes """

		def print_subtree(node: Node) :
			""" Print ascending all Sub-Tree's Nodes what have Root Node, 'node' """

			if (node is not None) :
				print_subtree(node.left)
				print(f'{node.key} {node.value}')
				print_subtree(node.right)

		print_subtree(self.root)


	def min_key(self) -> Any :
		""" Min Key return """

		if (self.root is None) :
			return None

		p = self.root

		while (p.left is not None) :
			p = p.left

		return p.key


	def max_key(self) -> Any :
		""" Max Key return """

		if (self.root is None) :
			return None

		p = self.root

		while (p.right is not None) :
			p = p.right

		return p.key


if __name__ == "__main__" :
	Menu = Enum("Menu", ["Input", "Delete", "Search", "Dump", "KeyRange", "Quit"])

	def select_Menu() -> Menu :
		s = [f'({m.value}){m.name}' for m in Menu]

		while (True) :
			print(*s, sep = "  ", end="")
			n = int(input(": "))

			if (1 <= n <= len(Menu)) :
				return Menu(n)

	tree = BinarySearchTree()

	while (True) :
		menu = select_Menu()

		if (menu == Menu.Input) :
			key = int(input("Input Key(Input): "))
			val = int(input("Input Val(Input): "))

			if not tree.add(key, val) :
				print("Add Fail")

		elif (menu == Menu.Delete) :
			key = int(input("Input Key(Del): "))
			tree.remove(key)

		elif (menu == Menu.Search) :
			key = int(input("Input Key(Search): "))
			t = tree.search(key)

			if (t is not None) :
				print(f"Num of key: {t}")

			else :
				print("Search Fail")

		elif (menu == Menu.Dump) :
			tree.dump()

		elif (menu == Menu.KeyRange) :
			print(f"Min Num: {tree.min_key()}")
			print(f"Max Num: {tree.max_key()}")

		else :
			break