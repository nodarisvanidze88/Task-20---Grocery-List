def main():
    # give instruction to user how to stop loop
    print("Add items, stop adding add \"S\"")
    # create list for items
    items = []
    # create infinity loop for adding new items
    while True:
        # get user inputs and modify the text
        item = input().strip().upper()
        # if user input is "S" stop the loop
        if item == "S":
            break
        # ignor under input if empty
        if item == "":
            continue
        # add items in list
        items.append(item)
    # get modivied lists
    it, nums = textCounter(items)
    # print result
    for i in range(len(it)):
        print(str(nums[i]), str(it[i]))

def textCounter(txt):
    # sort users list
    txt = sorted(txt)
    # create new list with unique items
    uniqueList = []
    # create new list for unique numbers
    count = []
    for i in txt:
        if i not in uniqueList:
            uniqueList.append(i)
            count.append(txt.count(i))
    return uniqueList, count

main()
