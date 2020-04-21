# ENGG3130_Final_Project PsychoPy
### Modelling people's interactions with each other based on how they treat each other and their memories of previous interactions with each other and how that affects the system as a whole.

# How people interact with each other

We think about speech when we think about communication but there are many factors which affects our interaction with others.

1. Facial expressions.
2. Gestures.
3. Pointing / Using hands.
4. Writing.
5. Drawing.
6. Using equipment e.g. Text message or computer.
7. Touch.
8. Eye contact.

# How people treat each other and their memories of previous interactions

Memory supports and enables social interactions in a variety of ways. In order to engage in successful social interaction, people must be able to remember how they should interact with one another, whom they have interacted with previously, and what occurred during those interactions. Failure in any of these areas can lead to social rejection or violent conflict, which can be detrimental to a person's well being.

 # How this model is similar to Prisoner's Dilemma
 
 ## Prisoner's Dilemma: 
The prisoner's dilemma is a standard example of a game analyzed in game theory that shows why two completely rational individuals might not cooperate, even if it appears that it is in their best interests to do so.

Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. The prosecutors lack sufficient evidence to convict the pair on the principal charge, but they have enough to convict both on a lesser charge. Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent. The possible outcomes are:

- If A and B each betray the other, each of them serves two years in prison
- If A betrays B but B remains silent, A will be set free and B will serve three years in prison (and vice versa)
- If A and B both remain silent, both of them will serve only one year in prison (on the lesser charge).

This represent a variety of interactions where agents have to choose whether to "cooperate" with each other or "defect", and where the reward (or punishment) for each agent depends on what the other chooses. 

With this set of punishments, it is tempting to say that the players should cooperate, that is, that both should remain silent. But neither agent knows what the other will do, so each has to consider two possible outcomes. First, looking at it from A's point of view:

- If B remains silent, A is better off defecting; she would go free rather than serve 1 year.
- If B defects, A is still better off defecting; she would serve only 2 years rather than 3.

No matter what B does, A is better off defecting. And because the game is symmetric, this analysis is the same from B's point of view: no matter what A does, B is better off defecting.

In the simplest version of this game, we assume that A and B have no other considerations to take into account. They can't communicate with each other, so they can't negotiate, make promises, or threaten each other. And they consider only the immediate goal of minimizing their sentences; they don't take into account any other factors.

Under those assumptions, the rational choice for both agents is to defect. That might be a good thing, at least for purposes of criminal justice. But for the prisoners, it is frustrating because there is, apparently, nothing they can do to achieve the outcome they both want. And this model applies to other scenarios in real life where cooperation would be better for the greater good as well as for the players.

## PsychoPy:
Our model of PsycoPy is very much similar to the Prisoner's Dilemma described above. Here, instead of prisoners we have two real life players who could play this game called 'PsychoPy' against each other. The one who gets the highest score is the winner. The player could choose to be Generous, Selfish or TitForTat based on the situation. 



# Applications

PsychoPy helps us understand what governs the balance between cooperation and competition in business, in politics and in social settings. 

For instance consider three firms: Walmart and No Frills. They sell similar products and must decide on their pricing startegy. These firms could utilize their joint market power when all charge a high price. If one choose to set a low price, it will get a spike in sales and number of customers served. If both set low prices, both would make equal profits. On comparing this situation with PsychoPy model one could easily derive that, the low-price strategy is comparable to the prisoner’s confession, and the high-price akin to keeping silent. Call the former cheating, and the latter cooperation. Then cheating is each firm’s dominant strategy, but the result when both “cheat” is worse for each than that of both cooperating.

Arms races between superpowers or local rival nations offer another important example of the dilemma. Both countries are better off when they cooperate and avoid an arms race. Yet the dominant strategy for each is to arm itself heavily.

When each person in the game pursues his private interest, he does not promote the collective interest of the group. But often a group’s cooperation is not in the interests of society as a whole. Collusion to keep prices high, for example, is not in society’s interest because the cost to consumers from collusion is generally more than the increased profit of the firms. Therefore companies that pursue their own self-interest by cheating on collusive agreements often help the rest of society. Similarly, cooperation among prisoners under interrogation makes convictions more difficult for the police to obtain. One must understand the mechanism of cooperation before one can either promote or defeat it in the pursuit of larger policy interests.

