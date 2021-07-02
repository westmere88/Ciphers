from factordb.factordb import FactorDB



def n (p,q):
    return p*q

def pq (n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

def p (n):
    return pq[0]

def q (n):
    return pq[1]

def totient(p,q):
    return (p-1)*(q-1)

def d(e,totient):
    return pow(e,-1,totient)

def c(m,e,n):
    return (m**e)%n

def m(c,d):
    return (c**d)%n