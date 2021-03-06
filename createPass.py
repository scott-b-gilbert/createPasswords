#!/bin/python3
import sys
from random import randint
from xkcdpass import xkcd_password as xp

wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist( wordfile = wordfile, min_length=5, max_length=6, valid_chars='.')
password = ''
tries=500
minWords=6
while (len(password) == 0) or (len(password) > int(sys.argv[1])): 
    if tries == 0:
        minWords = minWords - 1
        tries=500
    password = xp.generate_xkcdpassword( mywords, numwords=minWords, delimiter='-' )
    tries = tries - 1
    print("{}".format(len(password)))
index1 = -1
index2 = -1
# create and replace capital letter
while( True ):
    index1 = randint( 0, len(password) - 1)
    try:
        if( password[index1] == "-"):
            continue
        else:
            if ( index1 + 1 ) > len( password ):
                password = password[ 0:index1 ] + password[ index1 ].upper()
            else:
                password = password[ 0:index1 ] + password[ index1 ].upper() + password[ index1+1:len(password)+1 ]
            break
    except IndexError:
        print("Length of password: {}.  Index1 value: {}".format(len(password), index1))
        exit
#create and replace number
while( True ):
    index2 = randint( 0, len(password) - 1)
    replaceNum = randint(0, 9)
    try:
        if(index1 == index2 ) or ( password[index2] == "-"):
            continue
        else:
            if ( index2 + 1 ) > len( password ):
                password = password[ 0:index2 ] + str(replaceNum)
            else:
                password = password[ 0:index2 ] + str( replaceNum ) + password[ index2+1:len(password)+1 ]
            break
    except IndexError:
        print("Length of Password: {}.  Index1 value: {}. Index2 value: {}".format(len(password), index1, index2))
        exit
print("Length of password: {}".format(len(password)))
print( password )
