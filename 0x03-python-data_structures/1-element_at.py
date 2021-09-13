#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return("None")
        elif i >= 0 and i <= idx:
            return(my_list[idx])
        else:
            return("None")
