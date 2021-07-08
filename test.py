from manim import *
import numpy as np
"""
manim -pql test.py Factoring
"""
class Factoring(Scene):
    def construct(self):
        # self.play_example_1()
        self.play_example_2()

    def play_example_2(self):

        # second example
        header2 = MathTex(r"\text{Factor }",
                          "5", "x^{2}", "(y + 2)", "-",
                          "5", "(y + 2)",
                          r"\text{ completely}").scale(1.5)
        self.play(FadeIn(header2))
        self.wait(1)

        # expresson
        expression = MathTex(
            "5", "x^{2}", "(y + 2)", "-",
            "5", "(y + 2)"
        ).scale(1)

        expression_left = MathTex(
            "5", "x^{2}", "(y + 2)", "-",
            "5", "(y + 2)"
        ).scale(1)


        # locate the expression
        expression.shift(3 * LEFT + UP)
        expression_left.shift(3 * LEFT + UP)
        self.play(ReplacementTransform(header2, expression))
        self.wait(1)

        # equal sign
        equal = MathTex(" = ").next_to(expression, RIGHT)
        self.play(Write(equal))
        self.wait(0.5)

        # highlight the coefficients
        new_expression = MathTex("5",
                                 "(y + 2)",
                                 "(",
                                 "x^{2}",
                                 " - ",
                                 "1",
                                 ")").next_to(equal, RIGHT)

        ## 5
        # arrow1 = CurvedArrow(expression[0].get_center(), [0.2, 0.5, 0]).set_color(YELLOW)
        # arrow2 = CurvedArrow(expression[4].get_center(), [0.2, 0.5, 0]).set_color(YELLOW)
        # self.play(expression[0].animate.set_color(YELLOW), run_time=0.1)
        # self.play(expression[4].animate.set_color(YELLOW), run_time=0.1)
        # self.wait(0.25)
        # self.play(FadeIn(arrow1, arrow2))
        # self.wait(0.25)
        # self.play(Write(new_expression[0]))
        # self.wait(0.5)
        # self.play(FadeOut(arrow1, arrow2))
        # self.wait(0.5)

        # Highlighting 5:
        self.play(
            Indicate(expression[0]),
            Indicate(expression[4])
        )
        # Carrying the 5:
        self.move_multiple_in_arc(
            mobject_list = [expression[0], expression[4]],
            end_point_list=[new_expression[0].get_center(), new_expression[0].get_center()],
            right_side_list=[new_expression[0], new_expression[0]],
            left_side_list=[expression_left[0], expression_left[4]]
        )


        ## (y + 2)
        arrow3 = CurvedArrow([-3.6, 1.5, 0], [1, 1.5, 0], angle=-TAU / 4).set_color(GREEN)
        arrow4 = CurvedArrow([-1.2, 1.5, 0], [1, 1.5, 0], angle=-TAU / 4).set_color(GREEN)
        self.play(expression[2].animate.set_color(GREEN), run_time=0.1)
        self.play(expression[5].animate.set_color(GREEN), run_time=0.1)
        self.wait(0.25)
        self.play(FadeIn(arrow3, arrow4))
        self.wait(0.25)
        self.play(Write(new_expression[1]))
        self.wait(0.5)
        self.play(FadeOut(arrow3, arrow4))

        # # bracket
        # self.play(Write(new_expression[2]))
        # self.wait(0.5)
        #
        # # remaining terms (part 1)
        # underline1 = Underline(mobject=expression[1], buff=0.2).set_color(BLUE)
        # self.play(Create(underline1), run_time=0.6)
        # self.wait(0.25)
        # self.play(Write(new_expression[3]))
        #
        # # minus
        # self.play(Write(new_expression[4]))
        # self.wait(0.5)
        #
        # # remaining terms (part 2)
        # constant = MathTex("1").next_to(expression[5], DOWN * 0.7).set_color(BLUE).scale(0.8)
        # self.play(Write(constant))
        # self.wait(0.25)
        # self.play(Write(new_expression[5]))
        # self.wait(0.25)
        #
        # # brackets
        # self.play(Write(new_expression[6]))
        #
        # # equal sign
        # equal2 = MathTex(" = ").next_to(equal, DOWN * 6)
        # self.play(Write(equal2))
        # self.wait(0.5)
        #
        # # factorizing (x^2 - 1)
        # self.play(new_expression[2].animate.set_color(PINK), run_time=0.05)
        # self.play(new_expression[3].animate.set_color(PINK), run_time=0.05)
        # self.play(new_expression[4].animate.set_color(PINK), run_time=0.05)
        # self.play(new_expression[5].animate.set_color(PINK), run_time=0.05)
        # self.play(new_expression[6].animate.set_color(PINK), run_time=0.05)
        # self.wait(0.25)
        #
        # arrow5 = Arrow([3, 0.6, 0], [3, -0.1, 0], buff=0).set_color(PINK)
        # self.play(FadeIn(arrow5))
        # self.wait(0.5)
        #
        # # factoring
        # final_expression = MathTex("5", "(y + 2)", "(x + 1)(x - 1)").next_to(equal2, RIGHT)
        # self.play(Write(final_expression))
        # underline2 = Underline(mobject=final_expression[2], buff=0.2).set_color(PINK)
        # self.play(Create(underline2), run_time=0.6)
        # self.wait()

    def move_multiple_in_arc(self, mobject_list, left_side_list, right_side_list, end_point_list):
        animations = []

        for i in range(len(mobject_list)):

            a1 = self.move_in_arc(mobject_list[i], end_point_list[i])
            animations.append(a1)

            self.add(left_side_list[i])

        self.play(*animations)

        for m in right_side_list:
            self.add(m)

        for m in mobject_list:
            self.remove(m)




    def play_example_1(self):
        header = MathTex(r"\text{Factor }",
                         "24", "x^{6}", "+",
                         "16", "x^{2}", "y",
                         r"\text{ completely}").scale(1.5)
        self.play(FadeIn(header))

        self.wait(1)

        # the orginal expression
        text = MathTex(
            "24", "x^{6}", "+",
            "16", "x^{2}", "y"
        ).scale(2)

        # locate the expression
        text.shift(3 * LEFT + 3 * UP)

        self.play(ReplacementTransform(header, text))

        self.wait(1)

        # factoring numbers
        line1 = Line([-4.2, 2.5, 0], [-4.7, 2, 0])
        text24 = MathTex("8", "\cdot", "3")
        text24.shift(5 * LEFT + 1.5 * UP)

        line2 = Line([-2.8, 2.5, 0], [-2.3, 2, 0])
        text16 = MathTex("8", "\cdot", "2")
        text16.shift(2.2 * LEFT + 1.5 * UP)


        # Making copies of the left side of the equation:
        text16_left = MathTex("8", "\cdot", "2")
        text16_left.shift(2.2 * LEFT + 1.5 * UP)

        text24_left = MathTex("8", "\cdot", "3")
        text24_left.shift(5 * LEFT + 1.5 * UP)




        # highlight the coefficients (24)
        self.play(Indicate(text[0]))

        self.add(line1)
        self.wait(0.25)
        self.play(Write(text24))
        self.wait(0.25)

        # highlight the coefficients (16)
        self.play(Indicate(text[3]))

        self.add(line2)
        self.wait(0.25)
        self.play(Write(text16))
        self.wait(1)

        # factoring variables
        text_x6 = MathTex("x^{4}", "x^{2}").next_to(text24, RIGHT)
        text_x2 = MathTex("x^{2}", "y").next_to(text16, RIGHT)

        #Making copies for the left side of the equation:
        text_x6_left = MathTex("x^{4}", "x^{2}").next_to(text24, RIGHT)
        text_x2_left = MathTex("x^{2}", "y").next_to(text16, RIGHT)


        # plus
        plus = MathTex(" + ").next_to(text_x6, RIGHT)

        # highlight and factor variables
        self.play(Indicate(text[1]))
        self.play(Write(text_x6))
        self.play(Write(plus))
        self.wait(0.25)

        # self.play(Indicate(text[4] + Indicate(text[5])))
        self.play(Indicate(text[5]), Indicate(text[4]))
        self.play(Write(text_x2))
        self.wait()

        # equal sign
        equal = MathTex(" = ").next_to(text_x2, RIGHT)
        self.play(Write(equal))
        self.wait(0.5)

        # highlight common factors
        new_text = MathTex("8",
                           "x^{2}",
                           "(",
                           "3x^{4}",
                           " + ",
                           "2y",
                           ")").next_to(equal, RIGHT)

        to_move_coordinate = new_text[0].get_center()
        to_move_coordinate[0] += 0.25
        to_move_coordinate[1] += 0.25
        self.play(text24[0].animate.set_color(YELLOW), run_time=0.1)
        self.play(text16[0].animate.set_color(YELLOW), run_time=0.1)
        arrow1 = CurvedArrow(text24[0].get_center(),
                             to_move_coordinate).set_color(YELLOW)
        arrow2 = CurvedArrow(text16[0].get_center(),
                             to_move_coordinate).set_color(YELLOW)

        print("ALPHA:", new_text.get_center())

        # self.play(FadeIn(arrow1, arrow2))
        # self.wait(0.25)
        # self.play(Write(new_text[0]))
        # self.wait(0.5)
        # self.play(FadeOut(arrow1, arrow2))



        self.play(Indicate(text24[0]), Indicate(text16[0]))

        self.add(text24_left[0])
        self.add(text16_left[0])

        self.play(MoveAlongPath(text24[0], arrow1),
                  MoveAlongPath(text16[0], arrow2),
                  run_time = 1.5)



        self.remove(text24[0])
        self.remove(text16[0])

        self.add(new_text[0])

        self.wait(0.25)


        self.play(FadeToColor(text16_left[0], color = GRAY),
                  FadeToColor(text24_left[0], color = GRAY),
                  run_time = 1)

        self.wait(2)

        self.play(
            Indicate(text_x6[1], color = PINK),
            Indicate(text_x2[0], color = PINK)
        )
        text_x6[1].set_fill(PINK)
        text_x2[0].set_fill(PINK)

        new_text_1_coordinates = self.proper_center(new_text[1], -0.06, 0.35)

        arrow3 = CurvedArrow(text_x6[1].get_center(), new_text_1_coordinates, angle = TAU/2)
        arrow4 = CurvedArrow(text_x2[0].get_center(), new_text_1_coordinates, angle = TAU/2)

        self.add(text_x2_left[0])
        self.add(text_x6_left[1])
        self.play(MoveAlongPath(text_x6[1], arrow3),
                  MoveAlongPath(text_x2[0], arrow4),
                  run_time = 2)

        self.add(new_text[1])
        self.remove(text_x6[1])
        self.remove(text_x2[0])
        self.wait(0.05)

        self.play(FadeToColor(text_x6_left[1], color = GRAY),
                  FadeToColor(text_x2_left[0], color = GRAY),
                  run_time = 1)

        # text_x2_left[0].set_fill(GRAY)
        # text_x6_left[1].set_fill(GRAY)
        self.wait(1)


        # bracket
        self.play(Write(new_text[2]))
        self.wait(0.25)
        #
        # remaining terms (part 1)
        self.play(
            Indicate(text24[2], color = BLUE),
            Indicate(text_x6[0], color=BLUE),
            run_time = 1.3
        )

        arrow5 = CurvedArrow(text24[2].get_center(),
                             self.proper_center(new_text[3], -0.18, 0.12)).set_color(YELLOW)

        arrow6 = CurvedArrow(text_x6[0].get_center(),
                             self.proper_center(new_text[3], 0.28, 0.23)).set_color(YELLOW)



        self.wait(0.25)

        self.add(text24_left[2])
        self.add(text_x6_left[0])

        self.play(
            MoveAlongPath(
                text24[2], arrow5
            ),
            MoveAlongPath(
                text_x6[0], arrow6
            ),
            run_time = 2.5
        )
        self.add(new_text[3])
        self.remove(text24[2])
        self.remove(text_x6[0])


        self.play(FadeToColor(text24_left[2], GRAY),
                  FadeToColor(text_x6_left, GRAY))
        # self.play(Write(new_text[3]))

        # plus
        self.play(Write(new_text[4]))

        # remaining terms (part 2)

        self.play(
            Indicate(text16[2], color = BLUE),
            Indicate(text_x2[1], color = BLUE)
        )

        # underline3 = Underline(mobject=text16[2], buff=0.2).set_color(BLUE)
        # self.play(Create(underline3), run_time=0.6)
        #
        # underline4 = Underline(mobject=text_x2[1], buff=0.2).set_color(BLUE)
        # self.play(Create(underline4), run_time=0.6)

        self.wait(0.25)

        self.add(text16_left[2])
        self.add(text_x2_left[1])

        to_move = self.move_in_arc(text16[2], self.proper_center(new_text[5], 0.15, 0.26))
        to_move2 = self.move_in_arc(text_x2[1], self.proper_center(new_text[5], 0.39, 0.28))

        self.play(to_move,
                  to_move2,
                  run_time = 2)
        self.remove(text16[2])
        self.remove(text_x2[1])

        self.add(new_text[5])

        self.play(
            FadeToColor(text16_left[2], color = GRAY),
            FadeToColor(text_x2_left[1], color = GRAY)
        )
        self.wait(0.25)

        # bracket
        self.play(Write(new_text[6]))

        self.play(FadeToColor(new_text, YELLOW),
                  run_time = 1)

        to_fade = [text, text24[1], text16[1],
                          text_x2_left,
                          text24_left,
                          text16_left,
                          text_x6_left,
                          line1, line2,
                          plus, equal,
                          new_text]

        fade_animations = []
        for mobject in to_fade:
            fade_animations.append(
                FadeToColor(mobject, BLACK)
            )

        self.play(*fade_animations)

        for mobject in to_fade:
            self.remove(mobject)

        self.wait(3)
    def move_in_arc(self, mobject, final_coordiantes,):
        arrow = CurvedArrow(mobject.get_center(), final_coordiantes)
        return MoveAlongPath(mobject, arrow)

    def proper_center(self, mobject, x = 0.25, y = 0.25):
        a = mobject.get_center()
        a[0] += x
        a[1] += y

        return a

