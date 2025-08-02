print("*** Reading E-Book ***")
brotext = input("Text , Highlight : ")
brotext = brotext.split(",")
text = brotext[0]
highlight = brotext[1]
text = list(text)
num = 0
for i in text:
    if i == highlight:
        text[num] = f"[{i}]"
    num += 1

out = "".join(text)
print(out)
