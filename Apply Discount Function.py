#Apply Discount Function
def apply_discount(price, discount):
    #Determining whether the arguments are integer or float
    if not isinstance(price, (int, float)):
        return "The price should be a number."
   
    if not isinstance(discount, (int, float)):
        return "The discount should be a number." 
    if price <= 0:
        return "The price should be greater than 0."
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
   #Calculating the final_price.
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return final_price



