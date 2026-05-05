import numpy as np
from manim import *


class argument_principle(Scene):
    def construct(self):
        # Movement using polar coordinates, e^{i t}
        def expi(t):
            return ORIGIN + np.cos(t) * RIGHT + np.sin(t) * UP

        # Quick HSV coloring
        def cmap(t, k=1):
            if k >= 0:
                hue = k * t
            else:
                hue = abs(k) - abs(k) * t
            return HSV((hue, 0.75, 1))

        # Circle in the center, composed of multiple lines for easier coloring
        CIRCLE_POINT_COUNT = 100
        EPSILON = 1 / CIRCLE_POINT_COUNT
        circle = Group(
            *[
                # Point(location=expi(t), color=WHITE)
                Line(
                    start=expi(t),
                    end=expi(t + 2 * PI / CIRCLE_POINT_COUNT + EPSILON),
                )
                for t in np.linspace(0, 2 * PI, CIRCLE_POINT_COUNT)
            ]
        )

        # Arrow representing f(z)
        arrow = Arrow(max_tip_length_to_length_ratio=0.15, color=cmap(0))

        # Text giving the definition of f
        def definition_text(f):
            return MathTex(f"f(z) = {f}").move_to(3 * LEFT + 2 * UP)

        function_definition = definition_text("z")

        # Text counting the rotations of the arrow,
        # together with the underlying logic for calculating them
        def rotation_count():
            return int(
                np.sign(rotations.get_value())
                * np.floor(
                    np.sign(rotations.get_value()) * rotations.get_value()
                )
            )

        rotations = ValueTracker(0)
        rotation_counter = always_redraw(
            lambda: MathTex(
                f"\\text{{Umdrehungen: }}{rotation_count()}"
            ).move_to(3 * RIGHT + 2 * UP)
        )

        # Initial parameters
        arrow.put_start_and_end_on(expi(0), 2 * expi(0))
        t_parameter = ValueTracker(0)

        # Update functions for circle and arrow
        def draw_color_circle(mob, k):
            t = t_parameter.get_value()
            for i in range(0, int(CIRCLE_POINT_COUNT * t // (2 * PI))):
                circle[i].set_color(cmap(i / CIRCLE_POINT_COUNT, k))

        def rotate_arrow(mob, k):
            t = t_parameter.get_value()
            mob.put_start_and_end_on(expi(t), expi(t) + expi(k * t))
            mob.set_color(cmap(t / (2 * PI), k))

        # Add all objects to the scene
        self.add(circle, Dot(ORIGIN), function_definition)
        self.play(Write(arrow))
        self.play(Write(rotation_counter))
        self.wait(1)

        # Considered exponents and corresponding functions
        exponents = [1, 2, -1, -2]
        functions = ["z", "z^2", "\\frac{1}{z}", "\\frac{1}{z^2}"]

        # Now the actual animation(s)
        for k, f in zip(exponents, functions):
            # Reset the ValueTrackers and colors
            t_parameter.set_value(0)
            rotations.set_value(0)
            for p in circle:
                p.set_color(WHITE)

            # Add updater functions to the relevant objects
            arrow.add_updater(lambda mob: rotate_arrow(mob, k))
            circle.add_updater(lambda mob: draw_color_circle(mob, k))

            # Display the current function definition
            self.play(Transform(function_definition, definition_text(f)))
            self.wait()

            # Finally let t go to 2 pi :)
            self.play(
                t_parameter.animate.set_value(2 * PI),
                rotations.animate.set_value(k),
                run_time=3,
                rate_func=rate_functions.linear,
            )
            self.wait(1)
