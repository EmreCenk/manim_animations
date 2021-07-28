
"""
manim -pql venn_diagram.py VennScene
"""
import copy

from typing import Sequence
from manim import *

class VennScene(Scene):

    def construct(self):
        self.camera.background_color = BLUE
        # self.introduction()
        # self.wait(1)
        self.venn_animation()


    def move_multiple_in_arc(self, mobject_list,
                             end_mobject_list,
                             end_point_list = None,
                             left_side_list = None,
                             fade_out_animation = True,
                             indicate_color = YELLOW, indicate = True, wait_time = 1, movement_animation_time = 1.5):

        # This is a utility method that is used to automate moving element(s) from one point to another
        if left_side_list is None:
            left_side_list = []
            for m in mobject_list:
                left_side_list.append(copy.deepcopy(m))
        if end_point_list is None:
            end_point_list = [end_mobject_list[i].get_center() for i in range(len(end_mobject_list))]


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

        self.play(*animations, run_time = movement_animation_time) #plays all movement animations at once

        for m in end_mobject_list: #makes the right side of the equation visible
            self.add(m)

        for m in mobject_list: #removes the moved elements to avoid congruent mobjects overlapping
            self.remove(m)

        self.wait(0.65)

        if fade_out_animation:
            self.play(*fade_animations, run_time = 1) #plays all fade animations


        self.wait(wait_time)

        return left_side_list #returns this in case the user doesn't have a copy of the left side
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
        circle_scale = 1.25

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

        Uset_label = MathTex('U = \{', '1', ',', '2', ',',
                '3', ',', '4', ',', '5', ',', '6', ',', '7',
                ',', '8', ',', '9', ',', '10', '\}').next_to(Aset_label, direction = UP).shift(RIGHT*1.3)

        self.play(FadeIn(Aset_label, Bset_label, run_time = 2))

        return Aset_label, Bset_label, Uset_label

    def convert_to_venn(self,
                        Aset: Mobject,
                        Bset: Mobject,
                        left_side: Sequence[Mobject],
                        right_side: Sequence[Mobject],
                        everything_to_fade_out: Sequence[Mobject]
                        ):


        indicate_animations = [Indicate(thing, run_time=3) for thing in [Aset[4], Aset[-2], Bset[2], Bset[-2]]]
        self.play(*indicate_animations)



        self.play(FadeOut(*everything_to_fade_out, run_time = 2))

        why_intersect_explanation = Tex("Since A and B have common elements, A and be will intersect")
        self.play(FadeIn(why_intersect_explanation, run_time = 1.5))
        self.wait(3)

        self.play(FadeOut(why_intersect_explanation))

        self.wait(0.5)

        self.play(FadeIn(*everything_to_fade_out, run_time = 2))


        move_animations = []
        for m in right_side:
            mw = copy.deepcopy(m)
            mw.shift(0.8 * LEFT)
            move_animations.append(ReplacementTransform(m, mw, run_time = 2))

        for m in left_side:
            mw = copy.deepcopy(m)
            mw.shift(0.8 * RIGHT)
            move_animations.append(ReplacementTransform(m, mw, run_time = 2))
        self.play(*move_animations)



    def create_items(self, left_circle, right_circle):
        items = ["1", "3", "5"]
        left_circle_items = [MathTex(items[i]).shift(
            left_circle.get_center()).shift(DOWN * 0.6 * (i - 1) + 0.3 * LEFT) for i in range(len(items))]

        items = ["4", "6"]
        right_circle_items = [MathTex(items[i]).shift(
            right_circle.get_center()).shift(DOWN * 0.6 * (i - 1) + 0.3 * RIGHT + DOWN * 0.3) for i in range(len(items))]

        items = ["2", "8"]
        intersection_items = [MathTex(items[i]).shift(
            right_circle.get_center()).shift(DOWN * 0.6 * (i - 1) + 0.8 * LEFT + DOWN * 0.3) for i in range(len(items))]

        return left_circle_items, right_circle_items, intersection_items
    def move_items_into_circles(self, Aset_label: MathTex,
                                Bset_label: MathTex,
                                intersection_items: Sequence[MathTex],
                                right_circle_items: Sequence[Mobject],
                                left_circle_items: Sequence[Mobject]):

        acopy = copy.deepcopy(Aset_label)
        bcopy = copy.deepcopy(Bset_label)

        #moving the items to the left circle:
        #note: the move_multiple_in_arc method is a custom method I wrote to automate moving mobjects from
        #one point to another. The code for this is in the top of the class.

        #moving the intersecting elements:
        intersection_set_copies = self.move_multiple_in_arc(
            mobject_list = [Aset_label[4], Aset_label[-2], Bset_label[2], Bset_label[-2]],
            end_mobject_list= [intersection_items[0], intersection_items[1], intersection_items[0], intersection_items[1]],
            left_side_list = [acopy[4], acopy[-2], bcopy[2], bcopy[-2]],
            movement_animation_time = 2

        )


        #moving the a set:
        Aset_copy = self.move_multiple_in_arc(
            mobject_list = [Aset_label[2], Aset_label[6], Aset_label[8]],
            end_mobject_list= [left_circle_items[0], left_circle_items[1], left_circle_items[2]],
            left_side_list=[acopy[2], acopy[6], acopy[8]],
            movement_animation_time = 2
        )

        #moving b set:
        Bset_copy = self.move_multiple_in_arc(
            mobject_list = [Bset_label[4], Bset_label[6]],
            end_mobject_list= [right_circle_items[0], right_circle_items[1]],
            left_side_list=[bcopy[4], bcopy[6]],

            movement_animation_time = 2
        )


        return acopy, bcopy

    def find_mathtex(self, mathtex: MathTex, phrase):
        for i in range(len(mathtex)):
            if phrase in mathtex[i].tex_string:
                return i

        raise ValueError("The phrase is not in the mathtex object provided")
    def venn_animation(self):
        right_circle, left_circle, outer_rectangle, label_A, label_B, label_U, = self.create_shapes()


        # Creating the set definitions at the right side: (A = {1,3,4,5,8} etc.):
        Aset_label, Bset_label, Uset_label = self.create_set_labels(outer_rectangle,
                                                        left_circle,
                                                        right_circle)


        #moves the circles closer, and explains why we did so:
        self.convert_to_venn(Aset_label,
                             Bset_label,
                             left_side = [left_circle, label_A],
                             right_side = [right_circle, label_B],
                             everything_to_fade_out = [right_circle,
                                                       left_circle,
                                                       outer_rectangle,
                                                       label_A,
                                                       label_B,
                                                       label_U,
                                                       Aset_label,
                                                       Bset_label])

        self.wait(1)

        left_circle_items, right_circle_items, intersection_items = self.create_items(left_circle, right_circle)
        # self.play(FadeIn(*right_circle_items, *left_circle_items, *intersection_items))

        #moving items into the circles:
        Aset_copy, Bset_copy =  self.move_items_into_circles(Aset_label,
                                Bset_label,
                                intersection_items,
                                right_circle_items,
                                left_circle_items)

        self.play(FadeIn(Uset_label))
        self.wait(1)


        #gets content from the set texts
        a_content = [Aset_copy[self.find_mathtex(Aset_copy, str(i))] for i in [1,2,3,5,8]]
        u_content1 = [Uset_label[self.find_mathtex(Uset_label, str(i))] for i in [1,2,3,5,8]]

        print("here it is", Bset_copy)
        b_content = [Bset_copy[self.find_mathtex(Bset_copy, str(i))] for i in [2,4,6,8]]
        u_content2 = [Uset_label[self.find_mathtex(Uset_label, str(i))] for i in [2,4,6,8]]

        self.move_multiple_in_arc(
            mobject_list = a_content,
            end_mobject_list = u_content1,
            fade_out_animation = False,

        )
        for m in u_content1:
            m.color = GRAY

        self.move_multiple_in_arc(
            mobject_list=b_content,
            end_mobject_list=u_content2,
            fade_out_animation=False,

        )

        for m in u_content2:
            m.color = GRAY

