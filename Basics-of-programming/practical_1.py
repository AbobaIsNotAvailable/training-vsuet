surname, name = input("Ваши фамилия, имя?: ").split(" ")
age = int(input("Сколько Вам лет?: "))
location = input("Где вы живёте?: ")


print("Ваши фамилия и имя {0} {1}".format(surname, name))
print(f"Ваш возраст {age}")
print("Ваше место жительства: %s" % location)
