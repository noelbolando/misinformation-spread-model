# A Model to Explore the Spread of Misinformation #

Everyone who has any sort of presence in our modern soceity has encountered misinforamtion and/or disinformation on some sort of scale. Although these terms are more prevelant in our digitial world, misinformation and disinformation have existed since the birth of spoken language. However, the rise of online social media platforms have resulted in a more salient landscape for the birth, infection, and dissemenation of misinformation and disinformation and chances are, you and I interact with these information types on the DAILY. Sometimes without even realizing it.

This model explores the spread of misinformation across a population based on a SEHIR agent-based model. Before I get into the model details, a quick word:

I want to be very clear about how I'm communicating what this model DOES and DOES NOT do. So as not to incur any sort of misinformation about what I'm trying to explore here. This model explores the spread of misinformation, not disinforamtion. Although these terms are often used interchangeably and they have similiar meanings, they have very different conontations.

"Misinformation is false or misleading conent shared without harmful intent. The effects can still be harmful but the intent is not to harm [1]."

Whereas...

"Disinforamtion is false or misleading content spread to deceive or secure economic or political gain, which may cause public harm [1]."  

This isn't to say that I'm not interested in exploring the spread of disinformation - I certainly am - but for now, I'll be building a model that investigates the spread of misinformation. I'll leave some interesting references below for those interested in learning more about these interesting phenomena and the impact of interacting with information types today.

ENJOY! =D

## Project Details ##
As you'll see, there are three files in this repo:
1. agents.py: this file defines the behavior of all agents.
2. app.py: using Solara, this files defines an interactive workspace for people to view and play with the model.
3. model.py: this file defines the model and simulation enviornment for agent interactions.

## The Nerd Corner ##
SEHIR models explore the interaction of agents within 5 different agent states:
1. S - susceptible agents, capable of spreading misinformation.
2. E - agents exposed to misinformation.
3. H - hibernating agents; exposed to misinformation but not interacting with or spreading it, at first.
4. I - infected agents; exposed to misinformation and spreading it.
5. R - resistant/recovered/removed agents; these agents are either (A) not exposed to misinformation (perhaps they're not active on the socials), for the sake of this study, these agents would be considered "resistant" or (B) exposed to misinformation but "recovered" in the sense that they were exposed to it but never infected.

I created a little diagram below to understand the relationship between these agents. 

![SEHIR](https://github.com/user-attachments/assets/56794b54-d640-417d-a736-3b3295be1cdf)
SEHIR Diagram for this Misinformation Model

Notice the continuous lines between the different agents; this explains how agents change states/interact with other agents in the model. For example, a susceptible (S) agent can become an exposed (E) when exposed to misinformation. The equation that governs this behavior is given above the arrow. 

The dashed lines output from each agent signal a deactivation of that agent from the model.


## Further Reading ##

[1](https://arxiv.org/pdf/2406.09343). This is an excellent literature review on the frameworks, modeling, and simulations of misinformation and disinformation networks. It was published June 2024 so it's super releveant for understanding the landscape of this area of study today.

[Mathematical Model for the Prevalence of Disinformation](https://journals.indexcopernicus.com/api/file/viewByFileId/1472215). This paper was really informative for me while building this model. Honestly, I couldn't find much stuff online (academically or otherwise) on misinformation and disinformation models. This goes into the theory of SEHIR models in depth and goes through some pretty rigorous proofs for the math side of things.

[Disinformation as an Emergent Phenomenon](https://repository.isls.org/bitstream/1/10209/1/ICLS2023_2155-2156.pdf). This is a really cool read on how people respond and/or change their perspective when exposed to models that demonstrate the spread of disinformation. It really goes to show ya that a cute little model can go a long way in helping people understand their world a little bit better.
