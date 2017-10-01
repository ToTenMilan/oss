# s = 'azcbobobegghakl' #=> 2
# s = 'robobooboobbobobobobbobbobboobobobobobb' #=> 11
# s = 'bobtbobykpobobfbobbbobboobtoboo' #=> 5
s = 'bboobmybobobybobc' #=> 3

index = -1
counter = 0
result = ""
for char in s:
    index += 1
    try:
      if char == "b" and s[index + 1] == "o" and s[index + 2] == 'b':
        counter += 1
    except IndexError:
      pass

print(counter)
