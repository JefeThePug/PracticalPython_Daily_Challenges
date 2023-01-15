#Challenge 41: Car Classes
class Car:
    def __init__(self, model, color, year, transmission, electric=False):
        self.car_model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    def print_cars(self):
        print(f'{"-"*20}\n{self}\n{"-"*20}')
        
    def __str__(self):
        s = f'{self.car_model = }\n{self.color = }\n{self.year = }\n'
        s += f'{self.transmission = }\n{self.electric = }'
        return s.replace('self.','').replace("'","")
        
class BMW(Car):
    pass
class Tesla(Car):
    pass
class Ford(Car):
    pass
#but why?...


bmw1 = BMW(model='X6', color='Silver', year=2018, transmission='Auto') 
tesla1 = Tesla(model='S', color='Beige', year=2017, transmission='Auto', electric=True)
ford1 = Ford(model='Focus', color='White', year=2020, transmission='Auto')
bmw1.print_cars()
tesla1.print_cars()
ford1.print_cars()
