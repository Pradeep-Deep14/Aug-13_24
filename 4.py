Str_var = "abcde"
rev_str_var=""

for i in range((len(Str_var)-1),-1,-1):
    rev_str_var+=Str_var[i]

print(rev_str_var)