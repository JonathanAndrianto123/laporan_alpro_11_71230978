hasil = dict()

with open ("mbox-short.txt", "r") as file :
    for line in file :
        if line.startswith('From '):
            email = line.split()[1]
            hasil[email] = hasil.get(email, 0) + 1

print(hasil)
