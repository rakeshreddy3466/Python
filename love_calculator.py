def calculate_love_score():
    name1 = input("enter name 1").lower()
    name2 = input("enter name 2").lower()
    name = name1+name2
    print(name)  
    T = 0
    R = 0
    U = 0
    E = 0
    L = 0
    O = 0
    V = 0
    Y = 0    
    for x in name:
        if x == "t":
            T = T + 1
        if x == "r":
            R = R + 1
        if x == "u":
            U = U + 1
        if x == "e":
            E = E + 1            
    for x in name:
        if x == "l":
            L = L + 1
        if x == "o":
            O = O + 1
        if x == "v":
            V = V + 1
        if x == "e":
            Y = Y + 1  
    
    print(f"T occurs {T} times ")
    print(f"R occurs {R} times ")
    print(f"U occurs {U} times ")
    print(f"E occurs {E} times ")
    total1= T+R+U+E
    print(f"L occurs {L} times ")
    print(f"O occurs {O} times ")
    print(f"V occurs {V} times ")
    print(f"E occurs {E} times ")
    total2= L+O+V+E
    print(f"LOVE SCORE: {total1}{total2}")

calculate_love_score()