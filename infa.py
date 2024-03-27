from itertools import product, combinations, permutations

m = input()
n = input()
s = input()
mast = ['бубен', 'пик', 'треф', 'червей']
m = m.replace('буби', 'бубен')
m = m.replace('пики', 'пик')
m = m.replace('трефы', 'треф')
m = m.replace('черви', 'червей')
kart = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
del kart[kart.index(n)]
p = [' '.join(x) for x in product(kart, mast)]
v = [', '.join(x) for x in combinations(p, 3) if any(['1' for i in x if m in i.split()])]
print(v[v.index(s) + 1])
