def extract_even(l):
    even_list = []
    
    for num in l:
        if num % 2 == 0:
            even_list.append(num)
            
    return even_list

list = [1, 4, 5, -1, 10]
result = extract_even(list)

print("Original list:", list)
print("Even numbers list:", result)