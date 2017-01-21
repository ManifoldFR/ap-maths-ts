
# coding: utf-8

# # Exercice I.6
# 
# La fonction $f$ est dérivable, sa dérivée est $f'(x)=3(x-1)^2\geq0$, d'où $f$ est strictement croissante sur $I:={]-\infty,1]}$. De plus $f(x)\to-\infty$ lorsque $x\to-\infty$, et $f(1)=0$. 
# 
# Ainsi, l'image de $I$ par $f$ est $]-\infty,0]\subset I$, et la stabilité de $I$ par $f$.
# Enfin, $$\forall n\in\mathbb N, \ u_n\in I.$$
# 
# On a $g(x)=(x-1)^3-x$, d'où $g$ est dérivable de dérivée $g'(x)=3(x-1)^2-1 = 3x^2-6x+2 = 3\left(x-1-\frac{\sqrt 3}{3}\right)\left(x-1+\frac{\sqrt 3}{3}\right)$. Donc $g$ a pour maximum sur $I$ le réel $g\left(1-\frac{\sqrt 3}{3}\right) = \frac{2}{3\sqrt 3}-1<0$, d'où $g<0$ sur $I$.
# 
#    On en déduit que $\forall n\in\mathbb N,\ u_{n+1}-u_n = g(u_n)<0$: $(u_n)$ est strictement décroissante.
# 
# On a deux cas de figure : $u$ minorée (et donc converge vers un réel $\ell < u_0 \leq 1$), et $u$ non minorée (et donc $u_n\to-\infty$).
#  
#  Si $u$ est minorée, elle admet une limite finie $\ell\in I$ qui vérifie alors $f(\ell)=\ell$ i.e. $g(\ell)=0$, mais $g<0$ sur $I$: absurde.  
#  Donc $u$ n'est pas minorée, $$u_n\xrightarrow[n\to+\infty]{}-\infty. $$
# 

# # Exercice I.7
# 
# Soit $f:\mathbb R\longrightarrow\mathbb R,\;x\longmapsto -(x-2)^2+2$.
# 
# Étudions le signe de $g:x\longmapsto f(x)-x$ sur ${]-\infty,2]}$. On a $g(x)=-(x-2)^2+2-x = -x^2+3x-2 = -(x-1)(x-2)$ pour tout $x \leq 2$, d'où $1$ et $2$ sont les seuls points fixes de $f$, et le tableau de signe suivant:
# 
# | $x$ | $-\infty\qquad 1$ | $\hphantom{1}\qquad 2$ |
# |:---:|:-----------------:|:----------:|
# | $g(x)$ | $-$            | $+$        |
# 
# De plus $f'(x)=-2(x-2)$ d'où $f$ est strictement croissante sur $]-\infty,2]$. Donc $1<x<2\Rightarrow1=f(1)<f(x)<f(2)=2$ (donc $I:={]-\infty,1[}$ est stable), et $x<1 \Rightarrow f(x)<f(1)=1$ (donc $J:={]1,2[}$ est stable).
# 
# On distingue trois cas : $u_0<1$, $u_0=1$, et $1<u_0<2$.
# 
# Dans le deuxième cas $u$ stationne à $1$.  
# Dans le premier, on a $u_n\in I\; \forall n\in\mathbb N$ donc $u_{n+1}-u_n=g(u_n)<0$ et $u$ est strictement décroissante, non minorée sinon elle converge vers un point fixe qui serait inférieur à 1 ce qui est impossible : donc elle tend vers $-\infty$.  
# Dans le dernier, on a $u_n\in J\;\forall n\in\mathbb N$ donc $g(u_n)>0$ et $u$ est strictement croissante, majorée par $2$ ; ainsi $u$ converge vers un point fixe de $f$, qui ne peut être $1$ par croissance de $u$ : \begin{equation*}u_n\xrightarrow[n\to+\infty]{}2.\end{equation*}

# Pour finir, un petit aperçu du comportement de $(u_n)$ avec diverses valeurs de $u_0$ :

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

def f(x):
    '''Fonction de récurrence f'''
    return -(x-2)**2+2

def flot(u0,n):
    '''Construit les n premiers termes de la suite 
    de premier terme u0 vérifiant u_n+1 = f(u_n)'''
    L = [u0]
    for i in range(n): # construit les n premiers termes
        terme = L[-1]
        term_suiv = f(terme)
        L.append(term_suiv)
    return L


# In[2]:

def build_flow(prems,nmaxs,placement):
    """Construction des graphes des suites (u_n)"""
    nb_g = max(placement)+1
    fig,ax = plt.subplots(nb_g,1, figsize=(8,8))
    for i,[p, s, u0] in enumerate(zip(placement,styl,prems)):
        ax[p].plot(flot(u0,nmaxs[p]),s,label=r'$u_0={}$'.format(u0))
        # ajoute les points de la liste L au graphe
    for axi in ax:
        axi.grid()
        axi.legend(loc=0)
        axi.margins(y=0.06) # marge additionnelle sur l'axe des ordonnées
        axi.set_xlabel(r'$n$') # titre axe des abscisses
        axi.set_ylabel(r'$u_n$') # titre axe des ordonnées


# In[3]:

prems = [1, 2, 1.003, 2.91, 3.01, 0.996]
nmaxes = [16, 8]
placement = [0, 1, 0, 0, 1, 1]
styl = ['^--', '^--', 'p-.', '--.', 'p-.', '.-.']
build_flow(prems,nmaxes,placement)

