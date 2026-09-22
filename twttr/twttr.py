
def main():
    v = input("Enter words: ")
    print(vowels(v))



def vowels(n):
    result = ""
    for c in n:
        if c.lower() not in "aeiou":
            result += c
    return result

main()
