---
title: "Nikita Obraztsov Presented at the Russian Religious Studies Society Congress"
date: 2026-10-15
tags: ["news", "research", "computational religious studies"]
---
On 15 October 2026, Nikita Obraztsov presented at the IX Congress of the Russian Religious Studies Society. The talk, titled "The Operationalisation of Religiosity as an Unresolved Problem in Contemporary Religious Studies: A Computational Perspective," reported the first stage of an ongoing research project.

![Presenting at the IX Congress of the Russian Religious Studies Society](/images/nikita-presentation.jpg)

---

## The Problem

"How do you define religiosity?" is a genuinely painful question for any scholar of religion. There is no agreed answer, and no agreement seems imminent. Across empirical social science, religiosity is routinely operationalised by default — included as a variable in a checklist of factors — often inconsistently or without any explicit definition. This is a serious methodological problem.

The theoretical point of departure is a paper by M.Yu. Smirnov (published in the *Vestnik RKhG*), which argued that researchers should abandon attempts to operationalise religiosity in a principled way and instead study religion as it "manifests." Smirnov held that no single characterisation of religiosity can be exhaustive, and proposed using the concept as a loose framework — a "scaffold" — to be filled with context-specific content. He acknowledged, however, that in his own empirical work he cannot avoid operationalising it.

**Research hypothesis:** the conceptualisation and operationalisation of religiosity differ so substantially across research contexts that they effectively constitute distinct semantic spaces.

## Data and Method

**Source:** OpenAlex — the most accessible open-access bibliometric database, with a free API.

**Search term:** *religiosity* (not *religiousness* — that corpus runs to half a million records and skews away from religious studies).

**Corpus:** ~35,000 articles, 2010–2026 → ~30,000 after preprocessing.

**Preprocessing:**
- deduplication by DOI
- filtering of non-English abstracts (using word-level language detection rather than relying on OpenAlex's language field, which is sometimes inaccurate)
- removal of articles with no abstract or an abstract below a minimum length threshold

**Clustering:** k-means; optimal number of clusters determined by the elbow method — 8 clusters, grouped into 4 broad domains.

## Results

Eight clusters, grouped into four domains:

1. **Psychological and medical surveys** — the largest group; clinical studies, religiosity questionnaires in mental and physical health research.
2. **Spirituality and coping** — substantial overlap with well-being, meaning-of-life surveys.
3. **Political and social attitudes** — cross-national comparisons, values research (EVS/WVS-type).
4. **Islamic finance and halal consumption** — an unexpected cluster, predominantly Indonesian publications; reflects growth in that research area rather than in religious studies proper; requires separate treatment.

Co-occurrence network: *religiosity* clusters most densely with *spirituality*, *well-being*, *intrinsic religiosity*, *measurement*, and *role*. Co-occurrence with historical and humanities scholarship is substantially weaker.

The corpus grows at roughly 1% per year; the share of psychological and medical work is declining, while the Islamic finance cluster is growing. A robustness check (re-clustering on random subsamples) confirmed the reproducibility of the regions.

## Preliminary Conclusions

The field is highly heterogeneous. It would be unreasonable to expect a health psychologist, a values sociologist, and an Islamic finance researcher to mean the same thing by "religiosity." This confirms Smirnov's argument — now on data rather than intuition alone.

## Next Steps

- Manual coding of operationalisation strategies in individual articles
- Citation network analysis within clusters
- Possible narrowing of the corpus to Q1–Q2 religious studies and adjacent journals

Three possible outcomes: (1) operationalisation differs fundamentally across clusters; (2) measurement approaches are surprisingly similar regardless of discipline; (3) no significant correlation is found between cluster membership and operationalisation strategy.

## Limitations

- Only the term *religiosity*; synonyms (*religiousness*, *faith*, *piety*) excluded
- OpenAlex vs. Web of Science: the former is more open but includes a broader journal pool
- Clustering is algorithmic; manual verification of each cluster remains to be done
- Single researcher; a full continuation of the project requires a team


[You can find the slides in Russian here →](/docs/religiosity-slides.pdf)
