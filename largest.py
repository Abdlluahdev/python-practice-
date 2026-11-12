# LEARNING NOTE: A  working version of
# largest(); ties are handled with >=.


# Fixed the incorrect comparison opreators
# (< -> >=)

# so ties are covered.
# All paths now end in a return;
# largest(5, 5, 3) returns 5.

def largest(a,b,c):

  #  a >= b: b cannot be the largest, so
  # only c can beat a

  # >= (not >) so ties go to this branch
  # instead of falling through.

      # a is the larger of (a, b)
      # check whether c beats it
  if a >= b:

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
print(largest(5,5,3))
print(largest(5,5,5))
