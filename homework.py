import pandas as pd
import csv
import statistics
import plotly.graph_objects as go
df=pd.read_csv("StudentsPerformance.csv")
scorelist=df["scoreR"].to_list()

scoremean=statistics.mean(scorelist)

scoremedian=statistics.median(scorelist)

scoremode=statistics.mode(scorelist)

scoresd=statistics.stdev(scorelist)

print("mean,median and mode of score is {},{} and {}".format(scoremean,scoremedian,scoremode))
print("sd of score is {}".format(scoresd))

scorefirstsdstart,scorefirstsdend=scoremean-scoresd,scoremean+scoresd
scoresecondsdstart,scoresecondsdend=scoremean-(2*scoresd),scoremean+(2*scoresd)
scorethirdsdstart,scorethirdsdend=scoremean-(3*scoresd),scoremean+(3*scoresd)

scorelistofdatawithinfirstsd=[result for result in scorelist if result>scorefirstsdstart and result<scorefirstsdend]
scorelistofdatawithinsecondsd=[result for result in scorelist if result>scoresecondsdstart and result<scoresecondsdend]
scorelistofdatawithinthirdsd=[result for result in scorelist if result>scorethirdsdstart and result<scorethirdsdend]


print("{}% of data for score lies within 1sd ".format(len(scorelistofdatawithinfirstsd)*100.0/len(scorelist)))
print("{}% of data for score lies within 2sd ".format(len(scorelistofdatawithinsecondsd)*100.0/len(scorelist)))
print("{}% of data for score lies within 3sd ".format(len(scorelistofdatawithinthirdsd)*100.0/len(scorelist)))

