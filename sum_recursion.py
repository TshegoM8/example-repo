def adding_up_to(list_of_integers, index_point):
    if index_point == 0:
        return list_of_integers[0]
    else:
        return list_of_integers[index_point] + adding_up_to(list_of_integers, index_point -1)
print(adding_up_to([1,4,5,3,12,16], 3))
print(adding_up_to([8,4,2,6], 2))

    



               
