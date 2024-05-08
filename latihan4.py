hasil = dict()

with open ("mbox-short.txt", "r") as file :
    for line in file :
        if line.startswith('From '):
            email = line.split()[1]
            email_ = email.split("@")[-1]
            hasil[email_] = hasil.get(email_, 0) + 1

print(hasil)