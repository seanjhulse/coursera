""" 

Tree Class:
	List of nodes

Node Struct:
	Contains data member
	Contains a left, right node

"""

import random

class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class Tree(object):
	def __init__(self):
		self.root = None

	def generate_tree(self, size=0, left_range=None, right_range=None):
		if size == 0:
			print "Size of tree must be specified"
			return
		else:
			# specify left and right ranges if they are not provided
			if left_range is None:
				left_range = 0
			if right_range is None:
				right_range = 100 

			# iterate from 0 to 'size' to create Tree with random nodes
			for x in range(size):
				node = Node(random.randint(left_range, right_range))

				if self.root is None:
					self.root = node
				else:
					dummy = self.root

					while dummy is not None:
						prev = dummy
						if dummy.data > node.data:
							dummy = dummy.right
						else: 
							dummy = dummy.left


					if prev.data > node.data:
						prev.right = node
					else: 
						prev.left = node
					
	def _preorder(self, node):
		"""
		Helper function to print the tree nodes in Pre-Order.
		@return None
		"""

		print node.data
	 
		if node.left != None:
			self._preorder(node.left)
	 
		if node.right != None:
			self._preorder(node.right)

	def preorder(self, node=None):
		"""
		Pre-Order print the nodes in the Tree. Traverses from root by default.
		@param {Object} self
		@param {Object} node traverses from any node
		@return None
		"""

		if node is None:
			node = self.root

		self._preorder(node)

help(Tree)
