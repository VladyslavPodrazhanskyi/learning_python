"""
StringIO is a class that provides an in-memory stream,
which allows you to treat strings as file-like objects.
This can be useful when you want to work with string data as if
it were being read from or written to a file.
"""


from io import StringIO

# Create a StringIO object with initial content
buffer = StringIO("Hello, this is a StringIO example.")

# Read from the StringIO object
content = buffer.read()
print(content)

# Write to the StringIO object
buffer.write("Additional content.")
print(buffer.getvalue())  # Get the entire content of the buffer

# Close the buffer
buffer.close()
