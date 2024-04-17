statement = "a quick brown fox jumps over a lazy dog"
m=[(x.lower(),x.upper(),len(x)) for x in statement.split()]
print(m)
