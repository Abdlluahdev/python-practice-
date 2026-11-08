# LEARNING NOTE: reconstructed buggy first
# attempt, not working code.

# Bug: inverted operators (< instead of >)
# and uncovered ties.

def largest(a,b,c):
  #use comparison operators
  if a <  b:

  # to compare between arguments
    if c < a:
     return c
    else :
       return a
  elif b < a:

    if c < b:

      return c
    else:
      return b

print(largest(7,5,2))
