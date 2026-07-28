def electricity_bill(e_bill):
   return(e_bill*3 if 0 <=e_bill<=100 
   else e_bill*5 if 101 <=e_bill<=300 
   else e_bill*7 )

bill = electricity_bill(80)
print(f"Bill: ¥{bill}")
bill = electricity_bill(200)
print(f"Bill: ¥{bill}")

bill = electricity_bill(450)
print(f"Bill: ¥{bill}")