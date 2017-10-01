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

    # if char == "b":
    #   result += char
        # secondIndex = index + 1
        # for secondChar in s[index:-1]:
        #     if secondChar == "o":
        #         for thirdChar in s[secondIndex:-1]:
        #             if thirdChar == "b":
        #                 counter += 1
        #                 index += 2
        #                 break
print(counter)
