dict= {"maths":67,"physics":45,"english":52,"cse":78}

Q={"environmental":70,"csa":56}
dict.update(Q)
print(dict)

x = dict.fromkeys(dict)
print(x)

P= dict.values()
print(P)

Z= dict.copy()
print(Z)

A= dict.get("maths")
print(A)

B= dict.keys()
print(B)

C= dict.pop("english")
print(C)

H = dict.popitem()
print(H)

K= dict.setdefault("physics")
print(K)

Y = dict.clear()
print(Y)
