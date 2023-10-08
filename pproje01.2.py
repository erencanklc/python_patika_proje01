"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""


l = [[1, 2], [3, 4], [5, 6, 7]]

def ters(l):
    for i in l:
        i.reverse()
    l.reverse()
    return(l)
         
    
print(l)
print(ters(l))


#l=[[1,2],[3]]
#l[0].sort(reverse=True)
#print(l)