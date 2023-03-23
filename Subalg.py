import math
import numpy as np

class Subalg(object):
    #ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text
    def pb1(self,sir):
        cuvinte=sir.split()
        cuvinte.sort()
        return cuvinte[-1]

    #distanța Euclideană între două locații identificate prin perechi de numere
    def pb2(self,xi,xj,yi,yj):
        dist=math.sqrt(pow(yi-xi,2)+ pow(yj-xj,2))
        return dist

    #produsul scalar a doi vectori rari care conțin numere reale
    def pb3(self,a,b):
        prod=np.dot(a,b)
        return prod

    #cuvintele unui text care apar exact o singură dată în acel text
    def pb4(self,sir):
        cuvinte=sir.split()
        uniq_cuv=[]
        duplicate_cuv=[]
        for cuv in cuvinte:
            if cuv not in uniq_cuv:
                if cuv not in duplicate_cuv:
                    uniq_cuv.append(cuv)
            else:
                uniq_cuv.remove(cuv)
                duplicate_cuv.append(cuv)
            
        return uniq_cuv

    #șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură valoare
    #se repetă de două ori, să se identifice acea valoare care se repetă
    def pb5(self,sir_numere):
        suma=sum(sir_numere)
        suma_nr_distincte=sum(set(sir_numere))
        nr_duplicat=suma-suma_nr_distincte
        return nr_duplicat

    #șir cu n numere întregi care conține și duplicate, 
    #să se determine elementul majoritar (care apare de mai mult de n / 2 ori)
    def pb6(self,sir_numere):
        aparitii=0
        for nr in sir_numere:
            if aparitii==0:
                element_majoritar=nr
            if element_majoritar==nr:
                aparitii+=1
            else:
                aparitii-=1

        aparitii=0
        for nr in sir_numere:
            if nr==element_majoritar:
                aparitii+=1

        if aparitii>len(sir_numere)/2:
            return element_majoritar
        return -1

    # al k-lea cel mai mare element al unui șir de numere cu n element
    def pb7(self,sir_numere,k):
         sir_sortat=list(set(sir_numere))
         sir_sortat.reverse()
         if k<len(sir_sortat):
            return sir_sortat[k-1]
         return -1

    #Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n
    def pb8(self,n):
        sir_nr_binare=[]
        for i in range(1,n+1):
            sir_nr_binare.append(bin(i)[2:])
        return sir_nr_binare

    #matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)),
    #să se calculeze suma elementelor din sub-matricile identificate de fieare pereche
    def pb9(self,matrice,perechi_coordonate):
        sum_list=[]
        for coordonate in perechi_coordonate:
            suma=0
            p, q = coordonate[0][0], coordonate[0][1]
            r, s = coordonate[1][0], coordonate[1][1]
            if p<0 or r<0 or q>=len(matrice) or s>=len(matrice) or p>q or r>s:
                return -1
            if p > r:
                p, r = r, p
            if q > s:
                q, s = s, q
            for i in range(p,r+1):
                suma+=sum(matrice[i][q:s+1])
            sum_list.append(suma)
        return sum_list


    #matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, 
    #să se identifice indexul liniei care conține cele mai multe elemente de 1
    def pb10(self,matrice):
         max=0
         indice=-1
         for x in range(0,len(matrice)-1):
             suma=sum(matrice[x])
             if suma>max:
                 max=suma
                 indice=x
         return indice

    #o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 
    #toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1
    def pb11(self,matrice):
        k=1
        n=len(matrice)
        m=len(matrice[1])
        for i in range(0,n):
            for j in range(0,m):
                if matrice[i][j]==0:
                    k+=1
                    self.insula(i,j,k,matrice)

        nr_zero=[]
        for i in range(0,n):
            if matrice[i][0]!=1:
                nr_zero.append(matrice[i][0])
            if matrice[i][m-1]!=1:
                nr_zero.append(matrice[i][m-1])

        for j in range(0,m):
            if matrice[0][j]!=1:
                nr_zero.append(matrice[0][j])
            if matrice[n-1][j]!=1:
                nr_zero.append(matrice[n-1][j])

        for i in range(0,n):
            for j in range(0,m):
                if matrice[i][j]!=1:
                    if matrice[i][j] in nr_zero:
                        matrice[i][j]=0
                    else:
                        matrice[i][j]=1
        

        return matrice

    def insula(self,i,j,k,matrice):
        if i>=0 and j>=0 and i<len(matrice) and j<len(matrice[1]):
            if matrice[i][j]==0:
                matrice[i][j]=k
                self.insula(i+1,j,k,matrice)
                self.insula(i-1,j,k,matrice)
                self.insula(i,j+1,k,matrice)
                self.insula(i,j-1,k,matrice)


    #def run_all_subalg(self):
        #while(1):
            #nr_pb=input("Introduceti numarul problemei: ")
            #if(nr_pb=='1'):
                #sir=input("Introduceti propozitia:")
                #cuv=self.pb1(sir)
                #print(cuv)
            #elif(nr_pb=='2'):
               # xi=int(input("xi="))
                #xj=int(input("xj="))
               # yi=int(input("yi="))
                #yj=int(input("yj="))
               # dist=self.pb2(xi,xj,yi,yj)
               # print(dist)