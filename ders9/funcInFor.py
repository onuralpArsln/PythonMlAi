def basic(inp:str)->int:
    if inp == "a":
        return 1
    if inp == "b":
        return 2
    if inp == "c":
        return 3

def translate(word:str)->None:
    for i in word:
        print(f"i değeri {i}")
        z=basic(i)
        print(z)


key= "bcaa" # string
translate(key)