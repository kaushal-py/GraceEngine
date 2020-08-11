# Demo file to test the working of running code.
import sys
from io import StringIO

# create file-like string to capture output
codeOut = StringIO()
codeErr = StringIO()

code = "print('Hello, world')\nprint('Second line')"

# capture output and errors
sys.stdout = codeOut
sys.stderr = codeErr

exec(code)

# restore stdout and stderr
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

# print(f(4))

s_error = codeErr.getvalue()
print("error:\n", s_error)

s_out = codeOut.getvalue()
print("Output--")
print(s_out)

codeOut.close()
codeErr.close()