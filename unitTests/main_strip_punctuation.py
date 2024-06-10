from src.strip_punctuation import strip_punctuation_ru

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip()
    print(strip_punctuation_ru(data))
