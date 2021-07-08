from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = self.create_circle()

        sq = Square()
        sq.set_fill(BLUE, opacity = 0.5)


        self.play(Create(circle))  # show the circle on screen
        self.play(Transform(circle, sq))

    def create_circle(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        return circle