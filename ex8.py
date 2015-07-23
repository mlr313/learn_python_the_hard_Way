# this line equates "formatter" with four iterations of %r.
formatter = "%r %r %r %r"

# this line prints 1, 2, 3, 4. They are integers and do not need quotations 
print formatter % (1, 2, 3, 4)
# this line prints the words "one" "two" "three" and "four"
print formatter % ("one", "two", "three", "four")
# this line prints the keywords true and false; they do not need quotations as they are keywords
print formatter % (True, False, False, True)
# this line prints four iterations of "formatter", each of which are four iterations of %r.
print formatter % ( formatter, formatter, formatter, formatter)
# different double and single quotes are used with %r because %r is for debugging and therefore the simplest form of quotes (since they are interchangale) will be used.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
