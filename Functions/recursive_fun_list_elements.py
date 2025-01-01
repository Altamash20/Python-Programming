def print_list(list, idx=0):
    if(idx == len(list)):
        return 0
    print(list[idx])
    print_list(list, idx+1)

stationery = ["geometry box", "pen holder", "bookmarks", "calendar"]
print_list(stationery)