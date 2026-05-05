from math import sqrt

from manim import *

config.frame_height = 12
config.frame_width = 10
config.pixel_height = 1200
config.pixel_width = 1000


class ComplexMultiplicationCalculation(Scene):
    def construct(self):

        z = [1, 2, 0]
        w = [4, 1, 0]

        numberplane = NumberPlane(
            x_range=(-2, 8),
            y_range=(-2, 10),
            background_line_style={"stroke_width": 1, "stroke_opacity": 0.5},
        )

        dot = Dot(ORIGIN).shift(4 * DOWN + 3 * LEFT)
        arrowZ = Arrow(ORIGIN, z, buff=0, color=BLUE_B).shift(
            4 * DOWN + 3 * LEFT
        )
        arrowW = Arrow(ORIGIN, w, buff=0, color=GREEN_B).shift(
            4 * DOWN + 3 * LEFT
        )
        origin_text = MathTex("(0, 0)").next_to(dot, DOWN)
        tip_textZ = MathTex("z = ", f"{z[0]}", "+", f"{z[1]}", "i").next_to(
            arrowZ.get_end(), RIGHT
        )
        tip_textW = MathTex("w = ", f"{w[0]}", "+", f"{w[1]}", "i").next_to(
            arrowW.get_end(), RIGHT
        )

        self.add(
            numberplane, dot, origin_text, arrowZ, arrowW, tip_textW, tip_textZ
        )

        self.wait(2)

        resultArrow = Arrow(
            ORIGIN,
            [z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0], 0],
            buff=0,
            color=TEAL_E,
        ).shift(4 * DOWN + 3 * LEFT)
        tip_textResult = MathTex(
            f"z \\cdot w = {z[0] * w[0] - z[1] * w[1]} + {z[0] * w[1] + z[1] * w[0]} i"
        ).next_to(resultArrow.get_end(), UP)

        self.play(Write(resultArrow))
        self.play(Write(tip_textResult))
        self.wait(3)


class ComplexMultiplicationIntuition(Scene):
    def construct(self):

        z = [1, 2, 0]
        w = [4, 1, 0]

        numberplane = NumberPlane(
            x_range=(-2, 8),
            y_range=(-2, 10),
            background_line_style={"stroke_width": 1, "stroke_opacity": 0.5},
        )

        dot = Dot(ORIGIN).shift(4 * DOWN + 3 * LEFT)
        arrowZ = Arrow(ORIGIN, z, buff=0, color=BLUE_B).shift(
            4 * DOWN + 3 * LEFT
        )
        arrowW = Arrow(ORIGIN, w, buff=0, color=GREEN_B).shift(
            4 * DOWN + 3 * LEFT
        )
        origin_text = MathTex("(0, 0)").next_to(dot, DOWN)
        tip_textZ = MathTex("z = ", f"{z[0]}", "+", f"{z[1]}", "i").next_to(
            arrowZ.get_end(), RIGHT
        )
        tip_textW = MathTex("w = ", f"{w[0]}", "+", f"{w[1]}", "i").next_to(
            arrowW.get_end(), RIGHT
        )

        self.add(
            numberplane, dot, origin_text, arrowZ, arrowW, tip_textW, tip_textZ
        )

        self.wait()

        tip_textZPolar = MathTex(
            "z = ", "r_z", "\\mathrm{e}^{i \\phi_z}"
        ).next_to(arrowZ.get_end(), RIGHT)
        tip_textWPolar = MathTex(
            "w = ", "r_w", "\\mathrm{e}^{i \\phi_w}"
        ).next_to(arrowW.get_end(), RIGHT)
        tip_textZPolar.set_color_by_tex_to_color_map({"r_z": RED, "phi": GOLD})
        tip_textWPolar.set_color_by_tex_to_color_map({"r_w": RED, "phi": GOLD})

        zBrace = BraceBetweenPoints(z, ORIGIN, color=RED).shift(
            4 * DOWN + 3 * LEFT
        )
        zBrace_text = zBrace.get_tex("r_z", buff=0)
        zBrace_text.set_color_by_tex_to_color_map({"r_z": RED})
        self.play(Write(zBrace), Write(zBrace_text))

        zAngle = Angle(
            Line(ORIGIN, [1, 0, 0]).shift(4 * DOWN + 3 * LEFT),
            arrowZ,
            radius=0.75,
            color=GOLD,
        )
        zAngle_text = MathTex("\\phi_z", color=GOLD).move_to(
            Angle(
                Line(ORIGIN, [1, 0, 0]).shift(4 * DOWN + 3 * LEFT),
                arrowZ,
                radius=1.1,
            ).point_from_proportion(0.5)
        )
        self.play(Write(zAngle), Write(zAngle_text))

        self.wait()
        self.play(ReplacementTransform(tip_textZ, tip_textZPolar))
        self.play(FadeOut(zBrace, zBrace_text))
        self.wait()
        self.play(ReplacementTransform(tip_textW, tip_textWPolar))
        self.wait(2)

        resultArrow = Arrow(
            ORIGIN,
            [z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0], 0],
            buff=0,
            color=TEAL_E,
        ).shift(4 * DOWN + 3 * LEFT)
        tip_textResultCut = MathTex("z \\cdot w =").next_to(
            resultArrow.get_end(), UP
        )
        tip_textResult = MathTex(
            "z \\cdot w =", "r_z r_w", "e^{i (\\phi_z + \\phi_w)}"
        ).next_to(resultArrow.get_end(), UP)
        tip_textResult.set_color_by_tex_to_color_map({"r_w": RED, "phi": GOLD})

        self.play(Write(resultArrow))
        self.play(Write(tip_textResultCut))
        self.wait(2)
        self.play(ReplacementTransform(tip_textResultCut, tip_textResult))
        self.wait()

        arrowZCopy = Arrow(ORIGIN, z, buff=0, color=YELLOW_D).shift(
            4 * DOWN + 3 * LEFT
        )
        arrowZCopy.generate_target()
        arrowZCopy.target.scale(sqrt(w[0] ** 2 + w[1] ** 2)).shift(
            [e * (sqrt(w[0] ** 2 + w[1] ** 2) - 1) / 2 for e in z]
        )
        self.play(Write(arrowZCopy))
        self.play(MoveToTarget(arrowZCopy))
        self.wait()
        self.play(
            ReplacementTransform(
                arrowZCopy,
                Arrow(
                    ORIGIN,
                    [z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0], 0],
                    buff=0,
                    color=YELLOW_D,
                ).shift(4 * DOWN + 3 * LEFT),
            )
        )
        self.play(Write(Angle(arrowZ, resultArrow, color=GOLD, radius=2)))
        movedWAngle_text = MathTex("\\phi_w", color=GOLD).move_to(
            Angle(
                arrowZ,
                resultArrow,
                radius=2.3,
            ).point_from_proportion(0.5)
        )
        self.play(Write(movedWAngle_text))
        self.wait(3)
