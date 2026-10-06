#kalau tambah input sini minit dia ada sudah tapi customer dia tidak kena count 
#like input minit = 20 tapi dalam while customer masih 0 tapi minit ada suda 
total_minutes = 0
customers = 0

while total_minutes < 60 :
    minutes = int(input())
    customers += 1
    total_minutes += minutes


print(customers)
print(total_minutes)
