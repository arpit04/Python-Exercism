def user_input():
    return input("Enter the phrase: ")

def acronym(words):
    return "".join(word[0] for word in words).upper()

def main():
    words = user_input().split()
    print(f"The acronym for your phrase is {acronym(words)}.")

if __name__ == "__main__":
    main()
