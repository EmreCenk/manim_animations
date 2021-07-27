
"""
manim -pql venn_diagram.py VennScene
"""

from manim import *

class VennScene(Scene):

    def construct(self):
        self.introduction()

    def introduction(self):
        video_name = Tex("Venn Diagram With 2 Sets")
        self.play(FadeIn(video_name, run_time = 2))
        self.wait(1)
        self.play(FadeOut(video_name, run_time = 1))

        u_set_text = Tex("U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}")
        a_set_text = Tex("A = {1, 2, 3, 5, 8}").next_to(u_set_text, direction = DOWN)
        b_set_text = Tex("B = {2, 4, 6, 8}").next_to(a_set_text, direction = DOWN)

        self.play(
            FadeIn(u_set_text, a_set_text, b_set_text, run_time = 2.5)
        )


        self.wait(1.5)