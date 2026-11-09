# LEARNING NOTE: reconstructed buggy first
# attempt, not working code.

# Fixed inverted operators (< -> >). and
# Known issue: ties are still uncovered,
# e.g. largest(5, 5, 3) returns None.

def largest(a,b,c):
  #use comparison operators
  if a >  b:

  # to compare between arguments
    if c > a:
     return c
    else :
       return a
  elif b > a:

    if c > b:

      return c
    else:
      return b

print(largest(7,5,2))
