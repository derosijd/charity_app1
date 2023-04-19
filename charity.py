from baseObject import baseObject
import hashlib

class charity(baseObject):
    def __init__(self):
        self.setup('charity_app_charity')
        
    
    def verify_new(self,n=0):
        
        
        if len(self.errors ) == 0:
            return True
        else:
            return False
        
    def verify_update(self,n=0):
        
              
        if len(self.errors ) == 0:
            return True
        else:
            return False 

        
       
    def dropDownList(self):
        choices = []
        for item in self.data:
            d = {}
            d['value'] = item[self.pk]
            d['text'] = f"{item['name']} "
            choices.append(d)
        return choices
    