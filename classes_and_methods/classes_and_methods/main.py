from classes_and_methods import Account, AccountList,Card,CardList,ATM,ATMBank,Client,ClientList,ClientBank 

#This will be our main program where we test our classes and implemented methods
#for simplicity purposes we will work with only one client

client_name=str(input("Choose your client's name:"))#here we introduce our client name 
client_bank=str(input("Choose your client's bank(Recommended name:--BRD--):"))#here we get with input from keyboard the name of the bank
#if we want to test the ATM without a fee added it is recommended to enter "BRD"(because it is the same name as the ATM bank name)
#if we want to have a fee you can enter any other name
client_card=Card(3215513232,1234,2000,client_bank) #here we create our first card which we will use to test the problem
client_acc=Account(client_card,client_bank)#the card is added to an account
client_card1=Card(8473822315,2222,100,client_bank)#and here we have another created card(it is used to test the transfer function between two cards)
client_acc1=Account(client_card1,client_bank)#in the same account as aboze we put the second card as well
client1=Client(client_name,client_acc,client_card,0)#here we have our test Client object which will have the account and the cards created associated
cl_Bank=ClientBank(client_bank,1000000,client1) #this is the bank where our client is associated

#here we will create 3 lists to hold all of our information so we can choose between object more easily
cl=[]
clientlist=ClientList(cl)   #for our example this list holds a single client
clientlist.addClient(client1)

acc=[]
acclist=AccountList(acc)  #for our example this list holds a single account
acclist.addAccount(client_acc)

crd=[]
crdlist=CardList(crd)      #for our example this list holds a two cards
crdlist.addCard(client_card)

#next we will add the two cards to the cardlist and the print their details so it is easier to follow during the execution of the program

print("\n--Here is a list of all of your cards--\n")
clientlist.addClient(client1)
crdlist.addCard(client_card1)
acclist.addAccount(client_acc1)
crdlist.printCardList(crd)

#here we will be asked if we want to open the ATM,and to do so you will need to press 1
print("Do you want to go to the ATM?")
print("Press 1 if YES||Press 0 if NO")
opt=int(input())


if(opt==1):
  #next we will be asked to enter one of our cards in the ATM
  #for this set of cards that I provided above we will have only two option(1 for the first card||2 for the second one)
  current_card=int(input("Choose which Card you would like to introduce in the ATM\n(by pressing the number corresponding to the card from the list above):"))
  if((current_card>len(crdlist.cardlist)) or (current_card==0)):      
            while((current_card>len(crdlist.cardlist)) or (current_card==0)):
             print("Invalid option!")
             current_card=int(input("Choose which Card you would like to introduce in the ATM\n(by pressing the number corresponding to the card from the list above):"))
  newATM_bank=ATMBank("BRD",2000000,5) #this is our atm bank which can be the same as the client bank or different
  newATM=ATM(50000) #and this is our ATM objects which holds an amount of money
  
  while(opt==1):#the atm menu will appear multiple times if we want to execute multiple transactions(for this we use a while cycle)
   newATM.initTransaction(crdlist,newATM_bank,current_card-1,client1) #this is the method that shows the ATM menu and all the actions available
   opt=int(input("Do you want to execute another transaction with this current card?---1(YES)---0(NO)")) #here you will be asked if you finished working with the current card
   #and if you want to choose another one
   if(opt==0):
       opt=int(input("Do you want to choose another card?-----1(YES)---0(NO)"))
       if(opt==1):
        current_card=int(input("Choose which Card you would like to introduce in the ATM:"))#for our example you need to press 1 or 2(otherwise there  are not enough cards created)
        if((current_card>len(crdlist.cardlist)) or (current_card==0)):      
            while((current_card>len(crdlist.cardlist)) or (current_card==0)):
             print("Invalid option!")
             current_card=int(input("Choose which Card you would like to introduce in the ATM\n(by pressing the number corresponding to the card from the list above):"))
        
#after exiting the ATM machine the program is going to print how much money we have extracted from our cards
print("%s has now %d money in cash"%(client1.name,client1.cash))


