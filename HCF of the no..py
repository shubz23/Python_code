def f_hcf(a, b):
   while(b):
       a, b = b, a % b
   return a

hcf = f_hcf(19,47)
print("The HCF is", hcf)
