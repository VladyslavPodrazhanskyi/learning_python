import subprocess

# Run a shell command and capture its output
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print(type(result))
# Print the output and return code
print("Output:", result.stdout)
print("Return Code:", result.returncode)
