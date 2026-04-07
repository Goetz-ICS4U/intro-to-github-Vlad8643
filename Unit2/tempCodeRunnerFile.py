def isPalindrome(word):


    word = word.lower()
    return word == word[::-1] and len(word) > 1