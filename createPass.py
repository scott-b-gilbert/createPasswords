#!/bin/python3

from random import randint
from xkcdpass import xkcd_password as xp

wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist( wordfile = wordfile, min_length=5, max_length=6, valid_chars='.')

password = xp.generate_xkcdpassword( mywords, numwords=4, delimiter='-' )

# still need to randomly replace 1 letter with number and 1 letter with Capital

index1 = -1
index2 = -1
# create and replace capital letter
while( True ):
    index1 = randint( 0, len(password))
    if( password[index1] == "-"):
        continue
    else:
        if ( index1 + 1 ) > len( password ):
            password = password[ 0:index1 ] + password[ index1 ].upper()
        else:
            password = password[ 0:index1 ] + password[ index1 ].upper() + password[ index1+1:len(password)+1 ]
        break
#create and replace number
while( True ):
    index2 = randint( 0, len(password))
    replaceNum = randint(0, 9)
    if(index1 == index2 ) or ( password[index2] == "-"):
        continue
    else:
        if ( index2 + 1 ) > len( password ):
            password = password[ 0:index2 ] + str(replaceNum)
        else:
            password = password[ 0:index2 ] + str( replaceNum ) + password[ index2+1:len(password)+1 ]
        break

print( password )