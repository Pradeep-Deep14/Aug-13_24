list1 =[1, 2, 3, 4, 1, 2, 3, 5, 4, 5]

#Print duplicates alone

#duplicates=list(set([x for x in list1 if list1.count(x)>1]))

#print(duplicates)


#without using inbuilt functions

def duplicates_list(list1):
    seen=set()
    list=[]
    for i in list1:
        if i in seen and i not in list:
            list.append(i)
            
    return list

print (duplicates_list(list1))