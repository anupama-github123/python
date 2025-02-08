
my_list = []
while True:
    value = input("Enter a value (or type 'stop' to finish): ")
    if value == 'stop':
        break
    my_list.append(value) # You can convert to int/float if needed

print("Final list:", my_list)

print('max:',max(my_list))
print('min:',min(my_list))