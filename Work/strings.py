#Exercise 1.13
import re 

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
symbols = 'HPQ,' + symbols + ',GOOG'
lower = symbols.lower()
a = symbols.find('MSFT')
b = symbols[13:17]
c = symbols = symbols.replace('SCO', 'DOA')
name = 'IBM'
shares = 100
price = 91.1
total = f'{shares} shares of {name} at ${price:0.2f}'


text = 'Today is 19/05/2022. Tomorrow is 20/05/2022.'
re.findall(r'\d+/\d+/\d+', text)


print(total)


