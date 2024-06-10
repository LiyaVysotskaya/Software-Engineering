from src.phone_number import is_correct_mobile_phone_number_ru

if __name__ == "__main__":
    import sys
    number = sys.stdin.read().strip()
    if is_correct_mobile_phone_number_ru(number):
        print("YES")
    else:
        print("NO")
