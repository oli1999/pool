from flask import Flask
from flask_restful import Resource, Api, reqparse
import pygame
from pool.main import Game

parser = reqparse.RequestParser()
parser.add_argument('angle', type=float)
parser.add_argument('displacement', type=int)
parser.add_argument('player', type=int)

app = Flask(__name__)
api = Api(app)

g = Game()
g.start()

class GameApi(Resource):
    def get(self):
        g.update()
        return g.output_sprites
    def post(self):
        args = parser.parse_args()
        g.move(args)
        g.update()
        return g.output_sprites

api.add_resource(GameApi, '/')

if __name__ == '__main__':
    app.run(debug=False)