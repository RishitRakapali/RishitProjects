def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value

my_list = [1, 3, 7, 23, 0, 45, 3]

sorted_list = insertion_sort(my_list)
print(sorted_list)