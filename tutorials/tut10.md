# Tutorium 10

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut10/presentation.pdf)

## Kurzprotokoll
Es gab auch diese Woche nichts Außergewöhnliches: Nach der Besprechung des Foliensatzes gingen wir direkt zu den Aufgaben über.

## Zum Mitnehmen

### Aufgabe 2
- Genau wie es Teleskop-Summen gibt, gibt es auch Teleskop-Produkte und zur Berechnung von Grenzwerten kann es hilfreich sein, ein Produkt zu einem Teleskop-Produkt umzuformen.

### Aufgabe 3
- Eine Klassifizierung der konformen Abbildungen $$U \to V$$ kann mithilfe von konkreten konformen Abbildungen auf die Automorphismen bekannter Mengen zurückgeführt werden.  
  Hier haben wir beispielsweise die Form von konformen Abbildungen $$f \colon \mathbb{H} \to \mathbb{D}$$ bestimmt, indem wir die konforme Abbildung $$G \colon \mathbb{D} \to \mathbb{H}$$ aus der Vorlesung vorschalten und hierdurch das Resultat über $$\operatorname{Aut}(\mathbb{D})$$ auf $$\tilde{f} = f \circ G$$ anwenden können.

### Aufgabe 5
Verfahren zum Berechnen der Hadamard-Produktdarstellung einer ganzen Funktion $$f \neq 0$$:
1. Bestimme die Wachstumsordnung $$\rho_0$$ von $$f$$ und setze $$k = \lfloor \rho_0 \rfloor$$.
2. Bestimme die Nullstellen von $$f$$ mitsamt Vielfachheit.
3. Zu diesem Zeitpunkt kann man folgern, dass
    \\[
        f(z) = \mathrm{e}^{P(z)} \underbrace{z^m \prod_{n = 1}^{\infty} E_k\left(\frac{z}{b_n}\right)}_{=: g(z)},
    \\]
    wobei $$P$$ ein Polynom von Grad $$\le k$$, $$m$$ die in Schritt 2 bestimmte Ordnung der Nullstelle $$0$$ und $$(b_n)_{n \in \mathbb{N}}$$ die ebenfalls im Vorherigen Schritt bestimmte Folge der Nullstellen $$\neq 0$$ von $$f$$ mitsamt Vielfachheit ist.

    An dieser Stelle kann es sinnvoll sein, das Produkt auf der rechten Seite möglichst weit zu vereinfachen.
4. Zuletzt muss noch das Polynom $$P$$ bestimmt werden. Hier kann es hilfreich sein, $$P(z) = c_0 + c_1 z + \dots + c_k z^k$$ zu schreiben und dann zu versuchen, Symmetrien von $$f$$ und $$g$$ auszunutzen, da für alle $$z \in \mathbb{C} \setminus g^{-1}(\{0\})$$ gilt, dass $$\mathrm{e}^{P(z)} = \frac{f(z)}{g(z)}$$ (man beachte, dass $$g^{-1}(\{0\})$$ aufgrund von $$f \neq 0$$ höchstens abzählbar ist).  
    In dieser Aufgabe waren beispielsweise die Symmetrien $$f(-z) = f(z)$$, $$g(-z) = g(z)$$ sowie $$f(\mathrm{i})(z) = - \mathrm{e}^{-2 \pi z^2} f(z)$$, $$g(\mathrm{i} z) = - g(z)$$ hilfreich.

    Am Leichtesten ist oft der konstante Koeffizient $$c_0$$, denn für diesen können wir einfach $$\lim_{z \to 0} \frac{f(z)}{z^m}$$ betrachten.
    Aufgrund der gleichmäßigen Konvergenz des Produktes in $$g$$ in $$\mathbb{D}$$ gemäß Proposition 4.3 aus der Vorlesung gilt nämlich $$\lim_{z \to 0} \frac{g(z)}{z^m} = 1$$ (das sollte man gegebenenfalls nochmal etwas konkreter nachweisen!).
    Damit erhält man dann $$\lim{z \to 0} \frac{f(z)}{z^m} = \mathrm{e}^{P(0)} = \mathrm{e}^{c_0}$$ was nach $$c_0$$ umgeformt werden kann.
    

## Fun Facts

Gemäß des Weierstraßschen Produktsatzes gibt es zu jeder Folge $$(a_n)_{n \in \mathbb{N}} \subset \mathbb{C}$$ mit $$\lvert a_n \rvert \to \infty$$ eine ganze Funktion, welche genau bei diesen $$a_n$$ Nullstellen besitzt.
Umgekehrt könnte man sich Fragen, ob man auch Singularitäten anstelle von Nullstellen betrachten könnte, worauf der [Satz von Mittag-Leffler](https://de.wikipedia.org/wiki/Satz_von_Mittag-Leffler) eine positive Antwort liefert.
Tatsächlich besagt dieser noch mehr (sonst könnte man ja auch einfach $$1/f$$ betrachten), denn es können sogar die Hauptteile der Funktion in den $$a_n$$'s vorgeschrieben werden.
Das ist ähnlich wie der Weierstraßsche Produktsatz auf gewisse Weise eine Verallgemeinerung von Polynomfaktorisierung ist, eine Verallgemeinerung der Partialbruchzerlegung, man erinnere sich beispielsweise auch an die Partialbruchzerlegung von $$\cot$$ aus der Vorlesung (Beispiel 3.9 bzw. Lemma 4.5).
Dies wird auch ein wenig mit Bezug auf die [Weierstraßsche ℘-Funktion](https://de.wikipedia.org/wiki/Weierstra%C3%9Fsche_%E2%84%98-Funktion) in dem folgenden Klassiker zur Funktionentheorie beschrieben (s. Kapitel IV.3 und eventuell auch noch zu Produkten IV.2):

- [Freitag, E., & Busam, R. (2006). Funktionentheorie 1. In Springer-Lehrbuch. Springer Berlin Heidelberg.](https://doi.org/10.1007/3-540-32058-X)

Natürlich sind die Sätze von Mittag-Leffler und Weierstraß miteinander verwandt, beispielsweise durch logarithmisches Differenzieren.
