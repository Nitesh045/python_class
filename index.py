# # print('hello world')

# # def add(a,b):
# #     return a+ b
# # totalsum=90
# # bonus=60
# # final = add(totalsum,bonus)
# # print(f"{final}")

# # cars=["bmw","audi","mesrati"]
# # print(cars.__len__())

# # def calculate_sum(x:int,y:int):
# #   """
# #   return the sum value
# #   """
# #   return x + y

# # total_Sum=10
# # bonusSum=20
# # finalScrore=calculate_sum(total_Sum,bonusSum)
# # print(f"data type of totalsum is {type(total_Sum)} and \n"+f"bonus_points is {type(bonusSum)}")
# # print(f"Final Scrore is {finalScrore}")

# # def calculatingInput(x:int,y:int):
# #   # function to calculate sum
# #   return x + y
# # # declare the input so take in int
# # sumoftotal=int(input("Enter your value of total sum "))
# # sumofbonus=int(input("Enter your value of total bonus "))
# # # call the function with value
# # totalSum= calculatingInput(sumoftotal,sumofbonus)
# # print(f"{totalSum}")

# # #\


# Apple_GST=0.12
# Orange_GST=0.05


# # buyer name 
# buyer_name= input("Enter buyer name :")
# apple_price_kg= int(input("Enter Apple price per kg: "))
# apple_quantity_kg=float(input("Enter apple Quantity: "))
# orange_price_kg=int(input("Enter Orange price per kg: "))
# orange_quantity_kg=float(input("Enter orange Quantity: "))
# # step 3 to calculate the price without gst
# total_priceApple= apple_price_kg * apple_quantity_kg
# total_priceOrange= orange_price_kg * orange_quantity_kg
# # calculate price with gst
# total_gst_priceA=total_priceApple * Apple_GST
# total_gst_priceO= total_priceOrange * Orange_GST
# # now evaluting total price of apple 
# priceofapple= total_priceApple +total_gst_priceA
# priceoforange= total_priceOrange +total_gst_priceO
# # total amount on bill 
# totalBillAm=priceofapple+priceoforange
# total_roundAmount= round(totalBillAm)


# print(f"\nBuyer name :{buyer_name}")
# print(f"{'-'*74}")
# print(f"| {'Item Code':^10} | {'Price/Unit':^10} | {'# unit':^5}",
#       f"| {'Price':^5} | {'GST':^10} | {'Total w/ GST':^10} |")
# print(f"{'-'*74}")
# print(f"| {'Apple':^10} | {'Rs'+str(apple_price_kg):^10} | {apple_quantity_kg:^5}",
#       f"| {'Rs'+str(total_priceApple):^5} | {'Rs'+str(total_gst_priceA):^10}",
#       f"| {'Rs'+str(total_gst_priceA):^10}")
# print(f"| {'Orange':^10} | {'Rs'+str(orange_price_kg):^10} | {orange_quantity_kg:^5}",
#       f"| {'Rs'+str(total_priceOrange):^5} | {'Rs'+str(total_gst_priceO):^10}",
#       f"| {'Rs'+str(total_gst_priceO):^10}")
# print(f"{'-'*74}")
# print(f"Total {' '*54} \u20b9 {totalBillAm:.2f}")
# print(f"Total Round {' '*48} \u20b9 {total_roundAmount:.2f}")
# print(f"{'-'*74}")


def addingSum(a:int,b:int):
    return a+ b

try:
    intialInput= int(input("enter first value : "))
    seconsValue=int(input("inter second value: "))
    finalValue=addingSum(intialInput,seconsValue)
    print(f"final value is {finalValue}")
except ValueError as err:
    print(f"Opps having error {err} ")
except:
    print(f"having error in input try angain")