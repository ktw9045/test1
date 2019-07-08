# 2
print('kimtaewoo')

#3
def nucleotide(tide):
    if tide =='A':
        return 'Adenine'
    if tide =='T':
        return 'Thymine'
    if tide =='C':
        return 'Cytosine'
    if tide =='G':
        return 'Guanine'
print(nucleotide('A'))
print(nucleotide('T'))
print(nucleotide('G'))
print(nucleotide('C'))

#4
try:
    num = int(input("Enter : "))
    print(10/num)
except ZeroDivisionError:
    print("num can not 0")
except ValueError:
    print("input must exist")

$5
num = 5
result = 1

while num >0:
    result *= num
    num-=1
print(result)