Can “prisoners” extricate themselves from the dilemma and sustain cooperation when each has a powerful incentive to cheat? If so, how? The most common path to cooperation arises from repetitions of the game. In the Walmart-No Frills example, one month’s cheating gets the cheater extra profits. But a switch from mutual cooperation to mutual cheating loses some money. If one month’s cheating is followed by two months’ retaliation, therefore, the result is a wash for the cheater. Any stronger punishment of a cheater would be a clear deterrent. 

## The following five points elaborate on the idea:

1. The cheater’s reward comes at once, while the loss from punishment lies in the future. If players heavily discount future payoffs, then the loss may be insufficient to deter cheating. Thus, cooperation is harder to sustain among very impatient players (governments, for example).

2. Punishment will not work unless cheating can be detected and punished. Therefore, companies cooperate more when their actions are more easily detected (setting prices, for example) and less when actions are less easily detected (deciding on nonprice attributes of goods, such as repair warranties). Punishment is usually easier to arrange in smaller and closed groups. Thus, industries with few firms and less threat of new entry are more likely to be collusive.

3. Punishment can be made automatic by following strategies like “tit for tat.” This idea was popularized by University of Michigan political scientist Robert Axelrod. Here, you cheat if and only if your rival cheated in the previous round. But if rivals’ innocent actions can be misinterpreted as cheating, then tit for tat runs the risk of setting off successive rounds of unwarranted retaliation.

4. A fixed, finite number of repetitions is logically inadequate to yield cooperation. Both or all players know that cheating is the dominant strategy in the last play. Given this, the same goes for the second-last play, then the third-last, and so on. But in practice we see some cooperation in the early rounds of a fixed set of repetitions. The reason may be either that players do not know the number of rounds for sure, or that they can exploit the possibility of “irrational niceness” to their mutual advantage.

5. Cooperation can also arise if the group has a large leader, who personally stands to lose a lot from outright competition and therefore exercises restraint, even though he knows that other small players will cheat. Saudi Arabia’s role of “swing producer” in the opec cartel is an instance of this.

## Applications to Buisness

A classic example of the prisoner’s dilemma in the real world is encountered when two competitors are battling it out in the marketplace. Often, many sectors of the economy have two main rivals. In the U.S., for example, there is a fierce rivalry between Coca-Cola (KO) and PepsiCo (PEP) in soft drinks and Home Depot (HD) versus Lowe’s (LOW) in building supplies. This competition has given rise to numerous case studies in business schools. Other fierce rivalries include Starbucks (SBUX) versus Tim Horton’s (THI) in Canada and Apple (AAPL) versus Samsung in the global mobile phone sector.

Consider the case of Coca-Cola versus PepsiCo, and assume the former is thinking of cutting the price of its iconic soda. If it does so, Pepsi may have no choice but to follow suit for its cola to retain its market share. This may result in a significant drop in profits for both companies.

A price drop by either company may thus be construed as defecting since it breaks an implicit agreement to keep prices high and maximize profits. Thus, if Coca-Cola drops its price but Pepsi continues to keep prices high, the former is defecting, while the latter is cooperating (by sticking to the spirit of the implicit agreement). In this scenario, Coca-Cola may win market share and earn incremental profits by selling more colas.

### Payoff Matrix
Let’s assume that the incremental profits that accrue to Coca-Cola and Pepsi are as follows:

- If both keep prices high, profits for each company increase by $500 million (because of normal growth in demand).
- If one drops prices (i.e., defects) but the other does not (cooperates), profits increase by $750 million for the former because of greater market share and are unchanged for the latter.
- If both companies reduce prices, the increase in soft drink consumption offsets the lower price, and profits for each company increase by $250 million.

The payoff matrix looks like this (the numbers represent incremental dollar profits in hundreds of millions):

Coca-Cola vs. PepsiCo 

                               PepsiCo 
                               
Payoff Matrix


                                                 Cooperate           Defect


Coca-Cola                      

                               Cooperate         500, 500            0, 750


                               Defect            750, 0              250, 250
                               
                               
