'''
Created By:     Richard Payne
Created On:     8/4/17
Desc:           Using simple hashing functions against a simple string

Compatibility issue:
            If you get a error saying missing parentheses surround the print
            print statement with () as shown below:

            print ( "MD5: " + m.hexdigest() )                                     
'''


import hashlib

class simpleHashFunctions:

    INPUT = "This is a simple string"

    def md5Hash(INPUT):
        m = hashlib.md5()
        m.update(INPUT)
        print "MD5: " + m.hexdigest()

    def sha1Hash(INPUT):
        m = hashlib.sha1()
        m.update(INPUT)
        print "SHA1 : " + m.hexdigest()
    
    def sha256Hash(INPUT):
        m = hashlib.sha256()
        m.update(INPUT)
        print "SHA256: " + m.hexdigest()


    if __name__ == "__main__":
        print "Original string: " + INPUT
        md5Hash(INPUT)
        sha1Hash(INPUT)
        sha256Hash(INPUT)
    
