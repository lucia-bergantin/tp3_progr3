import math 

class Heap:
	def __init__(self):
		self.heap_list = []
		
	def __str__(self):
		return str(self.heap_list)
	
	def get_nb_level(self):
		return math.ceil(math.log(len(self.heap_list)+1,2))
	
	def get_values_from_level(self, level):
		return self.heap_list[2**(level-1)-1:2**(level-1)+(2**(level-1))-1]

	'''
	def __str__(self):  # Il manque la prise en compte du nombre de chiffres pour décaler en conséquence
		nb_level = self.get_nb_level()
		string_to_return = ""
		for i in range(1,nb_level+1):
			values_current_level = self.get_values_from_level(i)
			indent_cur_level = '\t' * ((2 ** (nb_level - i))-1)
			indent_between_values = '\t' * ((2 ** (nb_level - i + 1))-1)
			string_to_return += indent_cur_level
			for v in values_current_level :
				string_to_return += str(v) + indent_between_values
			string_to_return += '\n' #+ str(i+1)
					
		return '__________\n' + string_to_return[:-1] + '\n__________' 
		'''
		
		
		
	def get_left_child(self, index_current_node):
		index_left_child = index_current_node*2+1
		if((len(self.heap_list) - 1) > index_left_child):
			return index_left_child
		return None
			
	def get_right_child(self, index_current_node):
		index_right_child = index_current_node*2+2
		if(len(self.heap_list) - 1 > index_right_child):
			return index_right_child
		return None
			
	def get_parent(self, index_current_node):
		if index_current_node == 0 :
			return None
		return (index_current_node-1)//2
		
	def has_child(self, index_current_node):
		return len(self.heap_list) - 1 >= index_current_node*2+1
	
	def swap(self, index_node1, index_node2):
		_tmp = self.heap_list[index_node1]
		self.heap_list[index_node1] = self.heap_list[index_node2]
		self.heap_list[index_node2] = _tmp	
		
	def percolate_up(self, index_new_element):
		node_value = self.heap_list[index_new_element]
		if node_value == 0 :
			return
		index_parent = self.get_parent(index_new_element)
		node_parent_value = self.heap_list[index_parent]
		while index_new_element > 0 and node_value < node_parent_value :
			self.swap(index_parent, index_new_element)
			index_new_element = index_parent
			index_parent = self.get_parent(index_new_element)
			if index_parent is not None:
				node_parent_value = self.heap_list[index_parent]
			
	def percolate_down(self, index_new_element):
		node_value = self.heap_list[index_new_element]
		index_left_child = self.get_left_child(index_new_element)
		index_right_child = self.get_right_child(index_new_element)
		left_child_value = self.heap_list[index_left_child] if index_left_child is not None else math.inf 
		right_child_value = self.heap_list[index_right_child] if index_right_child is not None else math.inf 
		while self.has_child(index_new_element) and (node_value > left_child_value or node_value > right_child_value):
			if left_child_value < right_child_value :
				self.swap(index_left_child, index_new_element)
				index_new_element = index_left_child
			else:	
				self.swap(index_right_child, index_new_element)
				index_new_element = index_right_child

			index_left_child = self.get_left_child(index_new_element)
			index_right_child = self.get_right_child(index_new_element)
			left_child_value = self.heap_list[index_left_child] if index_left_child is not None else math.inf 
			right_child_value = self.heap_list[index_right_child] if index_right_child is not None else math.inf 

	def insert(self, new_element):
		self.heap_list.append(new_element)
		index_new_element = len(self.heap_list) - 1 
		if index_new_element > 0:
			self.percolate_up(index_new_element)
			
	def extract(self):
		node_max_priority = self.heap_list[0]
		self.heap_list[0] = self.heap_list.pop()
		
		if len(self.heap_list) > 0 :
			self.percolate_down(0)
		
		return node_max_priority
	
	def delete(self, index_node_to_delete):
		if index_node_to_delete == len(self.heap_list)-1:
			self.heap_list.pop()
			return
		self.heap_list[index_node_to_delete] = self.heap_list.pop()
		if len(self.heap_list) > 0 :
			self.percolate_down(index_node_to_delete)
			
	def build_v1(self, list_values): #version naive, complexité en O(n*log(n))
		self.heap_list = []
		for value in list_values:
			self.insert(value)	
	
	def build_v2(self, list_values): # Méthode proposée par Floyd en O(n)
		self.heap_list = list_values.copy() # au départ, on reprend la liste telle quelle, non triée.
		for i in range(math.floor(len(self.heap_list)/2)-1,-1,-1): # On parcout alors les noeuds de l'arbre qui ne sont pas des feuilles, de droite à gauche et en remontant
			self.percolate_down(i) # On replace au bon endroit chacun de ces éléments
		
		
if __name__ == '__main__':
	h = Heap()
	h.insert(10)
	print(h)
	h.insert(15)
	print(h)
	h.insert(12)
	print(h)
	h.insert(2)
	print(h)
	h.insert(1)
	print(h)
	h.insert(9)
	print(h)
	h.insert(7)
	print(h)
	h.insert(4)
	print(h)
	print(h)
	h.extract()
	print(h)
	h.delete(len(h.heap_list)-1)
	print(h)
	h.delete(2)
	print(h)
	list_values = [5,19,45,325,69768,40,654,46,0,540,40,45,798,7,468,564635,45,4,6,5,879,7]
	h2 = Heap()
	h2.build_v2(list_values)
	print(h2)
