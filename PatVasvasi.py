#!/usr/bin/env python3
# Author: Arash Zarif

def format_text(input_text):
    cleaned_text = " ".join(input_text.split())

    try:
        for i, char in enumerate(cleaned_text):
            if char == "@":
                for j in range(i + 1, len(cleaned_text)):
                    try:
                        if cleaned_text[j] == "#":
                            cleaned_text = cleaned_text[:j] + cleaned_text[j + 1:]
                            break
                    except IndexError:
                        break
    except IndexError:
        pass

    formatted_text = cleaned_text.replace("\\n", "\n")
    return formatted_text


def main():
    user_input = input().strip()
    formatted_text = format_text(user_input)
    print("Formatted Text:", formatted_text)


if __name__ == "__main__":
    main()
