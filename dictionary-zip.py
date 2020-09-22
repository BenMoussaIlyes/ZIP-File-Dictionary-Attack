import zipfile
from os import path
from tqdm import tqdm
while(1):
	wordlist = input("wordlist file : ")
	if (path.exists(wordlist) ) :
		break
	print("[-] File does not exist")

while(1):
	zip_file = input("Zipfile : ")
	if (path.exists(zip_file) ) :
		break
	print("[-] File does not exist")

 

zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")