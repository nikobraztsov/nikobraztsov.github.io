---
title: "Intergroup Connectivity and Religious Resilience: An Agent-Based Model of an Orthodox Religious Community"
date: 2026-06-24
description: Empty
tags:
  - texts
  - religious studies
---
Here is the text version of my talk on Seminar at the ML PSA Lab. 

 [Original announcement is here](https://anr.hse.ru/en/announcements/1166847041.html)


**Dear colleagues, thank you very much for the invitation. It is a great honor and an excellent opportunity to participate in this seminar. My name is Nikita Obraztsov.** 

I will briefly outline my background: my first degree is in law (I studied in Moscow at the Kutafin Moscow State Law University). After studying law, I made a sharp turn and moved into religious studies because I realized that this is what truly fascinates me. I completed my master's degree at St. Petersburg State University in 2020, where I focused on the "Brights" movement using qualitative methods—specifically, conducting in-depth interviews. At the time, we didn't have quantitative or computational methods in our program. Then, in 2025, I enrolled in the European University to study computational sociology, and right now, I have just completed my first year of the master's program.

I am working on several parallel tracks. One of my main interests is modern secularization, contemporary freethought, and atheism, as well as the history of freethought as a kind of secondary academic hobby (researching lesser-known freethinkers like John Toland, etc.). The main focus of my interest is secularization processes, secularization theory, and alternative theories—which of them work better, which ones can be tested, and so on.

### The Problem: Why Does the Secularization Mechanism Fail?

When I was thinking about how to structure my coursework and research, I wanted to use methods most relevant to the topic. That’s when the idea for this project was born. The inspiration came from looking at the Amish—these wonderful people in hats, with long beards and no mustaches. They live primarily in Pennsylvania and several other US states. As much as possible, they remain an isolated group. They live in closed communities, speak a specific dialect of Dutch/German, and are often seen as an absolute exception, an extremum in our modern secularizing world. 

Similar observations can be made regarding Old Believer communities in Russia or ultra-Orthodox Jewish communities in the US (for instance, in New York). If we look at the Amish, over the last 25 years, their population has doubled. And this isn't because they are attracting new converts—they simply don't do that. It happens entirely through high birth rates and successful religious transmission. The Amish even have a practice called *Rumspringa*, where adolescents can take an academic leave from the community, go out into the secular world, travel, and do whatever they want. Yet, even with this option to leave, they maintain their religiosity.

This raises a research question. At the macro-level, secularization theory posits that modernization increases existential security, which functionally decreases the need for religion (as noted by Norris and Inglehart). Yet, orthodox minorities persist. At the micro-level, religious decline happens through generational turnover—religion is incompletely transmitted from parents to children. Transmission is the key mechanism; deconversion is secondary. The problem with this "Big Theory" is that while the sequence of stages is described, the underlying generative causal mechanism remains elusive.

### Theoretical Basis: Complex Contagion and Plausibility Structures

Under what structural conditions does a religious minority survive without secularizing, even as the surrounding society secularizes? I searched for the answer by combining Agent-Based Modeling (ABM) and Social Network Analysis (SNA).

The theoretical basis relies on two key ideas:
1.  **Peter Berger's "Sacred Canopy" (1967) and Plausibility Structure:** Faith remains plausible only as long as it is supported by a consistent social environment. Contact with people of other faiths or secular individuals undermines this canopy.
2.  **Lawrence Iannaccone's "Why Strict Churches are Strong" (1994):** Strictness and exclusivity filter out free-riders and raise collective commitment.

Both of these propositions can be explained using SNA, specifically through the concept of **Complex Contagion** (Centola & Macy, 2007). Religious commitment is highly productive to view as a complex contagion. Adopting or maintaining it requires reinforcement from multiple sources; one contact is not enough. The structural consequence is that long "weak ties" (bridges) transfer simple contagions (like a virus or a rumor) but actually weaken complex contagions. A bridge stops complex contagion because the node on the other end only has one infected neighbor. Therefore, a segregated topology preserves religiosity and acts as a buffer against secularization under the pressure of existential security.

### Why ABM + SNA?

Why did I choose this specific methodological approach? In observational data, we face massive confounding. Segregated and integrated communities differ in income, urbanization, and education. A cross-sectional regression provides mixed estimates, and honestly, good observational data on real communities is basically nonexistent.

A virtual ABM experiment keeps everything constant and varies only one structural parameter: the probability of intergroup ties. This gives us pure identification of the topological effect.

There is a brilliant empirical study that justifies this approach: "Segregation in Religion Networks" based on Weibo data (Hu et al., 2018). They analyzed 6,875 believers across four traditions. Interestingly, they translated Muslims as "Islamists," which is a funny terminology issue, but the data is solid. They found that believers strongly prefer to form ties with their own faith, creating isolated communities. The assortativity index was $0.973$. Only $1.6\%$ of ties connected believers of different faiths.

### Experimental Design: The Stochastic Block Model (SBM)

I took $p_{cross}$ (the probability of a cross-group tie) as my key variable. I generated a new graph at each level of $p_{cross}$ (with 10 repetitions using different seeds) and ran the same dynamics on each graph. 

The network architecture is an exogenous Stochastic Block Model (SBM). I used SBM because I am trying to isolate an effect in a segregated community. We have two blocks:
*   **Secular block:** 400 nodes (the majority).
*   **Religious block:** 100 nodes (the minority).

To control for methodology, the intra-block density ($p_{in}$) is fixed identically at $0.15$ for both blocks. Equal internal density eliminates confounding; any difference in outcomes cannot be attributed to one block being denser than the other. The cross-probability ($p_{cross}$) ranges from $0.001$ (nearly complete segregation, like an Old Believer enclave) to $0.15$ (integration). 

### Structural Metrics and the 56x Phenomenon

When we look at the structural metrics across this gradient:
*   **Block Assortativity** drops from $0.974$ down to $\approx 0$.
*   **Ego-support** (the proportion of co-religionists among neighbors) drops from $0.98$ to $0.20$.
*   **Cross-group ties** increase from $0.3\%$ to $32\%$.

The most fascinating metric is the **betweenness of cross-group edges**. In the highly segregated regime ($p_{cross} = 0.001$), these rare bridges carry up to **56 times** more betweenness centrality than internal edges. Following Granovetter, weak ties spread information effectively, but for complex contagions, these exact same bridges serve as channels for assimilation pressure. As $p_{cross}$ rises to $0.10$, this structural advantage disappears entirely (ratio drops to $1.0x$).

### The Three Mechanisms of the Model

I embedded three mechanisms into the network dynamics:
1.  **Existential Security:** Modernization reduces religiosity. This is driven externally.
2.  **Social Support Buffer:** Complex contagion at work. Reinforcement by co-religionists lowers the effective rate of secularization. This is the mechanism theoretically linked to CREDs (Credibility-Enhancing Displays, Henrich 2009).
3.  **Bounded Confidence (Deffuant Model):** Opinion dynamics over edges with a trust threshold. It's a pairwise influence where the majority ultimately wins (assimilation).

### Results: Mechanism Ablation and Bistability

When I ran an ablation study to see which mechanism does what, the results were definitive. The social buffer is the *only* protective mechanism. If you remove the buffer, final religiosity ($R$) collapses from $0.45$ to $0.08$. The Deffuant mechanism acts purely as an assimilation force. Furthermore, the "Reference" scenario (no network mechanisms) remains flat at $0.40$ regardless of topology. This proves that the effect of segregation requires an active mechanism on the network to function.

The simulation also revealed a **Tipping Point**. The topology gradient creates a bistable tipping regime with wide error bands around $p_{cross} \approx 0.06$. At this threshold, social support drops below $0.40$, and the bistable transition collapses. This aligns with threshold models of collective behavior (Granovetter 1978, Schelling 1971).

### Beating the Confounding: The Generative Approach

This brings me to the central identification problem in network sociology: homophily vs. influence. In observational data, the similarity between connected nodes can be explained either by influence (they interact, so they become similar) or by homophily (they are similar, so they connect). They look exactly the same in cross-sectional data.

My generative approach completely bypasses this. The structure (SBM) and the influence mechanisms are defined separately. The correlation between a tie and similarity in $R$ does not confound the effect because the problem is eliminated by design. This fits perfectly within Analytical Sociology (Coleman's boat)—we specify mechanisms as response functions to neighbor states without requiring the agents to "read minds" (Generative Sufficiency).

### Limitations

Of course, this is a proof-of-concept, and I must be transparent about its limitations:
1.  **Static Network:** The graph does not co-evolve. I chose this for the pure identification of topology.
2.  **Exogenous Modernization:** Security grows from the outside without feedback from the network.
3.  **SBM Degrees:** Poisson tails instead of heavy tails. Real networks are more clustered.
4.  **Homogeneous Agents:** No heterogeneity in thresholds, which would otherwise smooth out the transition.
5.  **Scope Limit:** This model is strictly about the *preservation* of religion under secular pressure, not about the spread or origins of religion.

### A Closing Anecdote

To wrap up, I want to share a brief story about interdisciplinary friction. My first public presentation of this ABM was at a religious studies conference in April. I am a religious scholar, I go to these congresses. I was placed in the "Anthropology and Sociology of Religion" section. The colleague speaking right before me was presenting on *olfaction* in religion—how religion transmits signals through the smell of incense. 

Then I log on, load up my slides on Stochastic Block Models, Agent-Based Modeling, and differential equations. When I finished, there was just dead, grave silence. One colleague gently criticized it, saying it had nothing to do with reality, and I just accepted it. It perfectly illustrates the gap we need to bridge between computational methods and the traditional humanities.

Thank you very much for your attention. I am looking forward to your questions and advice, particularly regarding how to expand the structural metrics and endogenize the network.