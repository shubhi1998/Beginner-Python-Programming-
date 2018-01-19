x='X-DSPAM-Confidence:0.8475'
str1 = x.find(':')
str2 = x[str1+1:]
float(str2)
print(str2)
