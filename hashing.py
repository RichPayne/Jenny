'''
Created By:     Richard Payne
Created On:     8/4/17
Desc:           Using simple hashing functions against a simple string

Compatibility issue:
            If you get a error saying missing parentheses uncomment the print statements with python 3
            next to them and comment out those with python 2 next to them.
'''

import hashlib

class simpleHashFunctions:

    INPUT = "This is a simple string"

    def md5Hash(INPUT):
        m = hashlib.md5()
        m.update(INPUT)
        print "MD5: " + m.hexdigest() #Python 2
        #print ("MD5: " + m.hexdigest()) #Python 3

    def sha1Hash(INPUT):
        m = hashlib.sha1()
        m.update(INPUT)
        print "SHA1 : " + m.hexdigest() #Python 2
        #print ("SHA1 : " + m.hexdigest()) #Python 3
    
    def sha256Hash(INPUT):
        m = hashlib.sha256()
        m.update(INPUT)
        print "SHA256: " + m.hexdigest() #Python 2
        #print ("SHA256: " + m.hexdigest()) #Python 3

    if __name__ == "__main__":
        print "Original string: " + INPUT #Python 2
        #print ("Original string: " + INPUT) #Python 3
        md5Hash(INPUT)
        sha1Hash(INPUT)
        sha256Hash(INPUT)
