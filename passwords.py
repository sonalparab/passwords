def strong(password):
    lower = [c for c in password if c.islower()]
    upper = [u for u in password if u.isupper()]
    nums = [n for n in password if n.isdigit()]
    return len(lower) != 0 and len(upper) != 0 and len(nums) != 0

print "Strong?"
print strong("hey")
print strong("HELLO")
print strong("hi123bye")
print strong("Hi123bye")
print strong("Bye321Hi")
print

def strength(password):
    lower = [c for c in password if c.islower()]
    upper = [u for u in password if u.isupper()]
    nums = [n for n in password if n.isdigit()]
    alnum = [a for a in password if not a.isalnum()]

    #print lower
    #print upper
    #print nums
    #print alnum
    
    points = 0

    #a point for every two lowercase numbers
    points += len(lower)/2

    #a point for every two uppercase numbers
    points += len(upper)/2

    #a point for every number
    points += len(nums)

    #a point for every alphanumeric
    points += len(alnum)

    #if password meets has all the types of characters
    if (len(alnum) > 0 and strong(password) and points > 10):
        return 10
    #if a password is long but does not contain all types of characters
    elif points >= 10:
        return 8
    else:
        return points

print "Strength"
print strength("hey")
print strength("HELLO")
print strength("Hi123bye")
print strength("Hi123bye!")
print strength("SoftDev pd 8 rocks!")
