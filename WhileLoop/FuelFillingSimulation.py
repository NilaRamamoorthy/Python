#9. Fuel Filling Simulation
total=0
extra=0
while True:
    fuel=int(input("Enter Fuel in Litres: "))
    total+=fuel
    if fuel<=0:
        continue
    if total>=50:
        if total>50:
            extra=total-50
            total-=extra
            print(f"No extra {extra}L is allowed")
        print("Fuel reached the limit of 50L")
        break
