import pygame

class GameObject:
    def __init__(self, x, y, w, h, color, clickable):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._color = color
        self._clickable = clickable

    def get_rect(self):
        return pygame.Rect((self._x, self._y), (self._w, self._h))