Other oft-cited prisoner’s dilemma examples are in areas such as new product or technology development or advertising and marketing expenditures by companies.

For example, if two firms have an implicit agreement to leave advertising budgets unchanged in a given year, their net income may stay at relatively high levels. But if one defects and raises its advertising budget, it may earn greater profits at the expense of the other company, as higher sales offset the increased advertising expenses. However, if both companies boost their advertising budgets, the increased advertising efforts may offset each other and prove ineffective, resulting in lower profits—due to the higher advertising expenses—than would have been the case if the ad budgets were left unchanged.

## Applications to Economy

The U.S. debt deadlock between the Democrats and Republicans that springs up from time to time is a classic example of a prisoner’s dilemma.

Let’s say the utility or benefit of resolving the U.S. debt issue would be electoral gains for the parties in the next election. Cooperation in this instance refers to the willingness of both parties to work to maintain the status quo with regard to the spiraling U.S. budget deficit. Defecting implies backing away from this implicit agreement and taking the steps required to bring the deficit under control.

If both parties cooperate and keep the economy running smoothly, some electoral gains are assured. But if Party A tries to resolve the debt issue in a proactive manner, while Party B does not cooperate, this recalcitrance may cost B votes in the next election, which may go to A.

However, if both parties back away from cooperation and play hardball in an attempt to resolve the debt issue, the consequent economic turmoil (sliding markets, a possible credit downgrade, and government shutdown) may result in lower electoral gains for both parties.

## How Can We Use It?

The PsychoPy model can be used to aid decision-making in a number of areas in one’s personal life, such as buying a car, salary negotiations and so on.

For example, assume you are in the market for a new car and you walk into a car dealership. The utility or payoff, in this case, is a non-numerical attribute (i.e., satisfaction with the deal). You want to get the best possible deal in terms of price, car features, etc., while the car salesman wants to get the highest possible price to maximize his commission.

Cooperation in this context means no haggling; you walk in, pay the sticker price (much to the salesman’s delight), and leave with a new car. On the other hand, defecting means bargaining. You want a lower price, while the salesman wants a higher price. Assigning numerical values to the levels of satisfaction, where 10 means fully satisfied with the deal and 0 implies no satisfaction, the payoff matrix is as shown below:

Car Buyer vs. Salesman 

                               Salesman 
                               
Payoff Matrix


                                                 Cooperate           Defect


Buyer                      

                               Cooperate         (a) 7, 7            (c) 0, 10


                               Defect            (b) 10, 0           (d) 3, 3

What does this matrix tell us? If you drive a hard bargain and get a substantial reduction in the car price, you are likely to be fully satisfied with the deal, but the salesman is likely to be unsatisfied because of the loss of commission (as can be seen in cell b).

Conversely, if the salesman sticks to his guns and does not budge on price, you are likely to be unsatisfied with the deal while the salesman would be fully satisfied (cell c).

Your satisfaction level may be less if you simply walked in and paid full sticker price (cell a). The salesman in this situation is also likely to be less than fully satisfied, since your willingness to pay full price may leave him wondering if he could have “steered” you to a more expensive model, or added some more bells and whistles to gain more commission.

Cell (d) shows a much lower degree of satisfaction for both buyer and seller, since prolonged haggling may have eventually led to a reluctant compromise on the price paid for the car.

Likewise, with salary negotiations, you may be ill-advised to take the first offer that a potential employer makes to you (assuming you know that you’re worth more).

Cooperating by taking the first offer may seem like an easy solution in a difficult job market, but it may result in you leaving some money on the table. Defecting (i.e., negotiating) for a higher salary may indeed fetch you a fatter pay package. Conversely, if the employer is not willing to pay more, you may be dissatisfied with the final offer.

Hopefully, the salary negotiations do not turn acrimonious, since that may result in a lower level of satisfaction for you and the employer. The buyer-salesman payoff matrix shown earlier can be easily extended to show the satisfaction level for the job seeker versus the employer.

Applications - https://www.econlib.org/library/Enc/PrisonersDilemma.html

Business Applications - https://www.investopedia.com/articles/investing/110513/utilizing-prisoners-dilemma-business-and-economy.asp#applications-to-business
