def bisect(num, List):
    copy = List
    while True:
        mid = len(List) / 2
        if num > List[mid]:
            List = List[mid:]
        elif num < List[mid]:
            List = List[:mid]
        elif num == List[mid]:
            return copy.index(num)


print bisect(35, [1,5,15,18,23,26,35,48,55])
