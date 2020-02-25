import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

import pool.collisions as collisions
import pool.event as event
import pool.gamestate as gamestate
import pool.graphics as graphics
import pool.config as config

import json

class Game:
    def __init__(self):
        self.game = gamestate.GameState()
        self.output_sprites = None

    def _output_sprites(self):
        sprites = []
        for sprite in self.game.all_sprites:
            if len(str(sprite)) > 0:
                sprites.append(sprite.get_dict())
        return sprites

    def start(self):    
        self.game.start_pool()
        self.game.redraw_all()

        self.output_sprites = self._output_sprites()

    def update(self):
        while not self.game.all_not_moving():
            collisions.resolve_all_collisions(self.game.balls, self.game.holes, self.game.table_sides)
            self.game.redraw_all()
        self.output_sprites = self._output_sprites()

    def move(self, args):

        events = {"angle" : args['angle'],
                  "displacement" : args['displacement']}

        if self.game.all_not_moving():
            
            self.game.check_pool_rules()
            self.game.cue.make_visible(self.game.current_player)

            while not self.game.is_game_over and self.game.all_not_moving():
                self.game.redraw_all()
                self.output_sprites = self._output_sprites()
                self.game.cue.cue_is_active(self.game, events)
