---
title: Tutorium 8
---

## Kurzprotokoll

Aus Zeitgründen und da dies besser zum Tutoriumsblatt passte, gab es in dieser Woche keinen Foliensatz und wir wiederholten stattdessen relevante Resultate direkt während der Besprechung der Aufgaben.

## Zum Mitnehmen

### Aufgabe 1
- Bestimmen von Laurent-Reihen gebrochen-rationaler Funktionen mittels der geometrischen Reihe.
    Diesbezüglich insbesondere die Intuition basierend auf geometrischen Skizzen, wann man hierbei eine Bedingung der Form $$\lvert z - z_0 \rvert < C$$ und wann man eine Abschätzung der Form $$c < \lvert z - z_0 \rvert$$ verwenden möchte (und dementsprechend Terme mit nicht-negativen oder nicht-positiven Exponenten erhält).
- Zur Partialbruchzerlegung, welche hierbei auch oft sehr nützlich ist, sei an dieser Stelle auf ein [entsprechendes Dokument](../../assets/2025/tut05/partialbruchzerlegung.pdf) aus dem Vorjahr verwiesen (insbesondere Beispiel 3 ist bei Anwendungen wie in dieser Aufgabe wahrscheinlich von Interesse).

### Aufgabe 2
Anwendung des Maximumprinzips zur Bestimmung von Suprema holomorpher Funktionen auf offenen zusammenhängenden Mengen.

### Aufgabe 3
Ich denke hier sind vor allem die Eigenschaften von [Möbiustransformationen](https://de.wikipedia.org/wiki/M%C3%B6biustransformation#M%C3%B6biustransformation_als_Automorphismus_der_riemannschen_Zahlenkugel) relevant, sowie die Feststellung, dass diese auch aus geometrischer Sicht (oder genau deshalb) sehr sinnvoll sind (vgl. Aufgabenteil (iv)).

Leider haben wir Aufgabenteil (v) im Tutorium zeitlich nicht mehr ganz ausführlich besprechen können, weshalb ich hier meine Lösung an die Tafel projizierte.
Allerdings war auf dem Bild die erste Zeile abgeschnitten, wodurch zu Beginn des Beweises noch ein kleiner Schritt gefehlt hat: Gemäß Aufgabenteil (iv) genügt es nämlich, die Aussage, dass Möbiustransformationen Kreise und Geraden wieder auf Kreise oder Geraden abbilden, für Translationen, Rotationen und Inversion zu beweisen.
Für Translationen und Rotationen ist dies offensichtlich, und nur für Inversionen muss man etwas mehr arbeiten.
Letzteres war dann der gezeigte Teil des Beweises.

An dieser Stelle sei vielleicht auch erwähnt, dass es eine sehr schöne alternative Argumentation über das sogenannte _Doppelverhältnis_ gibt, welches für vier Punkte $$z_1, z_2, z_3, z_4 \in \mathbb{C}$$ mittels
\\[
[z_1, z_2, z_3, z_4] := \frac{z_1-z_3}{z_1-z_4} : \frac{z_2-z_3}{z_2-z_4}
\\]
definiert ist.
Mit Aufgabenteil (iv) folgt leicht, dass dieses invariant unter Möbius-Transformationen ist, also $$[T(z_1), T(z_2), T(z_3), T(z_4)] = [z_1, z_2, z_3, z_4]$$ für jede Möbiustransformation $$T$$ gilt.
Beispielsweise für den Fall, dass $$T(z) = a z$$ eine Drehstreckung ist, kürzt sich der Faktor $$a$$ einfach bei beiden Brüchen.
Man kann sodann sehr schön auf elementargeometrische Weise argumentieren, dass $$[z_1, z_2, z_3, z_4]$$ genau dann reell ist, wenn die vier Punkte auf einer Gerade oder einem Kreis liegen (s. beispielsweise [diesen Post](https://math.stackexchange.com/questions/4225947/) auf dem Mathematics Stack Exchange).
Damit folgt dann die Behauptung.

## Fun Facts

Diese Woche ist vielleicht die [Riemannsche Zahlenkugel](https://de.wikipedia.org/wiki/Riemannsche_Zahlenkugel) (engl. [Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere)) schön gesehen zu haben, da diese auch etwas Intuition zur Wirkung von Möbiustransformationen auf die erweiterte Komplexe Ebene $$\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$ vermitteln kann (denn Möbiustransformationen sind genau die Automorphismen der Riemannschen Zahlenkugel).
Ein wenig kann man über diese auch auf Seiten 88 f. im Buch von Stein und Shakarchi lesen, die extreme Kurzfassung ist aber, dass wir von der Intuition her $$\hat{\mathbb{C}}$$ visualisieren können, indem wir die Ebene im Unendlichen nach oben zum neuen Punkt $$\infty$$ "zusammenziehen" (rigoros wird dies durch stereographische Projektion).
Vielleicht ist diese Konstruktion auch bereits von der erweiterten reellen Gerade $$\hat{\mathbb{R}} = \mathbb{R} \cup \{\infty\}$$ bekannt, welche man sich analog als Kreis vorstellen kann.

Um den Begriff einmal erwähnt zu haben, sei angemerkt, dass beide Konstruktionen Spezialfälle der sogenannten [Alexandroff-Kompaktifizierung](https://de.wikipedia.org/wiki/Alexandroff-Kompaktifizierung) sind (welche allerdings zumindest laut des verlinkten Wikipedia-Artikels als Verallgemeinerung der Riemannschen Zahlenkugel entdeckt wurde).

Für uns ist die Riemannsche Zahlenkugel vielleicht gerade deshalb interessant, weil sie etwas klarer macht, wie die Abbildung $$z \mapsto \frac{1}{z}$$ auf $$\hat{\mathbb{C}}$$ wirkt, da diese Funktion die Riemannsche Zahlenkugel einfach nur entlang der rellen Achse um den Winkel $$\pi$$ rotiert.
Insbesondere werden $$0$$ und $$\infty$$ vertauscht.
Da Geraden auf der Riemannsche Zahlenkugel Kreise sind, die durch $$\infty$$ verlaufen, kann man sich damit dann leicht die präziseren Aussagen aus Aufgabe (v) überlegen, zum Beispiel, dass Kreise, die durch den Ursprung verlaufen, durch $$z \mapsto \frac{1}{z}$$ auf Geraden, die nicht durch den Ursprung verlaufen, abgebildet werden.
Ein paar schöne Animationen hierzu finden sich beispielsweise in [diesem Youtube-Video](https://www.youtube.com/watch?v=hhI8fVxvmaw).
