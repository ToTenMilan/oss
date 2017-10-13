# # s = 'azcbobobegghakl' #=> beggh
# # s = 'xvbszaacvqvhwp' #=> aacv
# s = 'zyxwvutsrqponmlkjihgfedcba' #=> z
# # s = 'xbrlevzcenwmnlad' #=> cenw

# Dont work for all cases

previousChar = ""
string = ""
longestString = ""
prevbyte = 0
currbyte = 0
index = -1
for char in s:
    index += 1
    currbyte = ord(char)
    try:
        if (currbyte > ord(s[index + 1])):
            string += char
    #   previousChar = char
      # print(currbyte)
            if prevbyte <= currbyte:
                prevbyte = currbyte

                if len(string) > len(longestString):
                    longestString = previousChar +string
          # print(longestString)
            else:
                string = ""
                prevbyte = 0
        # currbyte = 0
    except IndexError:
        pass

print(longestString)

# previous charbyte
# current charbyte
# string
# longest string

# iterate through chars
#   convert char to byte
#   if current charbyte is greater or equal than previous charbyte
#     append char to string
#     if this string is longer than longest string
#       this string becomes the longest string
#   else
#     zero the string
#     zero prev charbyte
#     zero curr charbyte

# previousChar = ''
# string = ""
# longestString = ""
# prevbyte = 0
# currbyte = 0
# for char in s:
#   currbyte = ord(char)
#   # print(currbyte)
#   if prevbyte <= currbyte:
#     prevbyte = currbyte
#     string += char
#     if len(string) > len(longestString):
#       longestString = string
#       # print(longestString)
#   else:
#     string = "" + char
#     prevbyte = 0
#     currbyte = 0

# print(longestString)

# s = 'azcbobobegghakl' #=> beggh
# s = 'xvbszaacvqvhwp' #=> aacv
# s = 'zyxwvutsrqponmlkjihgfedcba' #=> z
# s = 'xbrlevzcenwmnlad' #=> cenw


