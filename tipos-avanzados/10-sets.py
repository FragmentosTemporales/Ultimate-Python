# set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo) # | se llama unión y es para unir los set
print(primer & segundo) # & se llama intersección y busca los valores que se repiten en los set
print(primer - segundo) # - se llama diferencia y busca los valores que no coinciden en los set sin incluir datos en el primer set
print(primer ^ segundo) # ^ se llama diferencia simétrica y retorna los números que no coinciden incluyendolos en el primer set
