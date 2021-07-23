import base64

# toEncode = [0, 127, 255]    # 3 bytes * 8 bits/byte = 24 bits
#                             # 24 bits / 6 bits/char = 4 char
# toEncode = [116, 133, 150]    # 3 bytes * 8 bits/byte = 24 bits
#                             # 24 bits / 6 bits/char = 4 char
# print('toEncode: {}. toEncode len: {}'.format(toEncode, len(toEncode)))
# encoded = base64.b64encode( bytearray(toEncode) )
# print('encoded: {}. encoded len: {}'.format(encoded, len(encoded)))
# encode_str = encoded.decode(encoding='ascii')
# print(encode_str)
# data = base64.b64decode(encode_str)
# print(data)
# print(int.from_bytes(data,'big'))


print()
toEncode = -100620
toEncode_bytes = int.to_bytes(toEncode, 3, 'big', signed=True)
print(toEncode_bytes)
encoded = base64.b64encode( bytearray(toEncode_bytes) )
print(toEncode, encoded)
encode_str = encoded.decode(encoding='ascii')
print(encode_str)
data = base64.b64decode(encode_str)
print(data)
print( int.from_bytes(data,'big', signed=True))