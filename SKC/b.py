def solve(n, emails, k):
    cnt = 0 
    for email in emails:
        prefix = email[:3]
        if prefix == "s27" or prefix == "s28":
            cnt += 1
    if cnt >= k:
        return "YES"
    else:
        return "NO"
    
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    emails = []
    for _ in range(n):
        emails.append(input().strip())
    print(solve(n, emails, k))