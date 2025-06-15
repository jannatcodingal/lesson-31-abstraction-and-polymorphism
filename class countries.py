class Pakistan():
    def capital(self):
        print("Pakistans capital is Islamabad")
    def language(self):
        print("Pakistans national language is urdu")
    def type(self):
        print("Pakistan is a developing country")
class USA():
    def capital(self):
        print("USA's capital is washington D.C")
    def language(self):
        print("USA's national language is english")
    def type(self):
        print("USA is a developed country")
obj_Pakistan=Pakistan()
obj_USA=USA()
for country in(obj_Pakistan,obj_USA):
    country.capital()
    country.language()
    country.type()