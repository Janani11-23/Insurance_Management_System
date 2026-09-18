class Insurance:
    CompanyName='SafeDrive'
    HeadOffice='Chennai'
    def __init__(self,name,policy_no,pin,sum_assured):
        self.name=name
        self.__policy_no=policy_no
        self.__pin=pin
        self.__sum_assured=sum_assured
        self.__premium=0
        self.__last_transaction='no transaction yet done'
    def __authenticate(self):
        Policy_no=int(input('enter policy_no here:'))
        Pin=int(input('enter pin_no here:'))
        return Policy_no==self.__policy_no and Pin==self.__pin
    def __generate_receipt(self,type,amount):
        return f'''
        ============INSURANCE TRANSACTION RECEIPT==============
        Company:{self.CompanyName}
        Headoffice:{self.HeadOffice}
        Vehicle Category:{self.VehicleCategory}
        policy holder:{self.name}
        policy number:{self.__policy_no}
        tnx type:{type}
        tnx amount:{amount}
        sum assured:{self.__sum_assured}
        current preminum:{self.__premium}
        '''
    def __calculate_base_premium(self):
        return self.__sum_assured*0.03
    def buy_policy(self):
        premium=self.__calculate_base_premium()
        self.__premium=premium
        self.__last_transaction=self.__generate_receipt('BUY POLICY',premium)
        print(f'policy purchased successfully,initial premium:{premium}')
    def pay_premium(self):
        if self.__authenticate():
            amount=int(input('Enter premium amount to pay:'))
            if amount>0:
                self.__premium+=amount
                self.__last_transaction=self.__generate_receipt('PAY PREMIUM',amount)
                print('Premium paid successfully')
            else:
                print('Invalid amount')
        else:
            print('Aunthentication failed')
    def claim_policy(self):
        if self.__authenticate():
            amount=int(input('Enter claim amount to pay:'))
            if amount>0 and amount<=self.__sum_assured:
                self.__sum_assured-=amount
                self.__last_transaction=self.__generate_receipt('CLAIM',amount)
                print('Claim process sucessfully')
            else:
                print('Invalid claim or exceeds sum assured')
        else:
            print('Authentiation failed')
    def show_policy_details(self):
        if self.__authenticate():
            print('=======================')
            print(f'company         :{self.CompanyName}')
            print(f'Vehicle Catagory:{self.VehicleCategory}')
            print(f'Name            :{self.name}')
            print(f'Policyno        :{self.__policy_no}')
            print(f'Sum Assured     :{self.__sum_assured}')
            print('========================')
        else:
            print('Authentication failed')
    def show_premium(self):
        if self.__authenticate():
            print(f'Current premium:{self.__premium}')
        else:
            print('Authentication failed')
    def list_last_transaction(self):
        if self.__authenticate():
            print(self.__last_transaction)
        else:
            print('Authentication failed')
class CarInsurance(Insurance):
    VehicleCategory='Four wheeler car'
    def __init__(self,name,policy_no,pin,sum_assured,car_number):
        super().__init__(name,policy_no,pin,sum_assured)
        self.__car_number=car_number
    def _Insurance__calculate_base_premium(self):
        return self._Insurance__sum_assured*0.05
class BikeInsurance(Insurance):
    VehicleCategory='two wheeler bike'
    def __init__(self,name,policy_no,pin,sum_assured,bike_number):
        super().__init__(name,policy_no,pin,sum_assured)
        self.__bike_number=bike_number
    def __calculate_base_premium(self):
        return self.__sum_assured * 0.02
car1=CarInsurance('bablu',22555,2255,500000,'TN01AB1234')
bike1=BikeInsurance('ramu',22666,2266,100000,'TN02CD5678')
while True:
    print('''
    ============WELCOME TO SAFEDRIVE INSURANCE=============
    1.buy policy
    2.pay premium
    3.claim policy
    4.show policy details
    5.show premium
    6.list last transaction
    7.exit
    ''')
    choice=int(input('enter your choice:'))
    if choice in range(1,7):
          Vehicle_choice=input('select vehicle- car or bike:').strip().lower()
          obj=car1 if Vehicle_choice=='car' else bike1 if Vehicle_choice=='bike' else None
          if obj is None:
             print('please type "car" or "bike"')
             continue
    if choice==1:
        obj.buy_policy()
    elif choice==2:
        obj.pay_premium()
    elif choice==3:
        obj.claim_policy()
    elif choice==4:
        obj.show_policy_details()
    elif choice==5:
        obj.show_premium()
    elif choice==6:
        obj.list_last_transaction()
    elif choice==7:
        print('''
        ================THANKYOU ,DRIVE SAFE===============
        ''')
        break
    else:
        print('enter valid choice number')

   
        
            
                  
            
        
                            
