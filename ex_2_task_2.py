# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)



# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!
from ex_2_task_1 import is_valid_email_address as is_valid 

gave_up = False
attempts_left = 3

# your code - start

# create while loop to run
while attempts_left > 0: # as long as attempts left > 0 then execute code below
    email = input("Enter email address.") # create input box for user to type in email and set to var email
    attempts_left = attempts_left - 1 # take var attempts_left which is set to 3 and subtract 1 and set back to attempts_left

    r, s = is_valid(email) # call to is_valid function to check if email is valid and set result to r and error message str to s
    if r == None: # if result is None then
        print(email, "is valid.") # print the email and "is valid"
        break # stop the loop
    else: # if the result is not None then
        print(email, "is invalid!") # print str and "is invalid!"
        print("Reason:", s) # print str and the str s that has the error code from function is_valid
        print("Please enter a valid email.") # print str
        print("Number of attempts left:", attempts_left) # print str and number from attempts_left var
        continue # continue to run the loop -> program will start back at beginning and run through code as long as attempts_left > 0

# your code - end
if not gave_up:
    print("valid email", email)
else:
    print("invalid email", email)
