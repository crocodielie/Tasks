numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summ = 0
for i in range(len(numbers)):
    if numbers[i] != None:
        summ += numbers[i]

new_num = summ / len(numbers)

for i in range(len(numbers)):
    if numbers[i] == None:
        numbers[i] = new_num

print("Измененный список:", numbers)
