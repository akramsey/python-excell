def countCapitalLetters(str):
    count = 0;
    for c in str:
        if c.isupper():
            count += 1
    return count


print countCapitalLetters("asddfasdFASDFASFDAASDF")
print countCapitalLetters("THISisAtest")