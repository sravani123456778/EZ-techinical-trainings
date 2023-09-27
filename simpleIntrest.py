'''swajith is having 1 lakh in his bank account in that rate of intrest is 12% per annum in the 5th month swajith is withdrawing
rupees 25,000 in inorder to buy gift for his loved one in the ninth month 10,000 is been deposited in order to give for second
loved one by end of the financial year,does how much swajith having in his bank account?'''
total_amount=int(input(""))
i=int(input())
m5=int(input())
m9=int(input())
intrest_upto_5months=(total_amount*4/12*i)/100
intrest_upto_9months=(total_amount-m5*4/12*i)/100
remaining_months=((total_amount-m5+m9)*4/12*i)/100
print((total_amount-m5+m9)+intrest_upto_5months+intrest_upto_9months+remaining_months)
