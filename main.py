class Transport:
  def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

  def seating_capacity(self, capacity):
      return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
  def seating_capacity(self, capacity=50):
      return super().seating_capacity(capacity)


# Создаем объект Autobus
my_bus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию об автобусе
print(f"Название автомобиля: {my_bus.name} Скорость: {my_bus.max_speed} Пробег: {my_bus.mileage}")
print(my_bus.seating_capacity())
