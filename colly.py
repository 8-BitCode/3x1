listF = {}
listG = {}

inlength = int(input('Length: '))

for p in range(3, inlength+1, 2):
    length = p
    track = length
    list1 = []
    count = 0
    while (length != 1):
        if (length % 2) == 0:
            length = length // 2
            if (length < p) and (p not in listG):
                listG[p] = count
            count += 1
        else:
            length = (3 * length) + 1
            if (length < p) and (p not in listG):
                listG[p] = count
            count += 1
        if(length == 1):
            track = track + 1
            length = track
            break
        list1.append(length)
    listF[p] = max(list1)

# print("Maximum value of sequence:")
# print(listF)

# print("Values of sequence:")
# print(listF.values())

inverted_dict = {}

# Iterate over the original dictionary
for key, value in listG.items():
    # Check if the value is already a key in the inverted dictionary
    if value in inverted_dict:
        # If the value is already a key, append the current key to the list of keys for that value
        inverted_dict[value].append(key)
    else:
        # If the value is not already a key, create a new list with the current key and add it to the dictionary
        inverted_dict[value] = [key]

# Sort the dictionary by the keys in ascending order
sorted_dict = {k: sorted(v) for k, v in sorted(inverted_dict.items())}


# for general testing
# print("Steps to go below original value:")
# print(sorted_dict)

# for big nums reasearch
with open("output.txt", "w") as f:
    f.write("Steps to go below original value:\n")
    # Write the sorted dictionary to the file
    for key, value in sorted_dict.items():
        f.write(f"{key}: {value}\n")
