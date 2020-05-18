# =============================================================================
# Data Structures and Algorithms Nanodegree Udacity (Linked Lists Challenges)
# 
# Problem Statement:
# You are given the head of a linked list and two integers, i and j. 
# You have to retain the first i nodes and then delete the next j nodes. 
# Continue doing so until the end of the linked list. 
# Write your code in the skip_i_delete_j function below
# 
# Here is an example:
# 
# linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
# i = 2
# j = 3
# Output = 1 2 6 7 11 12
# =============================================================================



# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Write your code in this function
def skip_i_delete_j(head, i, j):
    
    current_node = head
    count = 0
    
    while current_node:
        if count != i - 1:
            current_node = current_node.next
            count += 1
            
        elif count == i - 1:
            temp = current_node
            for k in range(j+1):
                if current_node != None:
                    current_node = current_node.next
                else:
                    break
            temp.next = current_node
            count = 0
            
    return head

# helper function for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

#helper function for testing purpose
def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
    
#helper function for testing purpose
def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")
        
        
# =============================================================================      
#Test 1 
#       
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 2
# head = create_linked_list(arr)
# solution = [1, 2, 5, 6, 9, 10]
# test_case = [head, i, j, solution]
# test_function(test_case)
#
#Test 2
#       
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 3
# head = create_linked_list(arr)
# solution = [1, 2, 6, 7, 11, 12]
# test_case = [head, i, j, solution]
# test_function(test_case)
#
#Test 3
#
# arr = [1, 2, 3, 4, 5]
# i = 2
# j = 4
# head = create_linked_list(arr)
# solution = [1, 2]
# test_case = [head, i, j, solution]
# test_function(test_case)
#
#Test 4
#
# arr = [1, 2, 3, 4, 5]
# i = 2
# j = 0
# head = create_linked_list(arr)
# solution = [1, 2, 3, 4, 5]
# test_case = [head, i, j, solution]
# test_function(test_case)
# =============================================================================
