def largest_number(list_of_integers):
    if len(list_of_integers) ==1 :
        return list_of_integers[0]
    else:
        max = largest_number(list_of_integers[1:])
        if list_of_integers[0] > max:
            return list_of_integers[0]
        else:
            return max
        
print(largest_number([2,5,3,4]))
print(largest_number([5,6,4,2,1,8]))