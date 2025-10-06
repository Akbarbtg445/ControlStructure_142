n = int(input("Masukan nilai n unntuk batas deret fiibonachi: "))

a, b = 0,1

print("Deret Fibonachi hingga ",n," : ")
while a <= n:
    print(a, end=" ")
    a,b = b, a + b