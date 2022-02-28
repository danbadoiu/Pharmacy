def mergeSort(myList, key, reverse):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left, key, reverse)
        mergeSort(right, key, reverse)
        i = 0
        j = 0
        k = 0
        if reverse == True:
            while i < len(left) and j < len(right):
                if key(left[i]) < key(right[j]):

                    myList[k] = left[i]

                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1

                k += 1


            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1
        else:
            while i > len(left) and j < len(right):
                if key(left[i]) > key(right[j]):

                    myList[k] = left[i]

                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1

                k += 1

            while i > len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j > len(right):
                myList[k] = right[j]
                j += 1
                k += 1

    return myList
