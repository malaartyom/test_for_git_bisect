a = [1, 2, 3, 4, 5]
for i in range(5):
    print(a[i])
a.reverse()
print()
for i in range(5):
    print(a[i])
print()
for i in range(5):
    for j in range(5):
        print(a[i] + a[j])