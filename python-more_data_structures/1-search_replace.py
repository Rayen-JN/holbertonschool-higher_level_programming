#!/usr/bin/python3
def search_replace(my_list, search, replace):
    NEW = list(map(lambda x: replace if x == search else x, my_list))
    return (NEW)
