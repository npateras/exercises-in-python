def rot13(value):
    apotelesma=""
    for i in value:
        j = ord(i)
        if ((j>=ord('a')) and (j<=ord('z'))):
            if (j>ord('m')):
                j-=13
            else:
                j+=13
        elif ((j>=ord('A')) and (j<=ord('Z'))):
            if j>ord('M'):
                j-=13
            else:
                j+=13
        apotelesma+=chr(j)
    return apotelesma
print(rot13(raw_input('Kataxwriste tin protasi: ')))
