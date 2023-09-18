def insertion_sorter(list):
    for key_pos in range(1, len(list)):
        key_value = list[key_pos]
        scan_pos = key_pos - 1

        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1

        list[scan_pos + 1] = key_value
    return list
file = open('world.txt')

lang_list = []
for line in file:
    line = line.strip()
    lang_list.append(line)
print(lang_list)

key = 'Russian'
i = 0
while i < len(lang_list) and lang_list[i] != key:
    i += 1
if i == len(lang_list):
    print('Language is not in the list')
else:
    print('%s is in index %s of the list' % (key, i))

sorted_list = insertion_sorter(lang_list)
for language in sorted_list:
    print(language)