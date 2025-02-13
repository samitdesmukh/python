n= int(input("Enter the number of terms in the list"))
sample_list=[]
for i in range(n):
    element= int(input(f"Enter element {i+1}:"))
    sample_list.append(element)
count_dict={}
for num in sample_list:
    count_dict[num]=count_dict.get(num,0)+1
print("Element count dictionary:",count_dict)