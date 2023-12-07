class Sports:
    def __init__(self,name):
        self.name=name
        
    @property
    def sports_name(self):
        return self.name

    @sports_name.setter
    def sports_name(self, new_name):
        self.name = new_name


class landsports(Sports):
    def __init__(self,name,field):
        super().__init__(name)
        self._field=field
        
    @property
    def landsports_field(self):
        return self._field

  

class watersports(Sports):
    def __init__(self,name,activity):
        super().__init__(name)
        self._activity=activity
    
    @property
    def watersports_field(self):
        return self._activity

if __name__=="__main__":
        baseball=landsports("baseball","baseball field")
        print(baseball.sports_name)
        print(baseball.landsports_field)
        water_skiing=watersports("water skiing","Strap on your skis and fly across the water")
        print(water_skiing.sports_name)
        print(water_skiing.watersports_field)
        