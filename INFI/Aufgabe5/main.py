import pandas as pd
import matplotlib.pyplot as m
import scipy.stats as sp
import seaborn as s

df = pd.read_csv("INFI\Aufgabe5\data\ESS8e02.1_F1.csv", sep=",")
df["gndr"] = pd.cut(df["gndr"], [0,1,2,9], labels=["Male", "Female", "Error 404"])
gender = df["gndr"]

# #1.3 a
# trustPolice = df["trstplc"]
# trustPoliceGender = pd.crosstab(trustPolice, gender, normalize="index")
# trustPoliceGender.plot.bar()
# m.show()

# chi, p, dof, expected = sp.chi2_contingency(trustPoliceGender)
# print(chi, "\n", p, "\n", dof, "\n", expected)

# s.heatmap(trustPoliceGender, annot=False, cmap="YlGnBu")
# s.heatmap(trustPoliceGender, annot=trustPoliceGender, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
# s.heatmap(trustPoliceGender, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
# m.show()

# #   Wie aus den Diagrammen ersichtlich, stimmt diese Aussage nicht
# #   Tendenziell vertrauen Frauen der Polizei mehr als Männer
# #   Und das obwohl auch ein größerer Anteil an Frauen keine Aussage dazu treffen wollten



# #1.3 b
# nCorrNucSun = df[["elgnuc", "elgsun"]]
# dfNCorr = pd.crosstab(nCorrNucSun["elgnuc"], nCorrNucSun["elgsun"])

# corr, p = sp.spearmanr(nCorrNucSun["elgnuc"], nCorrNucSun["elgsun"])
# print(corr)

# s.heatmap(dfNCorr, annot=False, cmap="YlGnBu")
# s.heatmap(dfNCorr, annot=dfNCorr, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
# s.heatmap(dfNCorr, annot=False, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
# m.show()

# print("Es gibt einen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr < 0 else "Es gibt einen positiven Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr > 0 else "Es gibt keinen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie")

# #   Wie bereits durch die Berechnung des Zusammenhanges bekannt, hängen die zwei Energiearten negativ zusammen 
# #   Das heißt, dass wenn es von einer dieser Energiequellen mehr Energie gibt, wird weniger von der anderen benötigt
# #   Zusätztlich wird dieses Ergebnis durch das Diagramm bestätigt



#1.3 c
climateFeeling = df["ccgdbd"]
countries = df["cntry"].loc[df["cntry"].isin(["AT", "HU"])]
climateFeelingATHU = pd.crosstab(climateFeeling, countries, normalize="index")
climateFeelingATHU.plot.bar()
m.show()