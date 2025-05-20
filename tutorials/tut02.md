# Tutorium 2

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut02/presentation.pdf)

## Kurzprotokoll

Nach einer kurzen Wiederholung von Holomorphie und ein wenig Intuition zu den Cauchy-Riemann-Gleichungen (s. Foliensatz), besprachen wir Aufgaben 1 bis 3.

Hinsichtlich der Cauchy-Riemann-Gleichungen haben wir auch kurz über konforme Abbildungen geredet, was in Kapitel 6, Aufgabe 2 von Stein, Shakarchi genauer formuliert wird (jetzt aber vielleicht noch nicht unbedingt sauber bewiesen werden kann und dem Vorlesungsstoff vorgreifen würde).

Eine schöne Animation, welche auch kurz gezeigt wurde, findet sich in [diesem Youtube-Video](https://www.youtube.com/watch?v=0CHZMY02Dhk&t=640s).

Zum Ende des Tutoriums besprachen wir noch kurz eine alternative Interpretation der Cauchy-Riemann-Gleichungen, nämlich dass diese sicher stellen, dass die Jacobi-Matrix von $$F$$ zu einer komplexen Zahl korrespondiert (mittels des Isomorphismus von Ringen/Körpern
\\[
  \mathbb{R}^{2 \times 2} \ni \begin{pmatrix} a & -b \\\\ b & a \end{pmatrix} \mapsto a + b \mathrm{i} \in \mathbb{C}
\\]
).
Auch dies ist natürlich nur eine von vielen möglichen Interpretation, s. zum Beispiel auch [Wikipedia](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations#Interpretation_and_reformulation), [stackexchange](https://math.stackexchange.com/questions/3818096/is-there-any-intuition-or-meaning-regarding-cauchy-riemann-equations) oder Seiten 143 bis 145 von [Wegert - Visual Complex Functions](https://link.springer.com/book/10.1007/978-3-0348-0180-5) (zugänglich über den Bibliotheks-Login).

## Zum Mitnehmen

### Aufgabe 1
- Definition von Holomorphie und Cauchy-Riemann-Gleichungen.
- "Holomorphie ist eine ziemlich restriktive Eigenschaft."
- "Komplexe Konjugation und Holomorphie vertragen sich nicht gut."

### Aufgabe 2
- Das Wurzelkriterium ist "stärker" als das Quotientenkriterium.
  Ein Beispiel, das zeigt, dass es wirklich _strikt_ stärker ist, findet sich in Tutorium 3 als kurzer Nachtrag.
- Trick, Ungleichungen iterativ anzuwenden, um Ungleichungen "im Grenzwert" zu beweisen (vgl. z.B. auch Beweis des Banachschen Fixpunktsatzes, wie er etwa in [Forster - Analysis 2](https://link.springer.com/book/10.1007/978-3-658-45812-6) gefunden werden kann).

### Aufgabe 3
- Der Entwicklungspunkt von Potenzreihen kann _innerhalb des Konvergenzkreises_ verschoben werden.
- Binomischer Lehrsatz.
- Rigoroses Argumentieren beim Vertauschen von Doppelreihen (z.B. Fubini mit Zählmaß (streng genommen in dieser Form eigentlich Pringsheim zuzuschreiben und in gewisser Weise implizit in manchen Beweisen von Fubini verwendet) oder mithilfe von summierbaren Familien, vgl. [Königsberger  - Analysis 1](https://link.springer.com/book/10.1007/978-3-642-18490-1)).

## Fun Facts

Die Voraussetzung von Aufgabe 1 (iii) kann deutlich abgeschwächt werden zu "$$\mathop{\text{Re}}(f)$$ beschränkt" statt "$$\mathop{\text{Re}}(f)$$ konstant".
Dies ist eine Konsequenz des Satzes von Liouville, welchen wir später in der Vorlesung sehen werden.
