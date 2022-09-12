


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    list_x = list(str(x))
    if list_x == list(reversed(list_x)):
        return True
    
    return False
        