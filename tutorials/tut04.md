# Tutorium 4

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut04/presentation.pdf)

## Kurzprotokoll
Nach der Besprechung der benötigten Sätze und Definitionen im Foliensatz sprachen wir über die Aufgaben.

## Zum Mitnehmen

### Aufgabe 1
- Bei Aufgabenteil (i) sind viele verschiedene mögliche Lösungswege ersichtlich: Finden einer Stammfunktion, aufteilen der Reihe in Hauptteil und "tail", majorisierte/dominierte Konvergenz, Fubini oder gleichmäßige Konvergenz von Potenzreihen auf Kreisscheiben innerhalb des Konvergenzkreises.
  Hier ist wichtig, gut das Verhalten von (Potenz-)Reihen oder allgemeiner von Grenzwerten im Zusammenhang mit Integralen zu verstehen.
- Standardparametrisierungen $$t z_1 + (1 - t) z_2$$, $$t \in [0, 1]$$, für die Strecke zwischen $$z_1$$ und $$z_2$$ sowie $$z_0 + r \mathrm{e}^{\mathrm{i} t}$$, $$t \in [a, b]$$, für Kreissegmente mit Radius $$r > 0$$, zentriert um $$z_0 \in \mathbb{C}$$.
- Homotopieinvarianz des Kurvenintegrals als Nachweis von Nicht-Holomorphie und Feststellung, dass auch Kurvenintegral nicht-holomorpher Funktionen verschwinden kann.
- (Mal wieder) binomischer Lehrsatz und $$\mathop{\text{Re}}(z) = \frac{1}{2}(z + \overline{z})$$ (merke auch: $$\mathop{\text{Im}}(z) = \frac{1}{2\mathrm{i}}(z - \overline{z})$$).

### Aufgabe 2
- Hier haben wir zum ersten Mal einen der vielleicht wichtigsten Tricks der Funktionentheorie gesehen, nämlich die Berechnung reeller Integrale mittels Anwendung des Satzes von Cauchy und Aufteilen der Kurve in Kurvenstücke, entlang welcher das Integral leicht berechnet werden kann und entlang welcher das ursprünglich gesuchte Integral rauskommt.
  Ein häufiger Trick ist hierbei, die Kurve "unendlich groß" werden zu lassen, beispielsweise die Breite eines Rechteckes oder den Radius eines Halbkreises im Grenzwert $$\to \infty$$ zu betrachten, wodurch manche Teilintegrale oft verschwinden.
- $$\lvert \mathrm{e}^z \rvert = \mathrm{e}^{\mathop{\text{Re}}(z)}$$ für alle $$z \in \mathbb{C}$$.

### Aufgabe 3
- Hier ist vielleicht die Aussage das Interessanteste, der Beweis ist sehr ähnlich zu bereits in der Vorlesung Gesehenen.

## Fun Facts
In Aufgabe 2 haben wir das Integral $$I := \int_{-\infty}^{\infty} \mathrm{e}^{-x^2} \,\mathrm{d}x = \sqrt{\pi}$$ verwendet, auch bekannt als [Gaußsches Integral](https://en.wikipedia.org/wiki/Gaussian_integral).
Hierzu könnte man aufgrund der weitreichenden Anwendungen dieses Integrals (beispielsweise in der Stochastik oder im Zusammenhang mit der Fouriertransformation) sicherlich sehr viele Fakten und Berechnungsmethoden aufzählen, aber hier vielleicht nur zwei meiner persönlichen Favoriten:
- Das Integral kann sehr elegant mithilfe von Methoden der Funktionentheorie (um genau zu sein, dem Residuensatz) berechnet werden (s. Example 3.10 im Skript von Prof. Frank).
- Vermutlich die berühmteste (und auch wirklich sehr schöne) auf Poisson zurückgehende Methode das Integral zu berechnen, ist es $$I^2$$ zu berechnen, indem man den Transformationssatz anwendet und zu Polarkoordinaten über geht.
  Eine natürliche Frage wäre, ob man diesen Trick öfter, also auch für andere Integrale, anwenden kann -- in der Tat ist dies im Wesentlichen aber nur für die Gaußfunktion möglich.
  In den Worten von Dawson (s. Referenz unten):
  > "One question that must have occurred to many over the years is: What else can I do with it? The surprising answer to this natural question is: Absolutely nothing!"

  Für eine präzisere Formulierung als "im Wesentlichen" und den recht kurzen Beweis (sowie auch für die ausführliche Version der oben beschriebenen Berechnung), siehe:
  - [Dawson, R. J. MacG. (2005). On a “Singular” Integration Technique of Poisson. The American Mathematical Monthly, 112(3), 270–272.](https://doi.org/10.1080/00029890.2005.11920195)

  Hierzu kann man sich, wenn man möchte, auch etwas mit der [Cauchyschen Funktionalgleichung](https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation) auseinandersetzen, welche im Beweis eine Rolle spielt.

Der Vollständigkeit halber sind hier auch noch ein paar weitere Berechnungsmethoden und ein wenig historischer Kontext: [Keith Conrad - The Gaussian Integral](https://kconrad.math.uconn.edu/blurbs/analysis/gaussianintegral.pdf).
