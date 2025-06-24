# Tutorium 8

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut08/presentation.pdf)

## Kurzprotokoll
Wie auch die anderen Tutorien begann dieses Tutorium mit der Besprechung des oben verlinkten Foliensatzes und endete mit der Besprechung der Aufgaben.

Zu Beginn haben wir auch über den Namen des Argumentprinzips geredet.
Hierfür als (nicht im Tutorium besprochene) Ergänzung folgende "formale" Rechnung (das heißt ohne Beachtung von Fragen bezüglich -- bzw. Überprüfen von -- Konvergenz, Differenzierbarkeit, etc.): Schreiben wir $$f(z) = r(z) \mathrm{e}^{\mathrm{i} \vartheta(z)}$$ in einer Umgebung von $$C$$ mit $$r(z) > 0$$ (man beachte, dass $$f$$ keine Nullstellen auf $$C$$ hat) und $$\vartheta(z) \in \mathbb{R}$$, so erhalten wir im Argumentprinzip mithilfe der Produktregel:
\\[
    \begin{aligned}
    \frac{1}{2 \pi \mathrm{i}} \int_{C} \frac{f'(z)}{f(z)} \,\mathrm{d}z &= \frac{1}{2 \pi \mathrm{i}} \int_{C} \frac{r'(z) \mathrm{e}^{\mathrm{i} \vartheta(z)}}{r(z) \mathrm{e}^{\mathrm{i} \vartheta(z)}} + \frac{r(z) \mathrm{e}^{\mathrm{i} \vartheta(z)} \vartheta'(z)}{r(z) \mathrm{e}^{\mathrm{i} \vartheta(z)}} \,\mathrm{d}z \\
                &= \frac{1}{2 \pi \mathrm{i}} \left[ \int_{C} \frac{r'(z)}{r(z)} \,\mathrm{d}z + \int_{C} \vartheta'(z) \,\mathrm{d}z \right]
    \end{aligned}
\\]
Wir wählen nun noch eine Parametrisierung für $$C$$, sagen wir $$z \colon [0, 2 \pi] \to C$$.
Da $$C$$ geschlossen ist, verschwindet das erste Integral gemäß Hauptsatz der Differential- und Integralrechnung:
\\[
    \begin{aligned}
    \int_{C} \frac{r'(z)}{r(z)} \,\mathrm{d}z &= \int_{0}^{2 \pi} \frac{r'(z(t)) z'(t)}{r(z(t))} \,\mathrm{d}t = \int_{0}^{2 \pi} \frac{\mathrm{d}}{\mathrm{d}t} \ln(r(z(t))) \,\mathrm{d}t \\
    &= \ln(r(z(2 \pi))) - \ln(r(z(0))) = 0.
    \end{aligned}
\\]
Das zweite Integral kann ebenfalls direkt berechnet werden:
\\[
    \int_{C} \vartheta'(z) \,\mathrm{d}z = \int_{0}^{2 \pi} \vartheta'(z(t)) z'(t) \,\mathrm{d}t = \vartheta(z(2 \pi)) - \vartheta(z(0)).
\\]
Dies ist die Gesamtänderung des Arguments (also des "Winkels") von $$f(z)$$ während $$z$$ entlang $$C$$ läuft!
Das ist also der Ursprung des Namens.

Diese Rechnung gibt auch Anlass zu einer schönen Visualisierung, indem man sich für jeden Punkt $$z$$ des Kreises, über welchen integriert wird, überlegt, was das Argumment von $$f(z)$$ ist.
Hierfür kann man einen Pfeil, beginnend bei $$z$$, betrachten, der in Richtung $$e^{\vartheta(z)}$$ zeigt.

Dies ist in der folgenden Animation dargestellt, die wir in den Tutorien angeschaut haben.
Der Einfachheit halber wird hier für $$C$$ der Einheitskreis betrachtet:

{:refdef: style="text-align: center;"}
![Veranschaulichung des Argumentprinzips](../assets/tut08/argument_principle.gif)

Wir sehen, dass die Ordnung der Null- oder Polstelle mit der Gesamtanzahl an Umdrehungen des oben beschriebenen Pfeils übereinstimmt, wobei die Richtung, in welche rotiert wird, angibt, ob es sich um eine Null- oder Polstelle handelt.

Man vergleiche auch die entstehenden Einfärbungen des Einheitskreises mit den [letzte Woche](./tut07.md) besprochenen domain colorings, insbesondere dem Ablesen von Null- und Polstellen mitsamt Ordnung aus diesen, was wie wir nun gesehen haben aufgrund des Argumentprinzips funktioniert (s. für Details beispielsweise das letzte Woche verlinkte Buch von E. Wegert).

Natürlich ist obige Argumentation nicht allzu rigoros (wer will, kann sich gerne überlegen, wo Lücken sind und versuchen, diese zu schließen).

Insbesondere falls man Umlaufzahlen kennt, ist aber vielleicht diese Interpretation des Argumentprinzips schön gesehen zu haben.[^1]

[^1]: In diesem Fall kann man sich aber auch überlegen, dass die linke Seite des Integrals der Umlaufzahl von $$f(C)$$ um den Ursprung entspricht.

## Zum Mitnehmen

### Aufgabe 1
- Rechnen mit $$\operatorname{Log}$$ und komplexen Potenzen.
- Vorsicht: Im Allgemeinen übertragen sich bekannte Rechenregeln für Potenzen nicht direkt aus dem Reellen ins Komplexe. Hier sollte man vielleicht auch etwas aufpassen und $$\mathrm{e}^z$$ _nicht_ als "$$\mathrm{e}$$ hoch $$z$$" lesen (auch wenn man das immer so sagt und natürlich auch die Schreibweise dazu veranlasst), sondern sich daran erinnern, dass $\mathrm{e}^z$ die über die Potenzreihe $$\sum_{k=0}^{\infty} \frac{z^k}{k!}$$ definierte komplexe Exponentialfunktion bezeichnet.
    Hierdurch kann man auch Fehler wie $$\mathrm{e}^{z w} = (\mathrm{e}^z)^w$$ vermeiden, was ein Beispiel für eine Rechenregel ist, die sich nicht direkt für beliebige $z, w \in \mathbb{C}$ übertragen lässt.
    Man betrachte beispielsweise $z = w = \mathrm{i} \pi$ in welchem Fall die rechte Seite der Gleichung mit unsere Definition über den Hauptzweig des Logarithmus nicht definiert ist -- aber selbst wenn die rechte Seite definiert ist, so hängt sie ja noch immer von der Wahl des Logarithmus ab und für eine andere Wahl können beide Seiten voneinander abweichen.

### Aufgabe 3
- Wiederholung der umgekehrten Dreiecksungleichung und Anwenden des Satzes von Rouché.
- Für Letzteres ist der Trick oft, eine gegebene Gleichung umzuformen zu einer Nullstellengleichung.

### Aufgabe 5
- [Der Residuensatz gilt auch für wesentliche Singularitäten](), allerdings hat man hier nicht eine direkte Formel wie für die Residuen bei Polstellen (vgl. Lemma 3.3), sondern muss explizit die Laurent-Entwicklung berechnen, um die Residuen ermitteln zu können.

## Fun Facts

Siehe obige Visualisierung des Argumentprinzips. :)
