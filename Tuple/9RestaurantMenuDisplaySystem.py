
# 9. Restaurant Menu Display System
menu = [
    (101, 'Idli', 30),
    (102, 'Dosa', 50),
    (103, 'Vada', 20)
]
for iid, name, price in menu:
    print(f"{iid}. {name} - Rs.{price}")
expensive = max(menu, key=lambda x: x[2])
print("Most expensive item:", expensive[1])
