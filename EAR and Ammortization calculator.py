#Ammortization Calendar Kyle Kehoe

rate = 0
years = 0
pv = 0
prin = 0
ear = 0
time = 0
count = 1
payment = 0

rate = float(input('What is the APR?'))
years = float(input('How many years is the loan expected to be?'))
pv = float(input('How much money is the loan for? :$'))
time = float(input('How frequently do you make payments per year? (Ex. if payments are monthly this would be 12):'))

#calculate EAR
ear = ((1+((rate/100)/time))**time)-1
print('Your Effective Annual Rate is:' , ear*100 , '%')


#make things periodic
rate= (rate/100)/time
#print('periodic rate is', rate ,)

#calculate payment
payment=pv/((((1+rate)**(time*years))-1)/(rate*(1+rate)**(time*years)))
print('Your monthly payment will be: $',payment)

#Calculate ammortization and print table
while count <= time*years:
#ear = interest
    ear=pv*rate
#prin of each payment
    prin=payment-ear
#end balance
    pv=pv-prin
#print each payment
    print('payment #',(round(count,2)), 'interest paid will be' , round(ear,2),' Amount towards principle is', round(prin,2), ' Remaining balance is', round(pv,2))
    count+=1
