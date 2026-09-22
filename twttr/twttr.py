
def main():
    v = input("Enter words: ")
    print(vowels(v))



def vowels(n):
    word = str(n)
    if word.lower() in "aeiou":
        return word.strip("a","e","i","o","u")

main()
