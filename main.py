import createKnowledgeBase as ckb
import random

def data_structure(chars,kb,binaryvalues):
    p, c, l = ckb.retKBcharacteristics()
    lst=[]
    counter=0
    for i in range(c):
        k = 0
        while (k <= p): # ελέγχουμε αν το κάθε στοιχείο του chars είναι ίσο με το
            if chars[k] in kb[i]:  # εαν το στοιχείο j του chars είναι ίσο με το kb πήγαινε
                if binaryvalues[k] == True:  # εάν είναι true τότε όλη η πρόταση θα είναι true οπότε δεν χρειάζεται περεταίρο αναζήτηση προχωράμε στην επόμενη
                    lst.append(bool(1))
                    break
            elif chars[k].swapcase() in kb[i]:  # εαν το κεφαλαίο στοιχείο του chars είναι ίσο με το kb
                if binaryvalues[k] == False:
                    lst.append(bool(1))
                    break
            if (k == p):
                lst.append(bool(0))
            k+=1
    for i in lst:
        if i == False:
            counter+=1
    lst.append(counter)
    return lst

def flip(values,i):
    binaryvalues=values
    if binaryvalues[i] == True:
        binaryvalues[i] = False
    elif binaryvalues[i] == False:
        binaryvalues[i] = True


def gsat(maxTries,maxFlips):
    kb, characters = ckb.readKnowledgeBase()
    p, c, l = ckb.retKBcharacteristics()

    breakcondition=0

    for j in range(maxTries): #max προσπάθειες
        binaryvalues = []  # μεταβλητή για να κρατάει boolean τιμές στις θέσεις τον λεκτικών
        mincost = c  # μεταβλητή για να κρατάει το μικρότερο κόστος των κινήσεων
        for i in range(p):#αναθέτουμε random bool τιμές
            binaryvalues.append(bool(random.getrandbits(1)))
        print(binaryvalues)
        data=[]#πίνακας που κρατάει το αποτέλεσμα της πρότασης

        for k in range(maxFlips):
            tmpointer=[]     #μεταβλητή που έχει δείκτη/ες από για τις αλλαγές με το μικρότερο κόστος
            tmplist=[]       #λίστα για να κρατάει τα κόστη των κινήσεων
            data.append(data_structure(characters,kb,binaryvalues))

            for i in range(p):  #συνάρτηση για να βρει τα μέγιστο κόστος
                values=binaryvalues.copy()  # το copy χρειάζεται γιατί χωρίς αυτό ο πίνακας values παίρνει τις τιμές του binaryvalues και λειτουργεί σαν δείκτης για τον binary
                flip(values,i)
                tmplist.append(data_structure(characters,kb,values)[-1])    #αποθηκεύεται το κόστος της κάθε αλλαγής μέσα στην λίστα
            print("λίστα με τα κόστη",tmplist)

            for i in tmplist:   #συνάρτηση για να βρίσκει το μικρότερο κόστος
                if(i < mincost):
                    mincost = i
            print("κοστος",mincost)

            for i in range(len(tmplist)):   #λίστα για να κρατάει τους δείκτες των τιμών όπου η αλλαγή τους έχει το μικρότερο κόστος
                if(tmplist[i] == mincost):
                    tmpointer.append(i)
            print("δείκτες",tmpointer)

            if len(tmpointer) == 0:
                break

            if(len(tmpointer)>1):
                flip(binaryvalues,tmpointer[random.randint(0,len(tmpointer)-1)])
            else:
                print(len(tmpointer))
                print("tmpointer",tmpointer[0])
                flip(binaryvalues,tmpointer[0])
            if mincost == 0:
                data.append(data_structure(characters, kb, binaryvalues))
                print(data)
                print("Congrats every sentence in the KB is True ")
                return True
            if k == maxFlips-1:
                data.append(data_structure(characters, kb, binaryvalues))
                print(data)
                print("No solution found,need to add new bool values")

            print("--------")


        if j == maxTries-1:
            print("No solution can be found through GSAT moving on to resolution.")
    return False


def main():
    ckb.createKnowledgeBase(3, 10, 3)
    p, c, l = ckb.retKBcharacteristics()
    gsat(10, 20)
    # while(1):
    #     newcharacter=input("dwse xaraktira re arxidi\n")
    #     c=c+1
    #     kb, characters = ckb.readKnowledgeBase()
    #     kb.insert(0,newcharacter.swapcase())
    #     if gsat(10,20):
    #         knowledgeBaseFile = open('knowledgeBase.txt', 'a')
    #         knowledgeBaseFile.write(newcharacter)
    #         knowledgeBaseFile.close()
    #     else:
    #         c=c-1
    #         kb.pop(0)
    #     tmpchar=input("Shall we continue sir? (y/n)")
    #     if tmpchar == "n":
    #         break












if (__name__ == '__main__'):
    main()
