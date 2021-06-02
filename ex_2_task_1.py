# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    # your code here

    # search to see if s contains @ before looking at each str (A, B, C)
    t = "@" in s # set var t to true or false depending on if @ is in s
    if t == False:  # if t is false (@ is not found in s)
        return 1, 'Must have exactly one @!' 

    # create var A for first part of s pre @
    A = s.split('@')[0] # split s into list at @ and return index 0 to get str before @ and set to A
    if len(A) < 3 or len(A) > 16: # if A is < 3 or > 16 chars in length
        return 2, 'pre @ part must contain 3 - 16 alfanum chars'
    elif A.isalnum() == False: # if A is not alphanumeric
        return 3, 'pre @ part must only contain alfanum chars'

    # search to see if s contains .
    d = "." in s # set var d to true or false depending on if . is in s
    if d == False: # if d is false (. is not found in s)
        return 4, 'post @ part must have exactly one dot!'

    # create var B for 2nd part of s post @ and pre .
    B = s[s.index('@')+1:] # index s at @ and include the first character after @ until the end and set to B
    B = B.split(".")[0] # take B from above and split it at . and return index 0 to get str before . and overwrite to B
    if len(B) < 2 or len(B) > 8: # if B is < 2 or > 8 chars in length
        return 5, "part after @ and before . must contain 2 - 8 alfanum chars"
    elif B.isalnum() == False: # if B is not alphanumeric
        return 6, "part after @ and before . must only contain alfanum chars"
    
    # get str after .
    C = s.split('.')[1] # split s into list at . and return index 1 to get str after . and set to A
    g = C in "com edu org gov" # set var g to true or false depending on if C is in str
    if g == False: # if g is false (C is not found in str)
        return 7, "past-dot part invalid, must be from: com, edu, org, gov"

    #if s passes all previous conditions
    return None, "Seems legit"

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error