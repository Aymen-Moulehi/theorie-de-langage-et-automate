#create simple program resolte all theorie_langage probleme
import time
from prettytable import PrettyTable


def testeur(q0,a,liste):
    r=0
    big_list=list()
    big_list.append([])
    big_list.append([])
    lista = list()   
    for i in q0:
        for j in a:
            for k in range(len(liste)):
                if(i==liste[k][0] and j==liste[k][1]):
                    lista.append(liste[k][2])
            #big_list.insert(r,big_list[r]+lista)
            
            
            for h in lista:
                if big_list[r].count(h) > 0 :
                    lista.remove(h)
            big_list[r]=big_list[r]+lista
            lista=list()
            r+=1
            #big_list.append(lista)
            
        r=0
    big_list.insert(0,q0)
    return big_list
    
def veriflist1(liste1,liste2):
    if len(liste1) == len(liste2):
        for i in liste1:
            if not(i in liste2):
                return False
        return True
    return False
def veriflist2(liste1,bigliste):

    for i in bigliste:
        if(veriflist1(liste1,i)):
            return True
    return False

print("------------------------------------------------------------------------")
print("[+]  Transformer automate non déterministe en automate déterministe  [+]")
time.sleep(1)
print("[+]                          program start                           [+]")
print("------------------------------------------------------------------------\n\n\n")
time.sleep(1)

#lecture liste de etat
print("donner la liste de q")
q=list()
i=0;
x=input("donner q "+str(i)+": ")
while(x != ''):
    q.append(x)
    i+=1
    x=input("donner q "+str(i)+": ")
print("------------------------------------------------------------------------\n\n\n")
    
#print(q)

#lecture liste d alphabet

print("donner la liste de alphabet")
a=list()
i=0;
x=input("donner Σ "+str(i)+": ")
while(x != ''):
    a.append(x)
    i+=1
    x=input("donner Σ "+str(i)+": ")
    
#print(a)

print("------------------------------------------------------------------------\n\n\n")

#lecture liste d etat intial

print("donner la liste d etat intial")
q0=list()
i=0;
x=input("donner Q0 "+str(i)+": ")
while(x != ''):
    q0.append(x)
    i+=1
    x=input("donner Q0 "+str(i)+": ")
    
#print(q0)
print("------------------------------------------------------------------------\n\n\n")
#lecture liste d etat final

print("donner la liste d etat final")
f=list()
i=0;
x=input("donner F "+str(i)+": ")
while(x != ''):
    f.append(x)
    i+=1
    x=input("donner F "+str(i)+": ")
print("------------------------------------------------------------------------\n\n\n")   
#print(f)

liste=list()
for i in q:
    for j in a:
        x=input("("+i+","+j+") ==> ")
        while(x!=''):
            liste.append([i,j,x])
            x=input("("+i+","+j+") ==> ")
#for i in liste:
    #print(i)
print("------------------------------------------------------------------------\n\n\n")

   

#print(test)
show_list=list()
show_list.append("etat \ alpahbet")
for i in a:
    show_list.append(i)
t = PrettyTable(show_list)


listn = list()
listn.append(q0)
st = 0
mx = 0
#test=testeur(listn[st],a,liste)
#print(test)

while(st <= mx  and st<10):
    test=testeur(listn[st],a,liste)
    for i in test:
        if(not(veriflist2(i,listn))):
            listn.append(i)
            mx += 1
    st+=1
    t.add_row(test)
    #print(test)
    test=list()
      
    
print(t)    
    
exiten = input("\n \npress any button to exit ...")
    
    
    



















