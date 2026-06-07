---
title: Tutorium 5
---

[Foliensatz](../../assets/2026/tut05/presentation.pdf)

## Kurzprotokoll

Wir begannen wieder mit einer Besprechung des Foliensatzes und gingen dann zu den Aufgaben über.
Aufgrund des vorlesungsfreien Dienstags fand zudem nur ein Tutorium statt.

## Zum Mitnehmen

### Aufgabe 1
- Für die Berechnung von Lösungen gewisser polynomieller Gleichungen sind Polarkoordinaten sehr gut geeignet (konkret etwa Gleichungen wie $$z^n = z_0$$ für ein $$z_0 \in \mathbb{C}$$).
- Grundsätzliche Anwendung des Residuensatzes (s. auch [Tutorium 6](./tut06.md) und den dort verlinkten "Hilfszettel").

### Aufgabe 2
- Hier ist wichtig, mit der Verwendung von Lemma 3.3 aus der Vorlesung zur Berechnung der Residuen von Polstellen gut umgehen zu können.
- Außerdem ist es nützlich, eine Intuition für die jeweilige Art einer Polstelle zu kriegen, aber auch hierzu ein wenig mehr beim Hilfszettel von [Tutorium 6](./tut06.md).

### Aufgabe 3
- Intuitiv ist bei dieser Aufgabe vielleicht ein wenig die Idee, dass eine holomorphe Funktion zu "rigide" ist, um eine Singularität zu besitzen, welche langsamer als eine einfache Polstelle wächst.
    Formalisiert wird dies dann natürlich durch Resultate wie den Riemannschen Hebbarkeitssatz (vgl. Musterlösung).

## Fun Facts

Zu Beginn des Tutoriums besprachen wir, inwiefern der Begriff der wesentlichen Singularität "gerechtfertigt" ist, in dem Sinne, dass die Definition _weder hebbar noch Polstelle_ nicht so willkürlich ist, wie sie zunächst scheinen könnte.
Man könnte ja schließlich erwarten, dass außerhalb dieser Begriffe noch eine Vielzahl an unterschiedlichen Verhalten bestehen könnten, die wir nun alle unter einem Begriff zusammenfassen.
Hier ist gegebenenfalls auch ein Vergleich mit reellen Funktionen angebracht, wo beispielsweise auch Sprungstellen wie bei der [Heaviside-Funktion](https://de.wikipedia.org/wiki/Heaviside-Funktion) oder wilde, aber beschränkte Oszillation wie bei der Funktion $$x \mapsto \sin(\frac{1}{x})$$ bestehen können.

Dass der Begriff der wesentlichen Singularität aber ein sinnvoller ist, wird durch den Satz von Casorati-Weierstraß unterstrichen, welcher uns intuitiv sagt, dass die gegebene Funktion sich bei wesentlichen Singularitäten "extrem wild" verhält (und auch die Funktion $$z \mapsto \sin(\frac{1}{z})$$ hört natürlich auf einer komplexen Umgebung der Null auf, beschränkt zu sein).
Noch mehr wird dies durch den [großen Satz von Picard](https://de.wikipedia.org/wiki/Satz_von_Picard) bekräftigt, welcher der diesmalige fun fact ist und eine starke Verallgemeinerung des Satzes von Casorati-Weierstraß darstellt: Das Bild einer Umgebung einer wesentlichen Singularität liegt nicht nur dicht in $$\mathbb{C}$$, sondern beinhaltet sogar bis auf höchstens eine Ausnahme jede komplexe Zahl unendlich oft.
