def main():
    ans = (input("What is the answer to the Great Question of Life, the Universe and Everything? "))
    answer(ans)

def answer(ans):
    ans = ans.strip().lower()
    if ans in ("42","forty two","forty-two"):
        print("Yes")
    else:
        print("No")

main()
