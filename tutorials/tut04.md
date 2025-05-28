# Tutorium 4

[Zurück zur Startseite](../README.md)

[Foliensatz](../assets/tut04/presentation.pdf)

## Kurzprotokoll
Wir gingen kurz über den Foliensatz, wobei wir auch [diese Animation](https://upload.wikimedia.org/wikipedia/commons/7/7e/HomotopySmall.gif) zu homotopen Kurven besprachen, welche eine mögliche Intuition für Homotopie demonstriert, nämlich den (bei uns) zweiten Parameter als Zeitvariable aufzufassen.

Daraufhin wurden die Aufgaben besprochen.

## Zum Mitnehmen

### Aufgabe 1
- Skizzen mit den Singularitäten/Problemstellen und der Integrationskurve können hilfreich sein, um zu erkennen, welche der Ersteren einen Einfluss auf das Kurvenintegral haben.
- Trick, Faktoren der Form $$\frac{1}{(z - z_0)^{n + 1}}$$, $$n \in \mathbb{N}_0$$, auszuklammern, um dann (nach Überprüfen der Voraussetzungen) die Cauchysche Integralformel anzuwenden.

### Aufgabe 2
- Topologisches Argument: Ist $$(X, \mathcal{T})$$ ein zusammenhängender topologischer Raum und $$A \subset X$$ offen und abgeschlossen, so folgt $$A \in \{\emptyset, X\}$$.
  (Wie in den Tutorien angemerkt, gilt hier natürlich auch die Rückrichtung, d.h. $$(X, \mathcal{T})$$ ist genau dann zusammenhängend, wenn die einzig zugleich offen und abgeschlossenen Mengen $$\emptyset$$ und $$X$$ selbst sind. Dies haben wir allerdings nicht weiter ausgeführt.)
- Wiederholung: Eine Teilmenge $$M$$ eines metrischen Raumes ist genau dann offen, wenn für jedes $$x \in M$$ ein $$r_x > 0$$ mit $$B_{r_x}(x) \subset M$$ existiert (Beweis: "$$\Rightarrow$$": um $$x$$ zentrierte offene Bälle (rationalen Radius) als (abzählbare) Umgebungsbasis von $$x$$ in der metrisch induzierten Topologie, "$$\Leftarrow$$": "self indexing trick", d.h. $$A = \bigcup_{x \in A} A_x$$ für geeignete Mengen $$(A_x)_{x \in A}$$ mit $$x \in A_x \subset A$$ schreiben).
- $$B_r(w) = \{w\} \cup \left( \bigcup_{\tilde{r} \in (0, r)} \partial B_{\tilde{r}}(w) \right)$$.
- Intuition für Identitätssatz: Gleichheit auf "kleinen" Mengen impliziert schon Gleichheit auf "großen" Mengen (beispielsweise impliziert Gleichheit ganzer Funktionen $$f$$ und $$g$$ auf $$B_{\epsilon}(z_0)$$ für beliebiges $$z_0 \in \mathbb{C}$$ und $$\epsilon > 0$$ (das ist als überabzählbare Menge sogar schon relativ "groß") bereits Gleichheit auf ganz $$\mathbb{C}$$).
- Für $$f$$ holomorph impliziert $$\lvert f \rvert \equiv \mathrm{const.}$$, dass $$f \equiv \mathrm{const.}$$ (verwende Cauchy-Riemann Gleichungen).

### Aufgabe 3
- Erneut: Skizzen können in der Funktionentheorie sehr hilfreich sein.

## Fun Facts (dieses Mal eher ein Ausblick...)
In Aufgabe 2 haben wir letztendlich nur die Mittelwerteigenschaft holomorpher Funktionen genutzt, um zu zeigen, dass solche ihr Maximum auf dem Rand ihres Definitionsbereichs annehmen, wenn dieser beschränkt ist.

Nun kann man sich überlegen, inwiefern dies verallgemeinert werden kann.
Eine mögliche Formulierung wäre zu sagen, dass $$u \colon \Omega \to \mathbb{R}$$ mit $$\Omega \subset \mathbb{R}^n$$ offen, $$n \in \mathbb{N}$$, die Mittelwerteigenschaft besitzt, wenn
\\[
    u(x) = \frac{1}{S(\partial B_r(x))} \int_{\partial B_r(x)} u(y) \,\mathrm{d}S(y) \qquad \text{für jede Kugel } B_r(x) \subset \Omega,
\\]
wobei $$S$$ das $$(n-1)$$-dimensionale Oberflächenmaß auf $$\partial B_r(x)$$ bezeichnet.

Tatsächlich ist dies äquivalent zu folgender Mittelwerteigenschaft, bei welcher wir den Mittelwert über die gesamte Kugel anstatt nur ihres Randes, also der Sphäre, nehmen und dementsprechend anstelle des Oberflächenmaßes das $$n$$-dimensionale Lebesgue-Maß verwenden:
\\[
    u(x) = \frac{1}{\lvert B_r(x) \rvert} \int_{B_r(x)} u(y) \,\mathrm{d}y.
\\]

Für den Fall, dass $$\Omega$$ beschränkt ist, kann man mit demselben Beweis wie in Aufgabe 2 (genauer, der topologischen Variante ohne Identitätssatz) zeigen, dass solche Funktionen $$u$$, sofern sie stetig auf den Rand von $$\Omega$$ fortgesetzt werden können, $$\max_{\overline{\Omega}} u = \max_{\partial \Omega} u$$ erfüllen.
Auch hier gilt also ein Maximumprinzip.
Außerdem folgt aus der Mittelwerteigenschaft genau wie für holomorphe Funktionen Analytizität.

Der Zusammenhang mit holomorphen Funktionen ergibt sich aus folgendem Resultat: Eine Funktion $$u \colon \Omega \to \mathbb{R}$$ mit $$\Omega \subset \mathbb{R}^n$$ offen besitzt die Mittelwerteigenschaft genau dann, wenn $$u$$ harmonisch ist, d.h. $$\Delta u = 0$$.
Und wie wir auf Übungsblatt 1, Aufgabe 1 (i) gesehen haben, sind Real- und Imaginärteil holomorpher Funktionen gemäß Cauchy-Riemann stets harmonisch.

Für diejenigen, die Beweise für die obigen Aussagen sehen möchten, kann ich folgendes Buch von Evans sehr empfehlen (von diesem gibt es auch Exemplare in der Universitätsbibliothek):
- [Lawrence C. Evans. Partial differential equations (Second Edition). AMS Graduate Studies in Mathematics, Volume 19, 2010.](https://bookstore.ams.org/gsm-19-r/)

Alternativ kann man sich auch bis zum nächsten Semester noch etwas gedulden und dann die Vorlesung zu partiellen Differentialgleichungen besuchen.
Hierzu könnt ihr mich aber gerne auch nochmals im Tutorium ansprechen, falls ihr Fragen haben solltet. :)
