cart = ["milk", "bread", "eggs", "milky"]  # duplicates OK!
print(cart[0])
print(cart[-1])
print(cart[1:-2])
# ekhanei value update hocche
cart[1]="banana" 
# ekhanei value index wise add hocche
cart.insert(2,"guava")
# extend eksathe onek gula value rakhe


# ei 2 vabe extend kora jay
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
cart.extend(["lichi","pinaapple"])
# only 1 ta rakha ajabe
cart.append("dragon fruit")
# [1:1] মানে index 1 থেকে index 1 পর্যন্ত খালি জায়গা (empty slice)।
# তাই 10, 20 ওই জায়গায় ঢুকে যায়, আর বাকি value গুলো ডানে সরে যায়।
cart[1:1] = [10, 20]

#kintu [1:2] emon hole age 1 theke 2 e jay 2 no index kisu thakle remove kore dhuke
cart[2:3] = [30, 40]
#

print(cart)