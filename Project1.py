import pandas as pd

data = pd.read_csv("Ecommerce Purchases")
df = pd.DataFrame(data)
#-----------------------------------------------------
# 1. Display Top 10 Rows of The Dataset
print(data.head(10))

#-----------------------------------------------------
# 2. Check Last 10 Rows of The Dataset
print(data.tail(10))

#-----------------------------------------------------
# 3. Check Datatype of Each Column
print(data.info())

#-----------------------------------------------------
# 4. Check null values in the dataset
print(data.isnull().value_counts())

#-----------------------------------------------------
# 5. How many rows and columns are there in our Dataset? 
print(data.count(0))

# -----------------------------------------------------
# 6. Highest and Lowest Purchase Prices.
print(data["Purchase Price"].sort_values().tail())
print("-----------------------------------------")
print(data["Purchase Price"].sort_values().head())

#-----------------------------------------------------
# 7. Average Purchase Price
print(data["Purchase Price"].mean())

#-----------------------------------------------------
# 8. How many people have French 'fr' as their Language?
print(len(data[data["Language"]=='fr']))

#-----------------------------------------------------
# 9. Job Title Contains Engineer
print(len(data[data["Job"].str.contains('Engineer', case=False)]))

#-----------------------------------------------------
# 10. Find The Email of the person with the following IP Address: 132.207.160.22
print(data["Email"][data["IP Address"] == '132.207.160.22'])

#-----------------------------------------------------
# 11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
print(data["CC Provider"] == "Mastercard") and (data["Purchase Price"] > 50 )

#-----------------------------------------------------------------------------------------------
# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
print(data[data["Credit Card"]== 4664825258997302]["Email"])

#-----------------------------------------------------------------------------------------------
# 13. How many people purchase during the AM and how many people purchase during PM?
print(data["Purchase Price"][data["AM or PM"].str.contains("AM")].count())
print(data["Purchase Price"][data["AM or PM"].str.contains("PM")].count())

#-----------------------------------------------------------------------------------------------
# 14. How many people have a credit card that expires in 2020?
def fun ():
    count = 0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count = count + 1
    print(count)
fun()

#-----------------------------------------------------------------------------------------------
# 15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
list1 = []
for email in data["Email"]:
    list1.append(email.split('@')[1])

data['temp'] = list1

print(data['temp'].value_counts().head())