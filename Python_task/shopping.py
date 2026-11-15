def calculate_total(price, quantity):
   total_cost = price * quantity
   return(total_cost)

def calculate_discount(total, percent):
   discount_amt = total * percent / 100
   return(discount_amt)

def display_receipt(item, total, quantity, discount):
   final_bill = total * quantity - discount
   
   print(final_bill)
   print("\n")
   print(f"item:     {item}")
   print(f"quantity:     {quantity}")
   print(f"subtotal:     {total:.2f}")
   print(f"Discount Applied :     {discount:.2f}")
   print(f"Final Bill:     {final_bill:.2f}")

  
