from rumus import luas_segitiga, keliling_segitiga

def posisi_angka(numbers):
    if not numbers or numbers[0] >= len(numbers):
        return -1
    return numbers[numbers[0] + 1]

list_number1 = (3, 10, 20, 30, 40)
list_number2 = (0, -10, 10)
list_number3 = (1, 2, 300, 10)
list_number4 = (100, 200, 300, -400)
list_number5 = (4, 200, 300, -400)

print(posisi_angka(list_number1)) 
print(posisi_angka(list_number2))  
print(posisi_angka(list_number3)) 
print(posisi_angka(list_number4)) 
print(posisi_angka(list_number5)) 


print(luas_segitiga(10, 20))
print(keliling_segitiga(10, 20, 30))