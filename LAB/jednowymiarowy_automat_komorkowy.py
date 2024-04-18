import random
print("podaj zestaw regul")
rule = f'{int(input()):08b}'
print("podaj dlugosc ciagu")
sequence_length  = int(input())
print("podaj liczbe krokow")
steps = int(input())
print(f"zasada: {rule} dlugosc ciagu: {sequence_length } liczba krokow: {steps}")

patterns = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
sequence = list("".join(random.choice('*_') for i in range(sequence_length+2)))

#sequence=list("_*_*_*_**__**__*_*_**_**__*__**_")
#sequence_length  = len(sequence)-2

sequence[0], sequence[-1] = sequence[-2], sequence[1] #uproszczone zapetlenie sekwencji

print(f"{'STEPS'.center(sequence_length*5, '_')}")
print(sequence[1:sequence_length +1])

for i in range(steps):
    temp = '_'
    for j in range(1, sequence_length+1):
        cur = int(rule[patterns.index(sequence[j-1]+sequence[j]+sequence[j+1])])
        #print(j-1, sequence[j-1], j, sequence[j], j+1, sequence[j+1], cur)
        sequence[j-1] = temp
        temp = '*' if cur else '_'
    sequence[sequence_length] = temp
    sequence[0], sequence[-1] = sequence[-2], sequence[1]
    print(sequence[1:sequence_length +1])
