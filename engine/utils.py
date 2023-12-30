import pygame as pg


def distance(v1: pg.Vector2, v2: pg.Vector2):
    return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2) ** 0.5
