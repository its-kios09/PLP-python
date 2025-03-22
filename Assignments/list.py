
#
def create_list():
    my_list = []
    my_list.extend([10, 20, 30, 40])
    my_list.insert(2, 15)
    my_list.extend([50,60,70])
    my_list.pop(-1)
    my_list.sort()
    index_of_30 = my_list.index(30)
    print(f"index of 30: ",index_of_30 )
    print(my_list)

create_list()

