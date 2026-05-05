class Settings :
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (255, 0, 0)

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.laser_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1





    

      
