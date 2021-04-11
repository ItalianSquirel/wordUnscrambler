# open file in read mode
f = open("words.txt", "r")

# read and close words
contents = f.read()
f.close()

# to split words by " " character
contents = contents.split(" ")

def build_dict(word_list):
    """Build a dictionary from the given word_list where key values of sorted word letters map to lists of the original word(s)"""

    # initialize a dictonary
    d = dict()

    # iterate through the word_list, mapping sorted letters to word
    for i in word_list:

        # key - sorted letters in the word
        # how to sort ? --> convert to list, then sort. Finally join the sorted list.
        key = ''.join(sorted(list(i)))

        # check if sorted letters avaialble in dict,
        # if yes - append the word to the value
        # else - put the word as the 0th element of the value list
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]

    return d


# call build_dict() function
sorted_dict = build_dict(contents)


def unscramble(jumble, sorted_dict):
    """Return a list of unscrambled words that match the given jumble"""

    # sort the jumbled word
    jumble = ''.join(sorted(list(jumble)))

    # check if jumble in dict
    if jumble in sorted_dict:
        return sorted_dict[jumble]
    else:
        return "No word found"


# read input and print output

word = input("Enter a jumbled word:/n")
print("{} unscrambles to: {}".format(word, unscramble(word, sorted_dict)))

word = "sdf"
print("{} unscrambles to: {}".format(word, unscramble(word, sorted_dict)))

word = "asewes"
print("{} unscrambles to: {}".format(word, unscramble(word, sorted_dict)))

word = "enost"
print("{} unscrambles to: {}".format(word, unscramble(word, sorted_dict)))

word = "aaabcs"
print("{} unscrambles to: {}".format(word, unscramble(word, sorted_dict)))


