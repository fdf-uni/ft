from manim import *

config.frame_width = 14
config.frame_height = 6
config.pixel_width = 1400
config.pixel_height = 1200


class ComplexAddition(Scene):
    def construct(self):

        z = [1, 2, 0]
        w = [4, 1, 0]

        numberplane = NumberPlane(
            x_range=(-2, 12),
            y_range=(-2, 4),
            background_line_style={"stroke_width": 1, "stroke_opacity": 0.5},
        )

        dot = Dot(ORIGIN).shift(5 * LEFT + 1 * DOWN)
        arrowZ = Arrow(ORIGIN, z, buff=0, color=BLUE_B).shift(
            5 * LEFT + 1 * DOWN
        )
        arrowW = Arrow(ORIGIN, w, buff=0, color=GREEN_B).shift(
            5 * LEFT + 1 * DOWN
        )
        origin_text = MathTex("(0, 0)").next_to(dot, DOWN)
        tip_textZ = MathTex("z = ", f"{z[0]}", "+", f"{z[1]}", "i").next_to(
            arrowZ.get_end(), LEFT
        )
        tip_textW = MathTex("w = ", f"{w[0]}", "+", f"{w[1]}", "i").next_to(
            arrowW.get_end(), RIGHT
        )

        tip_textZ.set_color_by_tex_to_color_map(
            {f"{z[0]}": RED, f"{z[1]}": PURE_GREEN}
        )
        tip_textW.set_color_by_tex_to_color_map(
            {f"{w[0]}": RED, f"{w[1]}": PURE_GREEN}
        )

        self.add(numberplane, dot, origin_text)
        self.play(Write(arrowZ))

        z1 = [z[0], 0, 0]
        z2 = [0, z[1], 0]
        braceReZ = BraceBetweenPoints(ORIGIN, z1).shift(5 * LEFT + 1 * DOWN)
        braceReZ_text = MathTex(f"{z[0]}", color=RED).next_to(braceReZ, DOWN)
        self.add(braceReZ)
        self.play(Write(braceReZ_text))
        braceImZ = BraceBetweenPoints(z2, ORIGIN).shift(5 * LEFT + 1 * DOWN)
        braceImZ_text = MathTex(f"{z[1]}", color=PURE_GREEN).next_to(
            braceImZ, LEFT
        )
        self.add(braceImZ)
        self.play(Write(braceImZ_text))

        self.wait()
        self.play(FadeOut(braceReZ, braceReZ_text, braceImZ, braceImZ_text))
        self.play(Write(tip_textZ))

        self.wait()

        self.play(Write(arrowW))
        self.play(Write(tip_textW))

        arrowWCopy = Arrow(ORIGIN, w, buff=0, color=YELLOW_D).shift(
            5 * LEFT + 1 * DOWN
        )
        arrowWCopy.generate_target()
        arrowWCopy.target.shift(z)
        self.play(Write(arrowWCopy))
        self.play(MoveToTarget(arrowWCopy))
        self.play(
            Write(
                Arrow(
                    ORIGIN,
                    [a + b for a, b in zip(z, w)],
                    buff=0,
                    color=MAROON_B,
                ).shift(5 * LEFT + 1 * DOWN)
            )
        )
        self.play(FadeOut(arrowWCopy))

        tip_textSumExpanded = MathTex(
            "z + w = ", f"({z[0]} + {w[0]})", "+", f"({z[1]} + {w[1]})", "i"
        ).next_to(arrowWCopy.get_end(), RIGHT)
        tip_textSumImagExpanded = MathTex(
            "z + w = ", f"{z[0] + w[0]}", "+", f"({z[1]} + {w[1]})", "i"
        ).next_to(arrowWCopy.get_end(), RIGHT)
        tip_textSum = MathTex(
            "z + w = ", f"{z[0] + w[0]}", "+", f"{z[1] + w[1]}", "i"
        ).next_to(arrowWCopy.get_end(), RIGHT)

        tip_textSumExpanded.set_color_by_tex_to_color_map(
            {f"({z[0]} + {w[0]})": RED, f"({z[1]} + {w[1]})": PURE_GREEN}
        )
        tip_textSumImagExpanded.set_color_by_tex_to_color_map(
            {f"{z[0] + w[0]}": RED, f"({z[1]} + {w[1]})": PURE_GREEN}
        )
        tip_textSum.set_color_by_tex_to_color_map(
            {f"{z[0] + w[0]}": RED, f"{z[1] + w[1]}": PURE_GREEN}
        )

        self.play(Write(tip_textSumExpanded))
        self.play(
            ReplacementTransform(tip_textSumExpanded, tip_textSumImagExpanded)
        )
        self.play(ReplacementTransform(tip_textSumImagExpanded, tip_textSum))
        self.wait(3)
