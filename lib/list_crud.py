def create_an_empty_list():
    return []

def create_a_list():
    return [5,3,1,2]

def add_element_to_end_of_list(l, element):
    # element = 5
    # l=[5,3,1,2]
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    # element = 0
    # l=[5,3,1,2,5]
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    # l =[0,5,3,1,2,5]
    # for num in l:
    l.pop(-1)
    return l
# print(remove_element_from_end_of_list([0,5,3,1,2,5]))
def remove_element_from_start_of_list(l):
    del l[0]
    return l

def retrieve_first_element_from_list(l):
   return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
