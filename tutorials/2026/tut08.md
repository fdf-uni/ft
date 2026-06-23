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
Anwendung des Maximumprinzips zur Bestimmung von Maxima holomorpher Funktionen auf offenen zusammenhängenden Mengen.

### Aufgabe 3
Ich denke hier sind vor allem die Eigenschaften von [Möbiustransformationen](https://de.wikipedia.org/wiki/M%C3%B6biustransformation#M%C3%B6biustransformation_als_Automorphismus_der_riemannschen_Zahlenkugel) relevant, sowie die Feststellung, dass diese auch aus geometrischer Sicht sehr sinnvoll sind (vgl. Aufgabenteil (iv)).

## Fun Facts

Diese Woche ist vielleicht die [Riemannsche Zahlenkugel](https://de.wikipedia.org/wiki/Riemannsche_Zahlenkugel) (engl. [Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere)) schön gesehen zu haben, da diese auch etwas Intuition zur Wirkung von Möbiustransformationen auf die erweiterte Komplexe Ebene $$\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$ vermitteln kann (denn Möbiustransformationen sind genau die Automorphismen der Riemannschen Zahlenkugel).
Ein wenig kann man über diese auch auf Seiten 88 f. im Buch von Stein und Shakarchi lesen, die extreme Kurzfassung ist aber, dass wir von der Intuition her $$\hat{\mathbb{C}}$$ visualisieren können, indem wir die Ebene im Unendlichen nach oben zum neuen Punkt $$\infty$$ "zusammenziehen" (rigoros wird dies durch stereographische Projektion).
Vielleicht ist diese Konstruktion auch bereits von der erweiterten reellen Gerade $$\hat{\mathbb{R}} = \mathbb{R} \cup \{\infty\}$$ bekannt, welche man sich analog als Kreis vorstellen kann.

Um den Begriff einmal erwähnt zu haben, sei angemerkt, dass beide Konstruktionen Spezialfälle der sogenannten [Alexandroff-Kompaktifizierung](https://de.wikipedia.org/wiki/Alexandroff-Kompaktifizierung) sind (welche allerdings zumindest laut des verlinkten Wikipedia-Artikels als Verallgemeinerung der Riemannschen Zahlenkugel entdeckt wurde).

Für uns ist die Riemannsche Zahlenkugel vielleicht gerade deshalb interessant, weil sie etwas klarer macht, wie die Abbildung $$z \mapsto \frac{1}{z}$$ auf $$\hat{\mathbb{C}}$$ wirkt, da diese Funktion die Riemannsche Zahlenkugel einfach nur entlang der rellen Achse um den Winkel $$\pi$$ rotiert.
Insbesondere werden $$0$$ und $$\infty$$ vertauscht.
Da Geraden auf der Riemannsche Zahlenkugel Kreise sind, die durch $$\infty$$ verlaufen, kann man sich damit dann leicht die Aussagen aus Aufgabe (v) überlegen, zum Beispiel, dass Kreise, die durch den Ursprung verlaufen, durch $$z \mapsto \frac{1}{z}$$ auf Geraden, die nicht durch den Ursprung verlaufen, abgebildet werden.
