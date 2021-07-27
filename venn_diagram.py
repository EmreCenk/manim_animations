
"""
manim -pql venn_diagram.py VennScene
"""

from manim import *

class VennScene(Scene):

    def construct(self):
        # self.introduction()
        # self.wait(1)
        self.venn_animation()
    def introduction(self):
        video_name = Tex("Venn Diagram With 2 Sets")
        self.play(FadeIn(video_name, run_time = 2))
        self.wait(1)
        self.play(FadeOut(video_name, run_time = 1))

        u_set_text = MathTex("U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}")
        a_set_text = MathTex("A = \{1, 2, 3, 5, 8\}").next_to(u_set_text, direction = DOWN)
        b_set_text = MathTex("B = \{2, 4, 6, 8\}").next_to(a_set_text, direction = DOWN)

        self.play(
            FadeIn(u_set_text, a_set_text, b_set_text, run_time = 2.5)
        )

        self.wait(1)

        self.play(
            FadeOut(u_set_text, a_set_text, b_set_text, run_time = 2.5)
        )

    def venn_animation(self):

        #outer rectangle:
        outer_rectangle = Rectangle().scale(2.5)
        outer_rectangle.fill_color = YELLOW

        circle_scale = 1.75
        left_circle = Circle().scale(circle_scale)
        right_circle = Circle().scale(circle_scale)
        shift_coef = 1.5 * circle_scale

        #a shift coefficient of 1.5 creates a perfect venn diagram

        left_circle.shift(LEFT*shift_coef)
        right_circle.shift(RIGHT*shift_coef)


        self.play(FadeIn(right_circle, left_circle, outer_rectangle, run_time = 2))


