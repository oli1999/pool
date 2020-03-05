<h1 align="center"> Pool </h1>
<p align="center">
    <a href="https://travis-ci.org/max-kov/pool">
        <img src="https://travis-ci.org/max-kov/pool.svg?branch=master"
             alt="build status">
             </a> 
</p>

<p align="center"><b> A pool game written entirely in python! </b></p>

Forked from [max-kov](https://github.com/max-kov/pool)!


![Alt text](/../screenshots/poolgif.gif?raw=true "Game gif")


## Install

### Windows

Install any Python3 installer and also install Git run in the console:

```bash
git clone https://github.com/qbeer/pool
cd pool

pip install -r requirements.txt
```

### Linux

```
sudo apt-get build-dep python-pygame
sudo apt-get install python-dev python3

git clone https://github.com/qbeer/pool
cd pool

pip3 install -r requirements.txt --user
```

## Run

### Windows

#### To play

```bash
python run.py
```

#### To run the server

```bash
python server.py
```

### Linux

#### To play

```bash
python3 run.py
```

#### To run the server

```bash
python3 server.py
```

### Docs

#### Current state

When the server is running on your machine call `localhost:5000` to get a JSON response of the current status of the game:

```json
[
    {
    center: [
        40,
        40,
    ]},
    {
    center: [
        500,
        40,
    ]
    },
    ...
    {
    center: [
        40,
        460,
    ]
    },
    {
    color: [
        255,
        255,
        255,
    ],
    number: 0,
    center: [
        265.5,
        250,
    ],},
    ...
    {
    color: [
        0,
        0,
        0,
    ],
    number: 8,
    center: [
        846.9948452238572,
        194,
    ],},
    {
        angle: 0,
        displacement: 14,
    },
    ]
```

Where a hole in the field is represented by an `(x, y)` coordinate
called center based on its center point. A ball on the other hand is represented by a `color` an `(x, y)` coordinate and a `number`.

The white ball is `number = 0` and there are 16 balls in total, 7 for each player and a black ball alongside the white. The game is over when the black ball is holed and the other player wins if this happens ahead of time.

### Play

Based on the current state you would generally need to be able to change it with the cue. The cue's head is always at the white ball and you would need to define a `displacement` between `15-99` and an `angle` from `[-\pi, \pi]`. The angle is measured from the bottom when the cue is pointing up.

In order to handle the cue you would need to send a `POST` request to `localhost:5000/?displacement=42&angle=-1.54` in order to push the white ball with 42 displacement (this translates in the game engine to force) and in a `-1.54` radian angle (this is the horizontal push to the right).

After the request succeeded you get back the new state of the field.