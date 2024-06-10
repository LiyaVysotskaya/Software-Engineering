from src.palindrome import is_palindrome

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip()
    if is_palindrome(data):
        print("YES")
    else:
        print("NO")
