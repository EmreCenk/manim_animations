
"""
manim -pql venn_diagram.py VennScene
"""

from manim import *

class VennScene(Scene):

    def construct(self):
        self.camera.background_color = BLUE
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

    def create_shapes(self):


        # circle_scale is the magic number. Everything else is relative to this.
        # As a result, simply changing the circle scale also adjusts everything else else accordingly
        circle_scale = 1.35

        #outer rectangle:
        outer_rectangle = Rectangle().scale(circle_scale * 1.45)
        outer_rectangle.fill_color = YELLOW






        left_circle = Circle().scale(circle_scale)
        right_circle = Circle().scale(circle_scale)
        shift_coef = 1.2 * circle_scale

        #a shift coefficient of 1.5 creates a perfect venn diagram

        left_circle.shift(LEFT*shift_coef)
        right_circle.shift(RIGHT*shift_coef)


        #Creating the labels for the shapes:
        label_shift_coef = 0.4 * circle_scale
        label_A = Tex("A").next_to(left_circle,
                                   direction = (LEFT + UP) ).shift((RIGHT+DOWN) * label_shift_coef)

        label_B = Tex("B").next_to(right_circle,
                                   direction = (RIGHT + UP)).shift((LEFT+DOWN) * label_shift_coef)

        label_U = Tex("U").next_to(outer_rectangle,
                                   direction = RIGHT + UP).shift( (LEFT+DOWN) * 0.8 )


        to_shift = [right_circle,
                    left_circle,
                    outer_rectangle,
                    label_A,
                    label_B,
                    label_U,]

        #shift everything to left:
        to_shift = [to_shift[i].shift(LEFT * 3 + UP * 0) for i in range(len(to_shift))]
        self.play(FadeIn(*to_shift, run_time = 2))

        return to_shift

    def create_sets(self, reference_point: Mobject):
        Aset_label = MathTex("A = \{1, 2, 3, 5, 8\}").next_to(reference_point, direction = RIGHT)
        Bset_label= MathTex("B = \{2, 4, 6, 8\}").next_to(Aset_label, direction = DOWN)
        self.play(FadeIn(Aset_label, Bset_label, run_time = 2))

    def venn_animation(self):
        right_circle, left_circle, outer_rectangle, label_A, label_B, label_U, = self.create_shapes()
        self.create_sets(outer_rectangle)

