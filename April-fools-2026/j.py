def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    s = input()
    if s == "Do you think this contest should be rated?":
        print("Yes")
    elif s == "Are you a verified human?":
        print("Yes, I can attest to my status as a thoroughly validated, carbon-based biological entity.")