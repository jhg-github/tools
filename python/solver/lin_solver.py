class LinSolver():
    def __init__(self):
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.m = 0
        self.n = 0
    
    def update_m_n(self):
        try:
            self.m = (self.y1-self.y0) / (self.x1-self.x0)
            self.n = self.y0 - (self.m*self.x0)
        except:
            self.m = 0
            self.n = 0
        return self.m, self.n
    
    def set_x0(self, x0):
        self.x0 = x0
        return self.update_m_n()

    def set_x1(self, x1):
        self.x1 = x1
        return self.update_m_n()

    def set_y0(self, y0):
        self.y0 = y0
        return self.update_m_n()

    def set_y1(self, y1):
        self.y1 = y1
        return self.update_m_n()
    
    def get_y(self, x):
        y = (self.m*x)+self.n
        return y
    
    def get_x(self, y):
        x = (y-self.n)/self.m
        return x
