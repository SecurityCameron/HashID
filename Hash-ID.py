#Hash Identifier
import time

# The two most common and largest hashing algorithms are 'MD5' and 'SHA'.
# This program identifies whether it is one or the other. This is a common,
# tool in Kali Linux via 'hash-identifier' so i decided to make a small copy,
# to ensure that no one uses MD5 or SHA anymore as it is easily cracked and identified

#Learnt that:
# - Text art is cool
# - MD5 and SHA are a certain length

# Resources:
# https://en.wikipedia.org/wiki/MD5#Pseudocode
# https://www.tunnelsup.com/hash-analyzer/
# https://www.reddit.com/r/AskNetsec/comments/8chw3s/what_are_good_cyber_security_programming_projects/
# https://stackoverflow.com/questions/3394503/maximum-length-for-md5-input-output

print ("""

############################################
#                          ___   __        #
#     |   |  __  _  |__     |   |  \       #
#     |---| |_| |_  |  |    |   |   |      #
#     |   | | |  _| |  |    |   |   |      #
#                          ___  |__/       #
#                                          #
############################################
""")
time.sleep(2)
# - Code for identifying MD5 Hash length - #
#Concluded MD5 Hashes are 32 long (checked with other hashes)
def MD5():
    
    md5 = '5d41402abc4b2a76b9719d911017c592'

    count = 0
    for i in md5:
        count+=1
    
        print ("MD5 is length:"+str(count))
        # MD5: length = 32



# - Code for identifying SHA Hash length - #

def SHA():
    
    #Sample Hash
    SHA = 'AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'

    count = 0
    for i in SHA:
        count+=1
    
        print ("SHA is length:"+str(count))
        # SHA: length = 40

#MD5()
#SHA()

def main():
    hash1 = input("Enter the hash you want to identify: ")
    if len(hash1) == 32:
        print ("Hash is MD5.")
        
    elif len(hash1) == 40:
        print ("Hash is SHA.")

    else:
        print ("Unrecognised Hash or the hash is plain text.")


main()







