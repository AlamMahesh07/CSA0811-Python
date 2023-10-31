num_elements = int(input("Enter the number of elements: "))
elements = input("Enter the elements (comma-separated): ").split(',')
elements = [int(x) for x in elements]
element_to_insert = int(input("Enter the element to be inserted: "))
position = int(input("Position: "))
elements.insert(position - 1, element_to_insert)
print(elements)
