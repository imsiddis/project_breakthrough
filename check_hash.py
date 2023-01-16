# This program will check a hash and give you the hash type.

import hashlib
import sys

hash = input("Enter hash: ")

hash_type = "" # This will be the hash type.

#=======================#
# Check if hash is MD5  #
#=======================#
if len(hash) == 32:
    hash_type = "MD5"
#=======================#
# Check if hash is SHA1 #
#=======================#
elif len(hash) == 40:
    hash_type = "SHA1"
#=========================#
# Check if hash is SHA224 #
#=========================#
elif len(hash) == 56:
    hash_type = "SHA224"
#=========================#
# Check if hash is SHA256 #
#=========================#
elif len(hash) == 64:
    hash_type = "SHA256"
else:
    print("Hash type not supported.")
    sys.exit()

print("Hash type: " + hash_type)
print("Hash: " + hash)
