from les5 import start

phones = [
    {"name": "Iphone",
     "model": "5",
     "price": 4000
     },
    {"name": "Iphone",
     "model": "5s",
     "price": 5000
     },
    {"name": "Iphone",
     "model": "6",
     "price": 6000
     },
    {"name": "Iphone",
     "model": "6s",
     "price": 7000
     },
    {"name": "Iphone",
     "model": "10",
     "price": 20000
     },
    {"name": "Samsung",
     "model": "S7",
     "price": 7000
     },
    {"name": "Samsung",
     "model": "S8",
     "price": 9000
     },
    {"name": "Samsung",
     "model": "S10",
     "price": 19000
     },
    {"name": "Xiomi",
     "model": "mi6",
     "price": 6000
     }, 
    {"name": "Xiomi",
     "model": "mi8",
     "price": 9000
     },
]
try:
    start(phones)
except ValueError:
    print("Введены некорректные данные in PRICE")

