products = [
    {"name":"mouse", "stock":10, "price": 2000},
    {"name":"Keyboard", "stock":12, "price": 5000}, 
    {"name":"monitor", "stock":2 , "price": 120000},
]


for item in products:
    if item["stock"] <5:
      print(f"")
    else: 
      print(item["name"], "-", "Stock:", item["stock"], "-", " stock ok")
