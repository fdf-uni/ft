---
title: Tutorium 3
---

[Foliensatz](../../assets/2026/tut03/presentation.pdf)

## Kurzprotokoll

Zu Beginn wurde der Foliensatz besprochen, und daraufhin die Aufgaben dieser Woche.

## Zum Mitnehmen

### Aufgabe 1
- Hier haben wir zum ersten Mal einen der vielleicht nützlichsten Tricks der Funktionentheorie gesehen, nämlich die Berechnung reeller Integrale mittels Anwendung des Satzes von Cauchy[^1].
    Hierfür teilt man die Kurve, über welche das Gesamtintegral verschwindet (bzw. leicht berechnet werden kann) in Kurvenstücke auf, entlang welcher entweder das Integral leicht berechnet werden kann oder genau das ursprünglich gesuchte Integral rauskommt.
- Hier sind häufig Symmetrien äußerst hilfreich, welche wir dieses Mal auch für den ersten Aufgabenteil verwendet hatten (konkret die $$2 \pi \mathrm{i}$$-Periodizität von $$z \mapsto \mathrm{e}^{\mathrm{e}^{z}}$$ zum Nachweis der Unabhängigkeit des Integrals vom Parameter $$a$$).
- Je nachdem, ob man nachgewiesen hat, dass $$I(a)$$ unabhängig von $$a \in \mathbb{R}$$ oder $$a > 0$$ ist, benötigt man ein Grenzwert-Argument um die Berechnung auf den Wert von $$I(0)$$ zurückzuführen.
    Hierfür noch einmal die Erinnerung, gegebenenfalls den [Satz von der majorisierten/dominierten Konvergenz](https://de.wikipedia.org/wiki/Satz_von_der_majorisierten_Konvergenz) nachzuschlagen!!
    Diesbezüglich kann man mich aber natürlich auch gerne fragen. :)
- Zuletzt haben wir noch die Cauchysche Integralformel zur Berechnung eines Integrals verwendet, wo häufig hilfreich ist, die typischen Parametrisierungen wiederzuerkennen (s. auch die [Notizen zur letzten Woche](./tut02#aufgabe-1)).

[^1]: Beziehungsweise später auch mithilfe der Cauchyschen Integralformel und allgemeiner des Residuensatzes.

### Aufgabe 2
- Ein häufiger Trick zur Berechnung von Integralen mit dem oben beschriebenen Verfahren ist, die Kurve "unendlich groß" werden zu lassen, beispielsweise die Breite eines Rechteckes oder den Radius eines Halbkreises im Grenzwert $$\to \infty$$ zu betrachten, wodurch manche Teilintegrale dann verschwinden.  
    Konkret hatten wir in diesem Fall ein Rechteck mit Breite $$2 K$$, wobei wir $$K \to \infty$$ gehen lassen haben.
    Hier sind dann die Integrale über die vertikalen Seiten verschwunden.
- Es gilt $$\lvert \mathrm{e}^z \rvert = \mathrm{e}^{\mathop{\text{Re}}(z)}$$ (und demnach insbesondere auch $$\lvert \mathrm{e}^z \rvert \le \mathrm{e}^{\lvert z \rvert}$$ aufgrund der Monotonie von $$\exp$$) für alle $$z \in \mathbb{C}$$.
- Wert des Gaußschen Integrals: $$\int_{-\infty}^{\infty} \mathrm{e}^{-x^2} = \sqrt{\pi}$$ (s. auch [unten](#fun-facts)).

### Aufgabe 3
- Hier ist vielleicht die Aussage das Interessanteste, der Beweis ist sehr ähnlich zu bereits in der Vorlesung Gesehenen.

## Fun Facts

In Aufgabe 2 haben wir das Integral $$I := \int_{-\infty}^{\infty} \mathrm{e}^{-x^2} \,\mathrm{d}x = \sqrt{\pi}$$ verwendet, auch bekannt als [Gaußsches Integral](https://en.wikipedia.org/wiki/Gaussian_integral).
Hierzu könnte man aufgrund der weitreichenden Anwendungen dieses Integrals (beispielsweise in der Stochastik oder im Zusammenhang mit der Fouriertransformation) sicherlich sehr viele Fakten und Berechnungsmethoden aufzählen, aber hier vielleicht nur zwei meiner persönlichen Favoriten:
- Das Integral kann sehr elegant mithilfe von Methoden der Funktionentheorie (um genau zu sein, dem Residuensatz) berechnet werden (s. Example 3.10 im Skript von Prof. Frank).
- Vermutlich die berühmteste (und auch wirklich sehr schöne) auf Poisson zurückgehende Methode das Integral zu berechnen, ist es $$I^2$$ zu berechnen, indem man den Transformationssatz anwendet und zu Polarkoordinaten übergeht.
  Eine natürliche Frage wäre, ob man diesen Trick öfter, also auch für andere Integrale, anwenden kann -- in der Tat ist dies im Wesentlichen aber nur für die Gaußfunktion möglich.
  In den Worten von Dawson (s. Referenz unten):
  > "One question that must have occurred to many over the years is: What else can I do with it? The surprising answer to this natural question is: Absolutely nothing!"

  Für eine präzisere Formulierung als "im Wesentlichen" und den recht kurzen Beweis (sowie auch für die ausführliche Version der oben beschriebenen Berechnung), siehe:
  - [Dawson, R. J. MacG. (2005). On a “Singular” Integration Technique of Poisson. The American Mathematical Monthly, 112(3), 270–272.](https://doi.org/10.1080/00029890.2005.11920195)

  Hierzu kann man sich, wenn man möchte, auch etwas mit der [Cauchyschen Funktionalgleichung](https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation) auseinandersetzen, welche im Beweis eine Rolle spielt.

Der Vollständigkeit halber sind hier auch noch ein paar weitere Berechnungsmethoden und ein wenig historischer Kontext: [Keith Conrad - The Gaussian Integral](https://kconrad.math.uconn.edu/blurbs/analysis/gaussianintegral.pdf).
