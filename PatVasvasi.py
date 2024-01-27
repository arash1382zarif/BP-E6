text = input().strip()
text = " ".join(text.split())
n = len(text)
try:
    for i in range(n):
        if text[i] == "@":
            for j in range(i+1, n):
                try:
                    if (text[j] == "#"):
                        text = text[:j] + text[j+1:]
                        break
                except:
                    break
except:
    pass

text = text.replace("\\n", "\n")
print("Formatted Text:", text)