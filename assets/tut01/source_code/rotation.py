from math import sqrt

from manim import *

config.frame_height = 7
config.frame_width = 7
config.pixel_height = 2000
config.pixel_width = 2000


class Rotation(Scene):
    def construct(self):
        numberplane = NumberPlane(
            x_range=(-7, 7),
            y_range=(-7, 7),
            background_line_style={"stroke_width": 1, "stroke_opacity": 0.5},
        )

        dot = Dot(ORIGIN)
        origin_text = MathTex("(0, 0)").next_to(dot, DOWN)

        triangle = Triangle(color=RED, radius=2)
        triangleLabel = MathTex("T", color=RED).next_to(triangle, RIGHT)

        self.add(numberplane, dot)
        self.play(Write(triangle), Write(triangleLabel))
        self.wait()

        z = [0, 2, 0]
        zDot = Dot(z, color=YELLOW)
        zLabel = MathTex("z", color=YELLOW).next_to(zDot, UP)
        zLine = DashedLine(start=ORIGIN, end=z, color=YELLOW)
        self.play(Write(zLine, run_time=0.7))
        self.play(Write(zDot), Write(zLabel))
        self.wait(2)

        zLineCopy = DashedLine(start=ORIGIN, end=z, color=YELLOW)
        angleTracker = ValueTracker(1)
        zLineCopy.rotate(
            angleTracker.get_value() * DEGREES, about_point=ORIGIN
        )
        angle = Angle(zLine, zLineCopy, radius=1)
        self.add(zLineCopy, angle)

        zLineCopy.add_updater(
            lambda x: x.become(zLine.copy()).rotate(
                angleTracker.get_value() * DEGREES, about_point=ORIGIN
            )
        )

        angle.add_updater(
            lambda x: x.become(Angle(zLine, zLineCopy, radius=1))
        )

        self.play(angleTracker.animate.set_value(90))

        ziLabel = MathTex("i", "\\cdot", "z").next_to(zLineCopy.get_end(), UP)
        ziLabel.set_color_by_tex_to_color_map({"i": GREEN, "z": YELLOW})
        ziDot = Dot(zLineCopy.get_end(), color=YELLOW)
        self.play(Write(ziLabel), Write(ziDot))
        self.wait(2)

        arc = Arc(radius=2, start_angle=PI / 2, angle=PI / 2)
        self.play(FadeOut(zLabel, zLine, ziLabel, zLineCopy))
        self.play(ReplacementTransform(angle, arc))

        triangleLabelRotated = MathTex("i", "\\cdot", "T").next_to(
            triangle, UP
        )
        triangleLabelRotated.set_color_by_tex_to_color_map(
            {"i": GREEN, "T": RED}
        )

        self.play(
            Rotate(triangle, PI / 2, about_point=ORIGIN),
            ReplacementTransform(triangleLabel, triangleLabelRotated),
            FadeOut(zDot, ziDot, arc),
            run_time=1.5,
        )
        self.wait(2)

        triangleLabelRotated2 = MathTex("e^{i \\pi/4}", "\\cdot", "T").next_to(
            triangle, (UP + RIGHT) / 2
        )
        triangleLabelRotated2.set_color_by_tex_to_color_map(
            {"i": GREEN, "T": RED}
        )
        self.play(
            Rotate(triangle, -PI / 4, about_point=ORIGIN),
            ReplacementTransform(triangleLabelRotated, triangleLabelRotated2),
            run_time=1.5,
        )
        self.wait(3)
