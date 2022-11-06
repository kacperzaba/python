i = 0

while True:
    i += 1
    if i % 2 == 1:
    #sprawdzanie liczb parzystych
        continue
        #continue sprawia że pętla zaczyczyna się od nowa, z pominięciem warunków pod continue
    print(i)
    if i > 10:
        break 
print("Koniec")

