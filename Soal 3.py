import math

P = 200_000_000  
A = 400_000_000  
r = 0.10  

t = math.log(A / P) / math.log(1 + r)

print("Waktu yang dibutuhkan untuk mencapai 400 juta adalah",round (t, 2), "tahun.")
