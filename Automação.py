#potencia util PU = P * N
#rendimento N = PU/P
#fator de potencia FP = cosphi = P/S
#potencia ativa P = PU/N
#potencia reativa Q = Q^2 = S^2 - P^2
#potencia aparente S = S = P/FP
# triangulo das potencias - S^2 = P^2 + Q^2

#motor 1
PU = 0.13
FP = 0.58
N = 0.50
P = PU/N
S = P/FP
Q = (S**2 - P**2)**0.5

print("\nMOTOR 1 \n")
print(f"\na potência útil é {P:2f}KW")
print(f"a potência aparente é {S:2f}KVA")
print(f"a potência reativa é {Q:2f}KVAr")

#motor 2
PU = 75
FP = 0.85
N = 0.946
P = PU/N
S = P/FP
Q = (S**2 - P**2)**0.5

print("\nMOTOR 2 \n")
print(f"\na potência útil é {P:2f}KW")
print(f"a potência aparente é {S:2f}KVA")
print(f"a potência reativa é {Q:2f}KVAr")

#motor 3
PU = 300
FP = 0.89
N = 0.958
P = PU/N
S = P/FP
Q = (S**2 - P**2)**0.5

print("\nMOTOR 3 \n")
print(f"\na potência útil é {P:2f}KW")
print(f"a potência aparente é {S:2f}KVA")
print(f"a potência reativa é {Q:2f}KVAr")

#motor 4
PU = 1.1
FP = 0.75
N = 0.815
P = PU/N
S = P/FP
Q = (S**2 - P**2)**0.5

print("\nMOTOR 4 \n")
print(f"\na potência útil é {P:2f}KW")
print(f"a potência aparente é {S:2f}KVA")
print(f"a potência reativa é {Q:2f}KVAr")









