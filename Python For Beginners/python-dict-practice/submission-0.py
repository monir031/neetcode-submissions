from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    m=set()
    L={}
    for i in word:
        m.add(i)
        L[i]=0

    for i in m:
        for j in range(len(word)):
            if (word[j]==i):
                L[i]+=1
    return(L)




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
