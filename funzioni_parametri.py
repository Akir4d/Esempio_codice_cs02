def sottrazione(x,y):
    return x - y

def sottrazione_infallibile(x=1,y=1):
    return x - y

print("Sottrazione:", sottrazione(5, 4))
print("Sottrazione:", sottrazione(y=4, x=5))
print("Sottrazione Infallibile:", sottrazione_infallibile(5))
print("Sottrazione Infallibile:", sottrazione_infallibile(5, 2))
print("Sottrazione Infallibile:", sottrazione_infallibile(9,y=5))
print("Sottrazione Infallibile:", sottrazione_infallibile(y=5))