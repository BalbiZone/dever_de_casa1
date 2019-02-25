

x = int(input('gimme num:\n'))


#100
ced_100 = x // 100
x = x - (ced_100 * 100)
#50
ced_50 = x // 50
x = x - (ced_50 * 50)
#20
ced_20 = x // 20
x = x - (ced_20 * 20)
#10
ced_10 = x // 10
x = x - (ced_10 * 10)
#5
ced_5 = x // 5
x = x - (ced_5 * 5)
#2
ced_2 = x // 2
x = x - (ced_2 * 2)
#1
ced_1 = x // 1
x = x - (ced_1 * 1)

print('CÉDULAS:\n100rs - {}\n50rs - {}\n20rs - {}\n10rs - {}\n5rs - {}\n2rs - {}\n1rs - {}\n'.format(ced_100, ced_50, ced_20, ced_10, ced_5, ced_2, ced_1))
print
