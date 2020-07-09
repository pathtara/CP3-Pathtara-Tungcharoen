def vatCalculate(price):
      #price = input("price")
      result = price + (price * 0.07)
      return result
      
p = float(input("Price : "))      
print("Net Price (Including VAT)"vatCalculate(p))