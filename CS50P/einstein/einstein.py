def energy(mass):
    c = 300000000
    return mass * pow(c,2)

def main():
    mass = int(input())
    en = energy(mass)
    print(en)

main()