print("=====THE RECEIPT FROM GWIZA SHOP=====")
pnm=input("Enter the product name:")
qu=float(input("Enter the product quantity:"))
ut=float(input("Enter the unit price per 1kg:"))
tt=qu*ut
vat=(tt*18)/100
print("============================================================")
print("Product name:",pnm)
print("The product quantity:",qu)
print("The unit price per 1kg:",ut)
print("The total to pay:",tt)
print("The value added tax (VAT)",vat)
print("============================================================")