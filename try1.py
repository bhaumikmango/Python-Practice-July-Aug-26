# # Decorators Demo

# import time

# def brew_tea():
#     start_time = time.time()
#     print("Brewing Tea ....")
#     time.sleep(1)
#     print("Tea is ready!")
#     end_time = time.time()
#     print(f"Task Time : {end_time-start_time} seconds")

# def make_matcha():
#     start_time = time.time()
#     print("Making Matcha ....")
#     time.sleep(2)
#     print("Matcha is ready!")
#     end_time = time.time()
#     print(f"Task Time : {end_time-start_time} seconds")

# brew_tea()
# make_matcha()

# # We can do the same using decorators

# import time

# def timer_dec(base_fn):
#     def enhanced_fn():
#         start_time = time.time()
#         base_fn()
#         end_time = time.time()
#         print(f"Task Time : {end_time-start_time} seconds")
#     return enhanced_fn

# def brew_tea():
#     print("Brewing Tea ....")
#     time.sleep(1)
#     print("Tea is ready!")
    
# # Method 1 of applying decorators

# a1 = timer_dec(brew_tea)
# print(a1)
# a1()
# brew_tea = timer_dec(brew_tea) #keeping the name of the decorator variable same as of the function will keep calling the decorator automatically everytime we call the base function
# brew_tea()

# # Method 2 of applying decorators
# @timer_dec
# def make_matcha():
#     print("Making Matcha ....")
#     time.sleep(2)
#     print("Matcha is ready!")

# make_matcha()


# Decorating functions with parameters

import time
from datetime import datetime, timedelta

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        res = base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Task Time : {end_time-start_time} seconds")
        return res
    return enhanced_fn

@timer_dec
def brew_tea(tea_type : str, steep_time : int):
    print(f"Brewing {tea_type.title()} Tea ....")
    time.sleep(steep_time)
    print(f"{tea_type.title()} Tea is ready!")
    return f"Start drinking tea by {datetime.now() + timedelta(seconds=340)}."

brew_tea("lAvender", 5)
brew_tea(tea_type="London", steep_time=3)
print(brew_tea("Masala", 4))