def flatten(list1):
    #boş bir liste oluşturuyoruz.
    newList = []
    #Listemizi döngüye alıp, elemanları bakıyoruz.
    for e in list1:
        #Eğer listenin elemanı, başka bir liste değilse newList'imize listemize ekliyoruz.
        if type(e) != type([]):
            newList.append(e)
        #Eğer listenin elemanı, başka bir liste ise, bu sefer onu flatten fonksiyonuna sokuyoruz ve 
        # liste olma özelliğini kaybedene kadar bu işlemi yapıyoruz. En sonunda newList'imize ekliyoruz.
        else:
            newList.extend(flatten(e))
    return newList
    

list1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
list1=flatten(list1)
print(list1)
#output [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
