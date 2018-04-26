# python2

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
		self.nodes = []

class Tree(object):
	def __init__(self):
		self.root = None

	def generate_random_tree(self, size=0, left_range=None, right_range=None):
		"""
		Generates a Tree of any size
		@param {integer} left_range is the lower limit of random leaves built
		@param {integer} right_range is an upper limit of random leaves built
		@param {integer} size is the number of leaves, not the height of the Tree
		@returns None
		"""

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
				data = random.randint(left_range, right_range)

				self.add_node(data)


	def add_node(self, data, position=None):
		"""
		Adds a leaf to the Tree by finding the first empty leaf that is in the correct position
		as defined by the Tree structure above
		@params {integer} data
		@params {integer} position, must be specified
		@return None
		"""
		node = Node(data)

		if self.root is None:
			self.root = node
			return

		if position is None:
			print "Position must be specified"
			return

		dummy = self.root





					
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


	def build_tree(self, data=None):
		if data is None:
			print "No data available."
			return

		data_map = {}
		for index, dat in enumerate(data):
			if dat in data_map:
				data_map[dat].append(index)
			else:
				data_map[dat] = [index]

		self.get_height(data_map)


	def get_height(self, data_map):
		
		height = 1

		if -1 in data_map:
			start = -1
		else:
			start = 0

		print data_map

		while True:
			prev = start
			start_inner = start

			prev_height = 0
			curr_height = 0

			while True:
				prev_inner = start_inner

				for dat in data_map[start_inner]:
					if dat in data_map:
						start_inner = dat
						print dat

				if prev_inner == start_inner:
					break
						

			if prev == start:
				break


		return height

n = input()
data = [int(x) for x in raw_input().split()]
tree = Tree()
tree.build_tree(data)
