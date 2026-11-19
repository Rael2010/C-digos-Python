import secrets
chaveAES = secrets.token_bytes(32)
binario = ""
for i in chaveAES:
    binario+= format(i, "08b")
print(binario)