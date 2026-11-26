---
title: "Research"
description: "Research on social networks, social influence, agent-based modelling and the persistence of social practices."
translationKey: "research"
draft: false
---

My research focuses on social influence in networks. I am particularly interested in how patterns of interaction among individuals shape the persistence of beliefs and practices within communities, and what information about social ties we need to predict these outcomes.

## Current project: Network characteristics and the persistence of social practices

*Master's research, European University at St. Petersburg, 2025–2027.*

Why do some communities maintain distinctive practices over time despite frequent contact with people who do not share them? Religious minorities were the starting point for this project. The same question can be posed in the study of other cultural practices, where individuals interact both within and outside their communities.

A common way to describe an individual's social environment is the proportion of ties to members of their own group. Two people with the same proportion may, however, have very different patterns of interaction. They may meet their contacts with different frequency, experience different degrees of social influence, or interact in settings where a particular practice is more or less salient.

I investigate whether these additional characteristics of ties improve our ability to predict practice persistence. My research compares three representations of an individual's network:

1. **Network composition:** the proportion of within-group ties.
2. **Weighted exposure:** information about the frequency and strength of interactions.
3. **Social context:** information about the settings in which interactions take place and how exposure is distributed across them.

### Methods

I use agent-based modelling to vary network characteristics and mechanisms of social influence in controlled simulation experiments. The model represents a practice on a continuous scale and includes individual commitment, allowing repeated interactions to affect both practice and commitment under specified assumptions. The implementation is in Python, using Mesa, NetworkX and NumPy.

The analysis compares predictive models using progressively richer network information. I am interested in whether additional information improves prediction on held-out simulation runs and under which model conditions it matters. The project draws on research in opinion dynamics, homophily, complex contagion and analytical sociology.

### Preliminary findings and limitations

In an earlier, unweighted version of the model, I found that changes in cross-group connectivity could produce substantial differences in the persistence of religious commitment. I presented this proof of concept at EUSN 2026. My current work extends this approach to investigate weighted and context-dependent ties.

These are simulation-based findings. The model is a stylised representation of social interaction; it has not yet been validated against observations of particular communities. The current research therefore examines the consequences of specified mechanisms and the predictive value of network information within the model. Empirical validation remains a separate task.

## Selected research presentations

**European Conference on Social Networks (EUSN 2026)** — Norrköping, Sweden, August 2026 (remote presentation). Earlier model of network structure and religious resilience. [Slides (PDF)](/docs/EUSN.pdf) · [Conference programme (PDF)](/docs/EUSN_Program.pdf)

**ML PSA Lab seminar** — June 2026. Presentation on intergroup connectivity and religious resilience.

**AI & Methods in Computational Communication (AIM-CC) Summer School** — Nazarbayev University, Astana, August 2026. Poster presentation on my agent-based model and a closing talk.

[All talks and presentations →](/talks/)

## Sociology of religion

My earlier work addressed secularisation, non-belief and religious identity, including the relationship between religious belonging and belief in the Russian context. This background informs my interest in the measurement of social practices and the mechanisms underlying cultural persistence.

[Publications →](/publications/) · [Google Scholar](https://scholar.google.com/citations?user=tYxoJv8AAAAJ)

## Research interests and collaboration

I am interested in doctoral research on social networks, social influence, computational models of collective behaviour, and the relationship between simulation and empirical network research. I plan to complete my current MA in 2027.

[Contact →](/contact/) · [Academic CV (PDF)](/cv.pdf)
