import chances
from animationStore import DragonAnimation
from hitboxes import Hitbox
from bullet import EnemyBullet


class Dragon:
    def __init__(self, app):
        self.app = app
        self.animation = DragonAnimation(app).main
        self.bullet_animation = DragonAnimation(app).bullet
        self.size = self.animation.get_pygame_surface().get_size()
        self.pos = chances.pos(self.size, self.app.res)
        self.world = app.world
        self.hitbox = Hitbox(self.size, self.world)
        self.temp_settings = app.temp_settings
        self.screen = app.screen
        self.hp = 10
        self.player = app.player
        self.moving = chances.RandomMoving(self.pos, self.app.res, 3, self.size)

        # self.world.add_object(self.bullet, self, self.bullet_animation)

    def update(self):
        self.hitbox.update(self.pos)
        self.pos = self.moving.increase()
        if chances.chance(0.6):
            self.world.add_object(EnemyBullet, self, self.player.pos, self.bullet_animation, 6, 5)
        if self.hp <= 0:
            self.world.remove(self)
            self.world.dragons -= 1

    def draw(self):
        self.animation.draw(*self.pos)

    def damage(self, dam):
        self.hp -= dam
