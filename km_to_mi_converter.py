conversion = 0.621

def km_to_mi(km):
    mi=km*conversion
    return mi

def main():
    km = float(input("Enter your km value here:"))
    miles = km_to_mi(km)
    print(f"{km} km = {miles.2f} miles")
    
main()