def uniq_add(my_list=[]):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    val = 0
    for j in unique_list:
        val += j
    return val
