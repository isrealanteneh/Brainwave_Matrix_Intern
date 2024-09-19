class Owner():
    def __init__(self, cardNum,pin, firstName, lastName, balance):
        self.cardNum = cardNum 
        self.pin = pin 
        self.firstName = firstName 
        self.lastName = lastName 
        self.balance = balance 
    
    #getter functions
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_balance(self):
        return self.balance
    
    # setter functions
    def set_cardNum(self,newVal):
        self.cardNum = newVal     
    def set_pin(self,newVal):
        self.pin = newVal
    def set_firstName(self,newVal):
        self.firstName = newVal
    def set_lastName(self,newVal):
        self.lastName = newVal
    def set_balance(self,newVal):
        self.balance = newVal
    

account_owners = []

# initializing the Owner class
account_owners.append(Owner(1692708020619256,2271," Israel"," Anteneh",20.00))
account_owners.append(Owner(2764590867554412,9140,"Bernabas", "Anteneh", 25.00))
account_owners.append(Owner(9112597031565441,5590,"Nathan","Anteneh", 10.00))
account_owners.append(Owner(2380567445678140,2064,"Shalom","Anteneh", 30.00))
account_owners.append(Owner(2340607940604023,4350,"Joshua", "Anteneh", 40.00))
