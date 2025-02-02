#Heads: 35, legs:94
def solve(numheads, numlegs):
    for chicken in range(numheads+1):
        rabbit=numheads-chicken
        if chicken*2+4*rabbit==numlegs:
            return f"Chicken: {chicken}, rabbit: {rabbit}"
        
    return "No solution"


heads=int(input("Heads:"))
legs=int(input("Legs:"))
print(solve(heads, legs))