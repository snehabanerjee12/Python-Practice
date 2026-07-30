""" Find duplicate Numbers"""


List = list(map(int,input("Enter data:").split(",")))
print(List)

List_Set = set()

Result = []

for item in List:
    if item not in List_Set:
        List_Set.add(item)
    else:
        Result.append(item)

print("Duplicates",Result)