tokens = open("tokens.txt", "r").read().splitlines()

for token in tokens:
    mail = token.split(":")[0]
    pw = token.split(":")[1]
    tk = token.split(":")[2]
    with open("output/mails.txt", "a") as f:
        f.write(mail + "\n")
    with open("output/pass.txt", "a") as f:
        f.write(pw + "\n")
    with open("output/tokens.txt", "a") as f:
        f.write(tk + "\n")