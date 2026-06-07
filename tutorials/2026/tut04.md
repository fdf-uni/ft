---
title: Tutorium 4
---

[Foliensatz](../../assets/2026/tut04/presentation.pdf)

## Kurzprotokoll

Nach Besprechung des (diese Woche recht kurzen Foliensatzes) gingen wir zu den Lösungen der Aufgaben über.

## Zum Mitnehmen

### Aufgabe 1
- Skizzen mit den Singularitäten/Problemstellen und der Integrationskurve können hilfreich sein, um zu erkennen, welche der Ersteren einen Einfluss auf das Kurvenintegral haben.
    Prinzipiell würde ich dies auch oft als ersten Schritt empfehlen (oder zumindest, sich die Skizze mental zu überlegen).
- Trick, Faktoren der Form $$\frac{1}{(z - z_0)^{n + 1}}$$, $$n \in \mathbb{N}_0$$, auszuklammern, um dann (nach Überprüfen der Voraussetzungen) die Cauchysche Integralformel anzuwenden.

### Aufgabe 2
- Im Wesentlichen ist die Herangehensweise hier dieselbe wie in Aufgabe 1.
    Zwei Schritte sind allerdings dennoch nützlich:
- Verwenden von Konvexität/Konkavität für Abschätzungen, in diesem Fall um beispielsweise um den Integranden $$\int_{0}^{\pi/4} \mathrm{e}^{-R^2 \cos(2 t)} \,\mathrm{d}t$$ durch den leichter zu berechnenden $$\mathrm{e}^{-R^2(1 - 4/t \pi)}$$ zu ersetzen.
- Hat man eine Gleichung $$z = w$$ zwischen komplexen Zahlen $$z$$ und $$w$$ nachgewiesen, kann oft ein nützlicher nächster Schritt sein, die Real- und Imaginärteile von $$z$$ und $$w$$ zu vergleichen.
    In unserem Fall konnten wir beispielsweise die Gleichung $$\int_{0}^{\infty} \sin(x^2) \,\mathrm{d}x = \int_{0}^{\infty} \cos(x^2) \,\mathrm{d}x$$ sofort mittels eines Vergleiches der Imaginärteile in der Gleichung
    \\[
        \frac{1}{\sqrt{2}} \int_{0}^{\infty} ((\cos(t^2) + \sin(t^2)) + \mathrm{i} (\cos(t^2) - \sin(t)^2)) \,\mathrm{d}t = \frac{\sqrt{\pi}}{2}
    \\]
    folgern, und hieraus dann auch den Wert dieser Integrale, indem wir die Realteile verglichen.

### Aufgabe 3
- Abschätzungen für die Ableitungen holomorpher Funktionen können oft mithilfe der Cauchyschen Integralformel gefolgert werden.

## Fun Facts

In Aufgabe 3 wurde bemerkt, dass für beliebige holomorphe Funktionen $$f \colon D \to \mathbb{C}$$ auf der Einheitskreisscheibe $$D = \{z \in \mathbb{C} : |z| \le 1 \}$$ Gleichheit in der Abschätzung
\\[
    2 |f'(0)| \le \sup_{z, w \in D} |f(z) - f(w)| =: d
\\]
genau dann gilt, wenn $$f$$ affin-linear ist.

Die Implikation '$$\Leftarrow$$' ist natürlich eher weniger überraschend.
Die umgekehrte Implikation folgt hingegen beispielsweise aus dem [Schwarzschen Lemma](https://de.wikipedia.org/wiki/Schwarzsches_Lemma), welches wir später in der Vorlesung beweisen werden.
Konkreter gibt es einen Satz von Landau und Toeplitz, welcher letztendlich genau diese Aussage als Inhalt hat, und welcher im folgenden Artikel aus dem Lemma von Schwarz (sowie dem [Offenheits-](https://de.wikipedia.org/wiki/Offenheitsprinzip) und [Maximumprinzip](https://de.wikipedia.org/wiki/Maximumprinzip_(Mathematik)), die wir auch noch sehen werden) gefolgert wird:

- [Robert B. Burckel, Donald E. Marshall, & Pietro Poggi-Corradini. (2006). On a theorem of Landau and Toeplitz. arXiv preprint arXiv:0603579](https://arxiv.org/abs/math/0603579)
