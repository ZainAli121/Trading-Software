balance=6000
withdraw=0
deposit=0
doge_coin=0
bit_coin=0
doge_coin_value=100
bit_coin_value=150
doge_coin_Purchased=0
bit_coin_Purchased=0

#transactions[4]={0,0,0,0}
transactions=[0,0,0,0]
#------------deposit money--------------
def deposit_money(money):
  global deposit,balance
  deposit+=money
  balance+=money
  transactions[0]=deposit
  return True

#-------------Withdraw money_______________
def withdraw_money(money):
  global withdraw,balance
  if money<=balance:
    withdraw+=money
    balance-=money
    transactions[1]=withdraw
    return True
  else:
    return False

#-------------Account Details-----------------
def get_acc_info():
  print("\nYour Banking Details")
  print("Your Bank Balance is: ",balance,"$")
  print("Your Dogecoin Details: ",doge_coin_Purchased,"$")
  print("Your Bitcoin Details: ",bit_coin_Purchased,"$\n")

#--------------Crypto Buying------------------------
def buy_cryoto():
  global doge_coin_Purchased,doge_coin_value,bit_coin_Purchased,bit_coin_value,balance
  print("\nAt this stage one Degecoin's worth is: ",doge_coin_value)
  print("At this stage one Bitcoin's worth is: ",bit_coin_value)
  print("\nEnter 1 for Dogecoin purchasing and \n2 for bitcoin purchasing\n")
  res=input("Enter tour response here: ")
  if res=='1':
    balance-=doge_coin_value
    doge_coin_Purchased+=doge_coin_value
  elif res=='2':
    balance-=bit_coin_value
    bit_coin_Purchased+=bit_coin_value
  else:
    print("Inavlid Key Entered\nPlease try again later!")
  transactions[2]=doge_coin_Purchased
  transactions[3]=bit_coin_Purchased
  print("\nCrypto Coins Successflly Purchased")
  return True

#--------------------Crypto Selling-------------------------------
def sell_crypto():
  global doge_coin_Purchased,bit_coin_Purchased,doge_coin_value,bit_coin_value,balance
  print("\nEnter 1 for dogecoin selling and 2 for bitcoin")
  res=input("\nRegister your response here: ")
  if res=='1':
    if doge_coin_Purchased!=0:
      balance+=doge_coin_value
      doge_coin_Purchased-=doge_coin_value
      print("\nCrypto selled successfully")
      return True
    else:
      print("\nInsufficient Balance!")
      return False
  elif res=='2':
    if bit_coin_Purchased!=0:
      balance+=bit_coin_value
      bit_coin_Purchased-=bit_coin_value
      print("Crypto selled successfully")
      return True
    else:
      print("Insufficient Balance!")
      return False
  else:
    print("Invalid Key Entered!")
  transactions[2]=doge_coin_Purchased    
  transactions[3]=bit_coin_Purchased

#---------------------------Getting Account history-----------------------
def acc_history():
  print("\nHere is your all transactions history")
  print("Deposited Amount is: ",transactions[0])
  print("Withdrawm Amount is: ",transactions[1])
  print("Dogecoins purchased are : ",transactions[2])
  print("Bitcoins purchased are : ",transactions[3])
  print("Total Crypto investment is : ",transactions[2]+transactions[3],"\n")


#------------------Main----------------------------------
while True:
  title='Trading Software'.center(31,'=')
  print("*******************************")
  print(title)
  print("*******************************")
  print("Enter 1 for Depositing Money")      
  print("Enter 2 for Withdrawing Money")      
  print("Enter 3 for Account Information")      
  print("Enter 4 for Transactions History")      
  print("Enter 5 for Buying Crypto")      
  print("Enter 6 for Selling Crypto")
  print("*******************************\n")

  res=input("Register your response here: ")
#------------Deposit---------------
  if res=='1':
    amount=int(input("\nEnter the amount to be deposited: "))
    ans=deposit_money(amount)
    if ans:
      print("\nMoney Deposited Successfully\n")
    else:
      print("Request Failed!")
  
#------------    Withdraw    ---------------
  elif res=='2':
    amount=int(input("\nEnter the amount to be Withdrawn: "))
    ans=withdraw_money(amount)
    if ans:
      print("\nMoney Withdrawn Successfully\n")
    else:
      print("Insufficient Balance!")
  
#---------------------Acc Info----------------------------------
  elif res=='3':
    get_acc_info()
  

#---------------------------------History----------------------------
  elif res=='4':
    acc_history()

#---------------------------Buying crypto-------------------------------
  elif res=='5':
    ans=buy_cryoto()
    if (ans):
      print("")
    else:
      print("Sorry!\n")

#---------------------------Selling crypto--------------------------------
  elif res=='6':
    ans=sell_crypto()
    if ans:
      print("Done\n")
    else:
      print("sorry!\n")

#============================All Done------------------=========================
  else:
    print("\nInvalid Key entered!\nTry Again!")
  
  

  
