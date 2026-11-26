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

My work on the unweighted model also includes parameter sweeps, ablation experiments, mean-field and fixed-network baselines, and sensitivity analysis. I have examined minority shares ranging from 2% to 50% in block and growing networks.

[Model code on GitHub](https://github.com/nikobraztsov/abm-secularization)

### Preliminary findings and limitations

In an earlier, unweighted version of the model, I found that changes in cross-group connectivity could produce substantial differences in the persistence of religious commitment. I presented this proof of concept at EUSN 2026. My current work extends this approach to investigate weighted and context-dependent ties.

In subsequent experiments, much of the apparent effect of group size depended on how the probability of cross-group ties was parameterised. The local proportion of in-group neighbours was a useful predictor of persistence, with a threshold around 0.85 in the specifications examined. This value is specific to the simulation conditions and should not be interpreted as a universal threshold for real communities.

These are simulation-based findings. The model is a stylised representation of social interaction; it has not yet been validated against observations of particular communities. The current research therefore examines the consequences of specified mechanisms and the predictive value of network information within the model. Empirical validation remains a separate task.

### Earlier model: results presented at EUSN 2026

The figures below come from my August 2026 presentation. This earlier model used 500 agents, a stochastic block model and unweighted ties. I varied the probability of cross-group ties while keeping the within-group tie probability fixed.

![Mean religiosity versus cross-group tie probability in the earlier EUSN model](/images/research/eusn-2026-connectivity.png)

*Figure 1. Mean religiosity in the religious group falls as cross-group connectivity increases in this specification. Source: EUSN 2026 slides, p. 13. The values are simulation outputs, not estimates of real-world religiosity.*

![Distribution of final mean religiosity in 100 simulations at cross-group tie probability 0.06](/images/research/eusn-2026-outcomes.png)

*Figure 2. At a cross-group tie probability of 0.06, 100 runs on a fixed network produced different outcomes: 80 in the higher-retention group and 20 in the assimilation group as classified in the presentation. Source: EUSN 2026 slides, p. 14. These proportions are specific to the earlier model and its classification.*

[Full presentation (PDF)](/docs/EUSN.pdf)

## Measuring religiosity in research literature

In a separate project, I examine how religiosity is conceptualised across research fields. In October 2026 I presented an exploratory bibliometric analysis of approximately 30,000 articles after preprocessing OpenAlex records. Clustering abstracts suggests substantial variation across research domains; whether these clusters correspond to distinct operationalisation strategies still requires manual coding of articles.

[Research presentation and description](/news/news-rro-congress-en/) · [Slides (Russian, PDF)](/docs/religiosity-slides.pdf)

## Reanalysis of a published religiosity measure

*Course project in survey methodology, European University at St. Petersburg, March–May 2026.*

I reanalysed the open replication data of Rainero, Stolz and Luijkx (2026) on religiosity and researchers’ judgements of secularization. I examined the dimensionality and reliability of the religiosity scale, separated belief and practice into subscales, and estimated logistic regression models with author-clustered standard errors and average marginal effects. The two subscales were strongly correlated (r = 0.83); a direct test of coefficient equality did not distinguish their effects in this analysis.

[Replication and analysis code on GitHub](https://github.com/nikobraztsov/faith-factor-reanalysis)

## Selected research presentations

**European Conference on Social Networks (EUSN 2026)** — Norrköping, Sweden, 11–15 August 2026 (remote presentation). Earlier model of network structure and religious resilience. [Slides (PDF)](/docs/EUSN.pdf) · [Conference programme (PDF)](/docs/EUSN_Program.pdf)

**ML PSA Lab seminar** — June 2026. Presentation on intergroup connectivity and religious resilience. [Transcript](/texts/seminar-en/)

**AI & Methods in Computational Communication (AIM-CC) Summer School** — Nazarbayev University, Astana, August 2026. Poster presentation on my agent-based model and a closing talk. [Event report](/news/news-aimcc-en/)

[All talks and presentations →](/talks/)

## Sociology of religion

My earlier work addressed secularisation, non-belief and religious identity, including the relationship between religious belonging and belief in the Russian context. This background informs my interest in the measurement of social practices and the mechanisms underlying cultural persistence.

[Publications →](/publications/) · [Google Scholar](https://scholar.google.com/citations?user=tYxoJv8AAAAJ)

## Research interests and collaboration

I am interested in doctoral research on social networks, social influence, computational models of collective behaviour, and the relationship between simulation and empirical network research. I plan to complete my current MA in 2027.

[Contact →](/contact/) · [Academic CV (PDF)](/cv.pdf) · [ORCID](https://orcid.org/0009-0001-1377-6188)
