'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0
# if string contains "th", repeat with recursion (NO LOOPS) and increment by 1
    if "th" in word[:2]:
        return count_th(word[2:]) + 1
# if not, go back to check each index
    else:
        return count_th(word[1:])
