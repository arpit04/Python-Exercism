NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

class Robot(object):
    def __init__(self, bearing='NORTH', x=0, y=0):
        self.bearing = str(bearing)
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    
    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
            print(self.bearing)
        elif self.bearing == EAST:
            self.bearing = SOUTH
            print(self.bearing)
        elif self.bearing == SOUTH:
            self.bearing = WEST
            print(self.bearing)
        elif self.bearing == WEST:
            self.bearing = NORTH
            print(self.bearing)
 
    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
            print(self.bearing)
        elif self.bearing == WEST:
            self.bearing = SOUTH
            print(self.bearing)
        elif self.bearing == SOUTH:
            self.bearing = EAST
            print(self.bearing)
        elif self.bearing == EAST:
            self.bearing = NORTH
            print(self.bearing)

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
            print(self.bearing)
        elif self.bearing == SOUTH:
            self.y -= 1
            print(self.bearing)
        elif self.bearing == EAST:
            self.x += 1
            print(self.bearing)
        elif self.bearing == WEST:
            self.x -= 1
            print(self.bearing)
        self.coordinates = (self.x, self.y)
        print(self.coordinates)
    
    def simulate(self, direction):
        for command in direction:
            if command == 'R':
                self.turn_right()
            if command == 'L':
                self.turn_left()
            if command == 'A':
                self.advance()
            self.coordinates = (self.x, self.y)

r = Robot()
r.turn_right()
r.turn_left()
r.advance()
r.simulate('RAALAL')
