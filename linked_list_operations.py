class Node:
    def __init__(self, value):
        #'''Create a new node'''
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, value):
        #'''linked_list constructor'''
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1     

    
    def append(self, value):
        ''' creates a new node ,and adds it to the end of the linkedList '''
        'create the new node'
        new_node = Node(value)
        
        #'check to see if the head is empty'
        if self.head is None:
           # 'create a node for the head'
            self.head = Node(value)
            self.tail = Node(value)
        else:
           # 'point the last node to the new node *appending it*'
            self.tail.next = new_node

            #'point the tail to the last node'
            self.tail = new_node
            self.tail.next = None
        self.length += 1
        return True
       
    
    def prepend(self, value):
        '''add node to begining of linked-list'''
        new_node = Node(value)
        temp_head = self.head

        #'assemble a new node if user tries to prepend an empty linked-list'
        if self.length <= 0:
            temp_head = new_node
            self.head = temp_head
            self.tail = self.head
            self.length += 1
            return True
        
        new_node.next = temp_head
        self.head = new_node
        self.length += 1
        return True


    def link_list_length(self):
        #'REturn the length of the current linked_list'
        return self.length

    def print_list(self):
        #'Check if linked-list is empty'
        if self.length == 0:
            return None
        temp = self.head

        while temp is not None:
            print(temp.value)
            #'move to the next node'
            temp = temp.next
        print(f'List Length is {self.link_list_length()}')
        return True
        
    def pop_first_node(self):
        #'Pop the first node off the linked-List'
        temp_head = self.head
       # 'check for empty linked-lists'
        if self.length <= 0:
            return None

        #'Move head to next node'              
        self.head = self.head.next
        self.length -= 1
        
        #'Move tail to None if length is 0 after decrement'
        if self.length == 0:
            self.tail = None
        return temp_head


    def pop(self):
        #'Pop node off the end of linked-list'
        temp = self.head
        pre = self.tail

        #'If user attempts to pop on an empty linked-list'
        if self.length <= 0:
            return None

        #'If user is popping linked-list with one Node'
        if self.length == 1:            
            self.length -= 1
            temp = self.head
            self.head = None
            self.tail = self.head

        #'Move temp(Head) to next Node'
        while temp.next:            
            pre = temp
            temp = temp.next
        self.tail = pre         
        self.tail.next = None
        self.length -= 1    
        return temp


    def get_value(self, index):
        #'Check for indexes that don\'t exist'
        if self.length < index or index >= self.length:
            return None        
        temp_head = self.head
        node_counter = 1

        while temp_head.next:
            if (node_counter - 1) == index:
                break
            temp_head = temp_head.next
            node_counter += 1
        return temp_head


    def set_value(self, index, new_value):
        #'Verify index using get_value method'
        temp = self.get_value(index)

        #'Set new_value if temp is true'
        if temp:
            temp.value = new_value
            return True
        return False


    def insert(self, index, new_value):
        #'If the user tries to insert a node with a lenght of zero'
        if self.length == 0:
            return self.prepend(new_value)
        
        #'If user tries to insert node at the end of list'
        if index == self.length:
            return self.append(new_value)
        
        #'Verify index using get_value method'
        temp = self.get_value(index)
 
        #'Insert new Node if temp'
        if temp:
            new_node = Node(new_value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False


    def remove_node(self, index):
        '''Check if index is equal to first node or last node
        the methods below will automatically check if the user is attempting
        to remove a node on an empty list'''        
        if index == 0: 
            return self.pop_first_node()
        if index == self.length - 1:
            return self.pop() 

        #'Remove the node'
        prevous_node = self.get_value(index - 1)
        temp = prevous_node.next
        prevous_node.next = temp.next
        self.length -= 1
        return temp
    
    #Reverse method V1
#     def reverse_list(self):
#         #'User cannot reverse a node that is less than or equal to 1 in length'
#         if self.length <= 1:
#             return None
        
#         #'Place_holders for swapped values'
#         head_place_holder = None
#         tail_place_holder = None
#         temp_head = self.head
#         temp_tail = self.tail

#         '''The "Iteration" variable is the Number of times linked-list will be iterated through.
#             This will cover lists lengths of  ODD or EVEN numbers.
#             *For Odd-numbered lists, the Center node will not be touched.*
#             example: 
#                 After one iteration, odd number linked-list (A-B-C-D-E-F-G) will become:
#                     v           v
#                     G-B-C-D-E-F-A
#             The second iteration will become:
#                       v       v
#                     G-F-C-D-E-B-A
#             Final iteration will become:
#                         v   v
#                     G-F-E-D-C-B-A
#         '''
#         iteration = self.length // 2 

#         current_tail_index = self.length - 1
        
#         while iteration != 0:
#             head_place_holder = temp_head.value
#             tail_place_holder = temp_tail.value
            
#             #'Swap Values for tails and heads'
#             temp_head.value = tail_place_holder
#             temp_tail.value = head_place_holder

#             #'Decrease number if iterations'
#             iteration -= 1

#             #'Move head to the NEXT node, move tails to PREVIOUS node'
#             temp_head = temp_head.next
#             current_tail_index -= 1
#             temp_tail = self.get_value(current_tail_index)
#         return
        
        #Reverse method V2
        def reverse_list(self):
            ''' This version points the Node's "next" attribute in the opposite 
            direction...a more efficient way to revser the list'''
            temp = self.head
            self.head = self.tail
            self.tail = temp

            after = temp
            before = None

            for _ in range(self.length):
                #Move after node
                after = temp.next

                #Point current node in the opposite direction
                temp.next = before
                before = temp
                temp = after            
        return


linked_list_one = Linked_list(10)
linked_list_one.append(20)
linked_list_one.append(30)
linked_list_one.append(40)
linked_list_one.append(50)
linked_list_one.append(60)
linked_list_one.append(70)
linked_list_one.append(80)#Middle Node
linked_list_one.append(90)
linked_list_one.append(100)
linked_list_one.append(120)
linked_list_one.append(130)
linked_list_one.append(140)
linked_list_one.append(150)


linked_list_one.reverse_list()
linked_list_one.print_list()

