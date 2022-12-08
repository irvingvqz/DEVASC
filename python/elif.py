aclNum=int(input("cual es el numero IPV4 ACL?: "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPv4 Estandar.")
elif aclNum >=100 and aclNum <= 199:
    print("Este es una ACL IPV4 extendida.")
else:
    print("Esta ACL IPv4 no es extendida o estandar.")