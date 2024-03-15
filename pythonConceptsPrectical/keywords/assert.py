x = "hello"

#if condition returns true, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
# assert x == "GoodBye"


"""
assert keyword is used when debugging code
you can write a message to be written if the code returns false,check the example below.
"""

assert x == "goodbye", "x should be 'hello'"