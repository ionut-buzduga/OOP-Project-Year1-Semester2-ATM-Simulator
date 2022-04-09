import random

class Card: #this class will be used to make the transactions in the ATM
  def __init__(self, cardNumber:int,pin:int, money:int,bank:str): 
    self.cardNumber = cardNumber
    self.pin = pin  #each card has a PIN security number consisting of 4 digits
    self.money=money
    self.bank=bank
  def setCardNumber(self):
    self.cardNumber=(random.randrange(1000000000,9999999999))
  def setPin(self):
    pin=(random.randrange(1000,9999))
  def setMoney(self,newValue:int):
    self.money=newValue
  def printDetails(self):     #this function will be used to print the details of each card
      print("CARD NUMBER:%d"%(self.cardNumber))
      print("PIN:%d"%(self.pin))
      print("BANK:%s"%(self.bank))
      print()

class CardList:#this class will be used to store all our cards and so we can choose which card we want to work with
    def __init__(self,cardlist): 
        self.cardlist=cardlist
    def addCard(self,card:Card):
        self.cardlist.append(card)
    def removeCard(self,card:Card):
        self.cardlist.remove(card)
    def printCardList(self,cardlist):
        for iterator in range(len(cardlist)):
            print("Press %d to choose this card"%(iterator+1))
            self.cardlist[iterator].printDetails()  

class Account:#this class is used to associate each Card object with an account
    def __init__(self,card:Card,bank:str):
        self.bank=bank
        self.card=card

class AccountList:#this class is used to hold all the accounts
    def __init__(self,acclist): 
        self.acclist=acclist
    def addAccount(self,acc:Account):
        self.acclist.append(acc)
    def removeAccount(self,acc:Account):
        self.acclist.remove(acc)
    def printAccountList(self,acclist):
        for iterator in range(len(acclist)):
            print(acclist[iterator].bank)
            

class Client:# the Client class will associate each Card and Account to a Client
    def __init__(self,name,account:Account,card:Card,cash:int):
        self.name=name
        self.account=account
        self.card=card
        self.cash=cash #this is where the money goes after the extraction from a card

class ClientList:#the ClientList class creates a list which holds all the clients
    def __init__(self,clientlist): 
        self.clientlist=clientlist
    def addClient(self,cl:Client):
        self.clientlist.append(cl)
    def removeClient(self,cl:Client):
        self.clientlist.remove(cl)
    def printClientList(self,clientlist): #this method is used to print all Client objects from the list
        for iterator in range(len(clientlist)):
            print(clientlist[iterator].name)
            print(clientlist[iterator].account.bank)

class ClientBank:#the ClientBank class is used to associate a client with a particular bank
    def __init__(self,bank_name,bank_money,client:Client): 
        self.bank_name=bank_name
        self.bank_money=bank_money



class ATMBank:#the ATMBank class will act as the bank which is associated with the ATM machine
    def __init__(self,bank_name,bank_money,fee):
        self.bank_name=bank_name
        self.bank_money=bank_money
        self.fee=fee   #here we have a fee which is taken into account if a client makes a transaction at an ATM that is not from his original bank
    def setFee(self,fee_value:int):
        self.fee=fee_value

class ATM:#this is the most important class which will execute all of our requirements for the problem:checking the balance,extracting money from the ATM,or making a transfer
  def __init__(self, money:int):
    self.money = money
  def myfunc(self,bank:ATMBank):
    print(bank.bank_name)
  def setMoney(self,newValue:int):
    self.money=newValue
  def printBalance(self,card:Card):#The printBalance method is used to print how much money does the chosen card hold at the moment
        print(card.money)
  def extractMoney(self,card,sumToExtract,bank:ATMBank,client:Client):#the extractMoney method Takes money from the card and puts it in cash form for our Client
      
        if(bank.bank_name==card.bank):#here we have the dependence between the client bank and the atm bank
           if(sumToExtract>card.money):#if the sum you want to extract exceeds the money available on the card then you will only get that sum in cash form
            client.cash=client.cash+card.money
            print("You could only extract %d money"%(card.money))
            card.money=0;
           else:
            client.cash=client.cash+sumToExtract
            card.money=card.money-sumToExtract
        else:
           if(sumToExtract+bank.fee>card.money): #if the name of the bank where the card is registered is different from the name of the ATM then you will get a FEE when extracting money
            client.cash=client.cash+card.money-bank.fee
            print("The fee has been applied")
            print("You could only extract %d money"%(card.money-bank.fee))
            card.money=0;
           else:
            client.cash=client.cash+sumToExtract
            card.money=card.money-sumToExtract-bank.fee;
  def transfer(self,crdl:CardList,bank:ATMBank,transfer_from:int,transfer_to:int,transfer_sum:int):#the transfer method allows a client to make a transfer of a sum between
      crdl.cardlist[transfer_from].money=crdl.cardlist[transfer_from].money-transfer_sum #two cards from the card list;
      crdl.cardlist[transfer_to].money=crdl.cardlist[transfer_to].money+transfer_sum
  def initTransaction(self,crdl:CardList,bank:ATMBank,it:int,client:Client):#using this method we will initialize the menu for our ATM 
      checkPin=int(input("\nPlease enter the pin number of 4 digits:\n"))#first we need to verify the credentials by introducing the PIN code corresponding to our current card in use
      if(crdl.cardlist[it].pin==checkPin):#the pin needs to be reintroduced after each transaction(this is to simulate how a real ATM behaves where after making a transaction you take the card out)
          print()                                                  #for the ATM menu there will be 3 options 
          print("---You are now using %s's ATM---"%(bank.bank_name))
          print()
          print("Press 1 to print the balance:\n")#to print the current sum of money on the current card
          print("Press 2 to extract money:\n")#to extract a sum of money from the card and to get it in cash form 
          print("Press 3 to transfer money to another card:\n")#to make a transfer between to cards
          option=int(input("Enter your option:\n"))
          if(option==1):
              self.printBalance(crdl.cardlist[it]) #we print the sum from the chosen chard(it-is an identifier which allows us to use different cards from the CardList)
          elif(option==2):
              sum_to_extract=int(input("Enter how much money you want to extract:")) #here we make an extraction after entering how much money we would like to extract
              self.extractMoney(crdl.cardlist[it],sum_to_extract,bank,client)
          elif(option==3):#this is the transfer option
              transfer_from=int(input("Choose the card where you want to transfer money from:"))-1 #this is the card number from where we want to transfer(for my example there will be only 2 cards in the cardlist))
              transfer_to=int(input("Choose the card where you want to transfer money to:"))-1#that means that you will only be able to choose from card number 1 or number 2
              transfer_sum=int(input("Choose how much money you want to transfer:"))
              if(transfer_sum<crdl.cardlist[transfer_from].money):#if the sum we want to transfer exceeds how much money we have available on the card then we will need
               self.transfer(crdl,bank,transfer_from,transfer_to,transfer_sum)#to enter another sum that is lower otherwise our transfer is not possible
               print("The sum of %d has been transferred successfully from card %d to card %d"%(transfer_sum,transfer_from+1,transfer_to+1))
              else: 
               print("The sum entered is bigger than the card's balance.Please initiate the transaction again and choose a lower sum.")
              
          else: print("invalid option")
      else: print("Card information is wrong")
  



        



