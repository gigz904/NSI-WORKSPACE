months = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout,' , 'septembre', 'octobre', 'novembre', 'decembre']

class Date():
    def __init__(self, j, m, y):
        self.j = j
        self.m = m
        self.y = y

    def __str__(self):
        return str(self.j) +  ' ' +months[self.m-1]+ ' '+ str(self.y)
    
    def dateFromStr(dateStr):
        dList = dateStr.split('/')
        return (int(dList[0]), int(dList[1]), int(dList[2]))
    
    def __lt__(self, u):
        if u.y > self.y:
            return True
        else:
            if u.m>self.m:
                return True
            else:
                if u.j>self.j:
                    return True
                else:
                    return False