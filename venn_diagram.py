
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


    def move_multiple_in_arc(self, mobject_list, left_side_list, right_side_list, end_point_list,
                             indicate_color = YELLOW,  indicate = True, wait_time = 1):

        # This is a utility method that is used to automate moving element(s) from the left
        # side of the equation to the right.



        if indicate: #checking to see if the indicate option is enabled, if so indicating the elements

            indicate_animations = []
            for m in mobject_list:
                indicate_animations.append(
                    Indicate(m, color = indicate_color)
                )
            self.play(*indicate_animations, run_time = 1.65)

            self.wait(1)

        animations = [] #stores the movement animations
        fade_animations = [] #stores the fade animations
        for i in range(len(mobject_list)): #loops through all mobjects and stores their movement & fade animations

            a1 = self.move_in_arc(mobject_list[i], end_point_list[i])
            animations.append(a1)

            self.add(left_side_list[i])
            fade_animations.append(FadeToColor(left_side_list[i], color = GRAY))

        self.play(*animations, run_time = 1.5) #plays all movement animations at once

        for m in right_side_list: #makes the right side of the equation visible
            self.add(m)

        for m in mobject_list: #removes the moved elements to avoid congruent mobjects overlapping
            self.remove(m)

        self.wait(0.65)
        self.play(*fade_animations, run_time = 1) #plays all fade animations


        self.wait(wait_time)

    def move_in_arc(self, mobject, final_coordiantes,):
        arrow = ArcBetweenPoints(mobject.get_center(), final_coordiantes)
        return MoveAlongPath(mobject, arrow)


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

    def create_set_labels(self, reference_point1: Mobject,
                          left_circle: Mobject,
                          right_circle: Mobject):

        Aset_label = MathTex("A",
                             "= \{",
                             "1",
                             ", ",
                             "2",
                             ", ",
                             "3",
                             ", ",
                             "5",
                             ", ",
                             "8",
                             "\}").next_to(reference_point1, direction = RIGHT)

        Bset_label= MathTex("B",
                            "= \{",
                            "2",
                            ", ",
                            "4",
                            ", ",
                            "6",
                            ", ",
                            "8",
                            "\}").next_to(Aset_label, direction = DOWN)


        items = ["1", "3", "5"]
        left_circle_items = [MathTex(items[i]).shift(
            left_circle.get_center()).shift(DOWN * 0.6 * (i - 1)) for i in range(len(items))]

        items = ["2", "4", "6", "8"]
        right_circle_items = [MathTex(items[i]).shift(
            right_circle.get_center()).shift(DOWN * 0.6 * (i - 1.4)) for i in range(len(items))]

        self.play(FadeIn(Aset_label, Bset_label, *left_circle_items, *right_circle_items, run_time = 2))

    def venn_animation(self):
        right_circle, left_circle, outer_rectangle, label_A, label_B, label_U, = self.create_shapes()
        self.create_set_labels(outer_rectangle, left_circle, right_circle)


