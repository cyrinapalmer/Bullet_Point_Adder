#! python 3
# bulletPointAdder.py - Adds Wikipedia bullet to the start of each line in the clipboard

import pyperclip

data = pyperclip.paste()

lines = data.split("\n")

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

data = "\n".join(lines)
pyperclip.copy(data)
