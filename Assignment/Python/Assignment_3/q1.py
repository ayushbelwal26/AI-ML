def palindrome(s):
    st = 0
    end = len(s)-1

    while(st <= end):
        if(s[st] != s[end]):
            return False
        st += 1
        end -= 1
    return True

s = input("Enter string to check: ")
print(palindrome(s))

