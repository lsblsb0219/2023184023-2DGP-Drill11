from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        # fill here
        return self.x-10,self.y-10,self.x+10,self.y+10
        pass

    def handle_collision(self, group, other):
        # fill here
        if group == 'boy:ball':
            game_world.remove_object(self) #게임 월드에서 지웠지만 충돌 리스트에는 여전히 있음.-> collision_pairs에 남아있음
        elif group == 'zombie:ball':
            game_world.remove_object(self)
        pass