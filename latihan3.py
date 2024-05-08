hasil = dict()

with open ("mbox-short.txt", "r") as file :
    for line in file :
        if line.startswith('From '):
            email = line.split()[1]
            hasil[email] = hasil.get(email, 0) + 1

print(hasil)
# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)