print('''
████████╗░█████╗░██╗░░░██╗███████╗░██████╗██╗░░██╗
╚══██╔══╝██╔══██╗╚██╗░██╔╝██╔════╝██╔════╝██║░░██║
░░░██║░░░██║░░██║░╚████╔╝░█████╗░░╚█████╗░███████║
░░░██║░░░██║░░██║░░╚██╔╝░░██╔══╝░░░╚═══██╗██╔══██║
░░░██║░░░╚█████╔╝░░░██║░░░███████╗██████╔╝██║░░██║
░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░╚═╝''')
f=open("website.txt","r")
print("IP\t\tDATE/TIME\t\t\tGET REQUEST\t\tHTTP/VERSION\t\tSTATUS\tPACKET SIZE")
print()
lines=f.readlines()
nf=open("output.txt","w+")
nf.write("IP\t\tDATE/TIME\t\t\tGET REQUEST\t\tHTTP/VERSION\t\tSTATUS\tPACKET SIZE")
for line in lines:
    line=line.replace('"',"")
    line=line.split(" ")
    nf.write(f"{line[0]}\t{line[3]}+{line[4]}\t{line[5]}\t\t\t{line[7]}\t\t{line[8]}\t\t{line[9]}\n")