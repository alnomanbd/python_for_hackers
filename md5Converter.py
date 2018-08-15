import hashlib
import sys
import time

print('''
==============================================================================================
       *    (                                                               
 (  `   )\ ) (  (             (                              )          
 )\))( (()/( )\))(            )\             )     (  (   ( /(  (  (    
((_)()\ /(_)|(_)()\   ___   (((_)  (   (    /((   ))\ )(  )\())))\ )(   
(_()((_|_))_ (()((_) |___|  )\___  )\  )\ )(_))\ /((_|()\(_))//((_|()\  
|  \/  ||   \ | __|        ((/ __|((_)_(_/(_)((_|_))  ((_) |_(_))  ((_) 
| |\/| || |) ||__ \         | (__/ _ \ ' \)) V // -_)| '_|  _/ -_)| '_| 
|_|  |_||___/ |___/          \___\___/_||_| \_/ \___||_|  \__\___||_|  
----------------------------------------------------------------------------------------------
Description: A simple program that converts your input to MD5 Hash.
Keywords: [Python 3, MD5 Hash, MD5 Hash Converter, MD5 Converter]
Aug 2018 v1.0
by
www.alnomanbd.com
----------------------------------------------------------------------------------------------                                                              
''')

while True:
    md5_len = '32'
    mystring = input("Enter String for MD5 Hashing > ")
    hash_obj = hashlib.md5(mystring.encode())

    print("")
    loading = "[+] Generating MD5 Hash : [-------------------]"
    for i in range(1,101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")

    print("\n[+] MD5 Hashing Completed with " + md5_len + " chars:")
    time.sleep(.5)
    x = "-"
    for i in range(1, int(md5_len) + 1):
        print(x, end="")
    print("")

    print(hash_obj.hexdigest())

    x = "-"
    for i in range(1, int(md5_len) + 1):
        print(x, end="")

    print("")
    print("")

    ask = input("You want convert another string ? [y/n] > ")
    if ask == 'y':
        print("")
        continue
    else:
        break
