def main():
    m = int(input("m: "))
    e = energy(m)
    print(f"E: {e}")



def energy(n):
    return (n * (3*10**8)**2)

if __name__ == "__main__":
    main()

