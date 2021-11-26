print(bytes(3))  # b'\x00\x00\x00'

print(b"Python Bytes")  # b'Python Bytes'
print(bytes("Python Bytes".encode("UTF-8")))  # b'Python Bytes'
print(bytes("Python Bytes", "utf8"))  # b'Python Bytes'

print(b"""First line    
Second line
Third line""")  # b'First line\nSecond line\nThird line'

#  convert bytes to string (decode)
byte_string = b"This is bytes"
string_from_bytes = byte_string.decode()
print("type: ", type(string_from_bytes), ", string: ", string_from_bytes)

# create a bytes object encoded using 'cp855'
x = b'\xd8\xe1\xb7\xeb\xa8\xe5 \xd2\xb7\xe1'
print(x)
# return a string using decode 'cp855'
y = x.decode('cp855')
print(y)    # привет мир




print(bytearray(3))  # bytearray(b'\x00\x00\x00')
print(bytearray("ifs2847sfhshf".encode("UTF-8")))  # bytearray(b'ifs2847sfhshf')
