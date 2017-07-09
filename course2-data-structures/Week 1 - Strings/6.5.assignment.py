text = "X-DSPAM-Confidence:    0.8475"
init = text.find(' ')
number = float(text[init:])
print(number)
