# 6. Unpack siblings and parents from family_members

family_members = ("naman","kamal","kriya","Jethalal","Daya")

# (siblings1,siblings2,siblings3,*parents) = family_members
siblings,parents = family_members[:3],family_members[3:]

print(siblings)
print(parents)