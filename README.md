# Baseball Performance Metric Analysis
This research isolates traditional player performance metrics from variables beyond their control, such as the ballpark in which they compete, as well as the strength of their opponent on any given day. Ballpark factor is empirically defined by a linear least squares regression analysis, and opponent offensive strength is derived from a combination of recent and full season performance metrics.  Predictive modeling is performed using the newly defined metrics as features to provide evidence of their value in assigning small modifications to starting pitchers’ ERAs.

# Introduction
Baseball performance has been long been measured to assess appropriate salaries and ultimately construct a competitive team; however, the methods for analyzing performance have changed dramatically over the years. How to best isolate a player’s performance from environmental factors beyond the player’s control. This analysis shares the same problem statement; In particular, this aims to quantify how ballpark factors and recent opponent performance can be used to augment an instantaneous measure of a baseball pitcher’s performance.  Finally, these new measures of a player’s performance will be used as features for modeling a more accurate assessment of player performance.

# Data
The data used for this analysis was primarily collected from two sources including: Retrosheet, a non-profit website with historical MLB box scores, and the Lahman Baseball Database, which is a relational database containing pitching, hitting, and fielding statistics for Major League Baseball from 1871 through 2023
# Methods
A least squares regression analysis is performed to define the park factor ratings for all MLB parks. A 'Game Difficulty' assessment is derived for each game measuring the difficulty of playing that opponent at that time, given the opponents’ recent success in scoring runs.

# Conclusions
This analysis provided evidence of a strength of opponent score influencing the outcome of a game, as shown in figure 3 of section 4.3 of the attached report. In addition, the MLP defined in section 4.4 provided evidence that changes in ballpark factors and opponent success can be used to predict a change in ERA. 

# Future Work
There may be other model architectures or modifications this MLP that may produce better results. In addition, expanding the dataset and experimenting with further pre-processing may yield better results. Runs scored was chosen to define both park factor and opponent success; however, it is possible to use other traditional metrics or some combination of many metrics. This analysis assumed the running average opponent success was twice as important as a team’s total season success when computing a ‘game difficulty’ score, but these weights can be learned as opposed to be predefined by the author. 