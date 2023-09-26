import requests
from time import sleep
from datetime import datetime


debugMsgOn = False


'''
#write actual price in ActualPriceList.txt
x = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur').json()
file = open("Coingecko_ActualPriceList.txt", "w", encoding="utf-8" )
num = 1
for i in x:
  line = str(num) + ': ' + i['id'] + ', Price : ' + str(i['current_price']) + ' €' + ', Time: ' + i['last_updated'] + '\n'  
  print( line )
  #print(  i['id'], 'Price: ', i['current_price'], 'Time:', i['last_updated'],  '\n'   )
  file.write( line  )
  num += 1
file.close()


sleep(1)



#write file with available coins ActualPriceList.txt
y = requests.get('https://api.coingecko.com/api/v3/coins/list').json()
newfile = open("Coingecko_CoinList.txt", "w", encoding="utf-8" )
num = 1
for j in y:
  newline = str(num) + ': id: ' + j['id']  + ', Name: ' + j['name'] + '\n'
  print( newline )
  newfile.write( newline )
  num += 1
newfile.close()

'''


#aleph-zero

#forta



#read etherscan activities
print( '\n' )

myEthAddress = '0xEEb27799AECEC7Be079CD93aa30Cd6aB59664681'
key = 'ZM83PRS1BC1CAUTRJSUM8SWRJZTBV4X4B2'
tokenAddress = '0xF001937650bb4f62b57521824B2c20f5b91bEa05'#taraxa
url = f'https://api.etherscan.io/api?module=account&action=tokentx&contractAddress={tokenAddress}&address={myEthAddress}&tag=latest&apikey={key}'
y = requests.get(url).json()

timestamp = y['result'][0]['timeStamp']
value = int(y['result'][0]['value'])/100000000000000000
dt_object = datetime.fromtimestamp( int(timestamp) )
date = dt_object.strftime( "%d-%m-%Y" )

if debugMsgOn:
  print("timestamp =", timestamp, ", date =,", date, ", Value =", value, 'TARA')



#get price of a coin at a time
coinID = 'taraxa'
url = f'https://api.coingecko.com/api/v3/coins/{coinID}/history/?date={date}'
y = requests.get(url).json()

price = y['market_data']['current_price']['eur'] 

totalValue = price* value
if debugMsgOn:
  print( 'Price at' , date , ':' , price, '€' )
  print( "total taxable =",  totalValue, '€' )



print("date =", date, ", Value =", value, 'TARA, ', price, '€', ", total taxable =",  totalValue, '€\n'  )
