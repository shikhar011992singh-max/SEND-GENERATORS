def chai_customer():
      print("welcome! what chai u like ?")
      order = yield
      while True:
            print(f"preparing: {order}")
            order = yield

stall = chai_customer()
next(stall)# start the generator

stall.send("masala chai")