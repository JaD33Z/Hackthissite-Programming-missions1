
# ====================== * Python Word-List Unscrambler * ======================== #


def word_list():
    with open('wordlist.txt', 'r') as word_file:
        result = word_file.readlines()
        word_list = [result[i].split() for i in range(len(result))]
        new_list = [x for y in word_list for x in y]
        return new_list


def scrambled_list():
    with open('paste.txt', 'r') as scram_file:
        result = scram_file.readlines()
        scrams = [result[i].split() for i in range(len(result))]
        scram_list = [x for y in scrams for x in y]
        return scram_list


def unscramble_word(scrambled_word):
    for word in word_list():
        if sorted(scrambled_word) == sorted(word):
            return word


def convert_whole_list():
    ls = []
    for i in scrambled_list():
        new = unscramble_word(i)
        ls.append(new)
    return ",".join(ls)

print(convert_whole_list())

