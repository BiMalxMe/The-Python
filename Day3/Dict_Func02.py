car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#setdefault
car.setdefault('Engine',4)


# update
car.update({"brand": "BMW"})
print(car)
#can update as well as add one

# pop
car.pop("model")

print(car)


# popitem
car.popitem()#deletes the last ley-value pair

print(car)


# clear
car.clear()
print(car)
