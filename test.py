print("test case 1:", end=" ")
x = 1
if x != 1:
    print("fail")
    exit(1)
print("... pass")
# assert x == 1, \
#     exit(1)
print("test case 2:", end=" ")
x = 3
if x != 3:
    print("fail")
    exit(1)
# assert x == 3, \
#     "wrong"
print("test passed")
exit(0)
