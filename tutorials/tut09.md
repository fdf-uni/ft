# Tutorium 9

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut09/presentation.pdf)

## Kurzprotokoll
Nach einer Besprechung des obigen Foliensatzes wurden zunächst Aufgaben 3 und 4 sowie zuletzt Aufgabe 2 des aktuellen Arbeitsblattes besprochen.

## Zum Mitnehmen

### Aufgabe 2
Ich denke hier sind vor allem die Eigenschaften gebrochen linearer Transformationen relevant, sowie die Feststellung, dass diese auch aus geometrischer Sicht sehr sinnvoll sind (vgl. Aufgabenteil (iv)).

### Aufgabe 3
- Das Lemma von Schwarz kann mittels konformer Äquivalenz auch Aussagen über andere Mengen liefern.

### Aufgabe 4
Für Teil (i):
- (Mögliche Teil-)Intuition zu Blaschke-Faktoren: Für jedes $$\alpha \in \mathbb{D}$$ ist $$\psi_{\alpha}$$ eine konforme Abbildung $$\mathbb{D} \to \mathbb{D}$$, welche "die Rollen von $$0$$ und $$\alpha$$ vertauscht".
- Geometrische Überlegung zum Lemma von Schwarz: Entweder wandert unter der Abbildung jeder Punkt (bis auf $$0$$) näher zum Ursprung oder es handelt sich bei der Abbildung nur um eine Rotation der Kreisscheibe.
    In diesem Fall kann diese Vorstellung recht viel helfen: Da wir einen Fixpunkt ungleich dem Ursprung haben, der also insbesondere nicht näher zum Ursprung geht, muss es sich um eine Rotation handeln, und wieder aufgrund der Fixierung dieses Punktes muss diese trivial sein.

Für Teil (ii):
- Um holomorphe Funktionen auf einer gegebenen offenen Menge zu analysieren, kann es hilfreich sein, konforme Äquivalenz auszunutzen. In diesem Fall nutzen wir, dass wenn $$U$$ und $$V$$ konform äquivalent sind, entweder sowohl $$U$$ als auch $$V$$ die Fixpunkteigenschaft für holomorphe Funktionen besitzen oder beide nicht.
    Dann wird die Aufgabe deutlich leichter, weil es signifikant einfachere fixpunktfreie, holomorphe Abbildungen $$H \to H$$ als $$\mathbb{D} \to \mathbb{D}$$ gibt.

## Fun Facts

Diese Woche ist vielleicht die [Riemannsche Zahlenkugel](https://de.wikipedia.org/wiki/Riemannsche_Zahlenkugel) (engl. [Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere)) schön gesehen zu haben, da diese auch etwas Intuition zur Wirkung von Möbiustransformationen auf die erweiterte Komplexe Ebene $$\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$ vermitteln kann (denn Möbiustransformationen sind genau die Automorphismen der Riemann sphere).
Ein wenig kann man über diese auch auf Seiten 88 f. im Buch von Stein und Shakarchi lesen, die extreme Kurzfassung ist aber, dass wir von der Intuition her $$\hat{\mathbb{C}}$$ visualisieren können, indem wir die Ebene im Unendlichen nach oben "zusammenziehen" und dort mit dem neuen Punkt $$\infty$$ verkleben (rigoros wird dies durch stereographische Projektion).
Einigen aus dem Lehramt dürfte diese Konstruktion auch von der erweiterten reellen Gerade $$\hat{\mathbb{R}} = \mathbb{R} \cup \{\infty\}$$ bekannt vorkommen, welche man sich als Kreis vorstellen kann.

Um den Begriff einmal erwähnt zu haben, sei angemerkt, dass beide Konstruktionen Spezialfälle der sogenannten [Alexandroff-Kompaktifizierung](https://de.wikipedia.org/wiki/Alexandroff-Kompaktifizierung) sind (welche allerdings zumindest laut des Wikipedia-Artikels als Verallgemeinerung der Riemann sphere entdeckt wurde).

Wie gesagt, ist die Riemann sphere für uns vielleicht gerade deshalb interessant, weil sie etwas klarer macht, wie die Abbildung $$z \mapsto \frac{1}{z}$$ auf $$\hat{\mathbb{C}}$$ wirkt, da diese Funktion die Riemann sphere entlang der rellen Achse einfach nur um den Winkel $$\pi$$ rotiert.
Insbesondere werden $$0$$ und $$\infty$$ vertauscht.
Da Geraden auf der Riemann sphere Kreise sind, die durch $$\infty$$ verlaufen, kann man sich damit dann leicht die Aussagen aus Aufgabe (v) überlegen, zum Beispiel, dass Kreise, die durch den Ursprung verlaufen, durch $$z \mapsto \frac{1}{z}$$ auf Geraden, die nicht durch den Ursprung verlaufen, abgebildet werden.
