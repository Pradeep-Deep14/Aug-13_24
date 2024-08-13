# write function to remove duplicate from below list

input_list = [5, 5, 5, 1, 1, 2, 2]

def remove_duplicates(input_list):
    seen=set()
    unique_list=[]
    duplicates_list=[]

    for i in input_list:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
        else:
            duplicates_list.append(i)
    return unique_list,duplicates_list

unique_list,duplicates_list = remove_duplicates(input_list)
print("Unique list:", unique_list)
print("Duplicates:",duplicates_list)