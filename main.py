import pygame
from math import radians, sin , cos
from datetime import datetime, date



class Clock:
    def __init__(self):
        self.height, self.width = 500, 500
        self.bg_color = (20, 19, 19)
        self.clk_color = (237, 157, 9)
        self.FPS = 60
        self.center = (self.width//2, self.height//2)
        self.clock_redius = self.width//2
        self.blue = (18, 30, 199)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("analog clock")
        self.clock = pygame.time.Clock()
        self.date_location = (self.width//2 + 5, self.height//2 + 5)
        self.glass = (143, 186, 201, 0.5)
    
    
    
    def numbers(self, number, size, position):
        font = pygame.font.SysFont("calibry", size, True, False)
        text = font.render(str(number), True, self.clk_color)
        text_rect = text.get_rect(center=position)
        self.screen.blit(text, text_rect)
        
    
    def polar_to_cartesian(self, r, theta):
        x = r * sin(radians(theta))
        y = r * cos(radians(theta))
        return self.width//2 + x , self.height//2 - y
    
    
    def draw_circle(self, screen):
        pygame.draw.circle(self.screen, self.clk_color, self.center, self.clock_redius -10, 5)
        pygame.draw.circle(self.screen, self.clk_color, self.center, 8)
    
      
    
    # def draw_date(self, screen):
    #     _date = date.today()
    #     pygame.draw.rect(self.screen,self.glass, pygame.Rect(230, 150, 30, 30))
        
            
        
        for number in range(1, 13):
            self.numbers(number, 40, self.polar_to_cartesian(self.clock_redius - 50, number* 30))
            
        
        for number in range(0,360,6):
            if number % 5:
                pygame.draw.line(self.screen, self.clk_color, self.polar_to_cartesian(
                    self.clock_redius -15, number),
                                 self.polar_to_cartesian(self.clock_redius - 23, number), 2)

            else:
                pygame.draw.line(self.screen, self.clk_color, self.polar_to_cartesian(
                    self.clock_redius -15, number),
                                 self.polar_to_cartesian(self.clock_redius - 30, number), 4)
                
    
    def draw_clock_hand(self):
        current_time = datetime.now()
        day = current_time.day
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour
        
        #Hour
        R = self.clock_redius - 150
        theta = (hour + minute/60 + second/3600) * (360 / 12)
        pygame.draw.line(self.screen, self.blue, self.center,
                         self.polar_to_cartesian(R, theta), 10)
        
        #Minute
        R = self.clock_redius - 100
        theta = (minute + second/360) * (360 / 60)
        pygame.draw.line(self.screen, self.blue, self.center,
                         self.polar_to_cartesian(R, theta), 9)
        
        #Second
        R = self.clock_redius - 80
        theta = second * (360 / 60)
        pygame.draw.line(self.screen, self.clk_color, self.center,
                         self.polar_to_cartesian(R, theta), 5)
        
    
    # Display date
        # date_font = pygame.font.Font(None, 36)     #show full of date
        # date_text = date_font.render(current_time.strftime("%B %d, %Y"), True, "BLACK")
        # self.screen.blit(date_text, (self.width // 2 -
        #                              date_text.get_width() // 2, self.height - 90))
        
        
    #display Data just day
    
        date_font = pygame.font.Font(None, 36)       
        date_text = date_font.render(str(day), True, "white")
        self.screen.blit(date_text, (self.width // 2 - date_text.get_width() // 2,
                                     (self.height // 2 - 75)- date_text.get_height() // 2))     
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
        
            self.screen.fill(self.bg_color)
            self.draw_circle(self.screen)
            self.draw_clock_hand()
            # self.draw_date(self.screen)
            pygame.display.update()
            self.clock.tick(self.FPS)
            
            
            
if __name__ == "__main__":
    myclock = Clock()
    myclock.run()