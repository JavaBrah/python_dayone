def linear_search_global(item, list_to_search: list):
    item_index_list = []
    for i in range(len(list_to_search)):
        if item == list_to_search[i]:
            item_index_list.append(i)
    return item_index_list
