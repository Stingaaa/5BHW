import pandas as pd
import matplotlib.pyplot as m
import scipy.stats as sp
import seaborn as s

df = pd.read_csv("INFI\Aufgabe5\data\ESS8e02.1_F1.csv", sep=",")
df["gndr"] = pd.cut(df["gndr"], [0,1,2,9], labels=["Male", "Female", "Unspecified"])
gender = df["gndr"]

#1.3 a
trustPolice = df["trstplc"]
trustPoliceGender = pd.crosstab(trustPolice, gender, normalize="index")
trustPoliceGender.plot.bar()
m.show()

chi, p, dof, expected = sp.chi2_contingency(trustPoliceGender)
print(chi, "\n", p, "\n", dof, "\n", expected)

s.heatmap(trustPoliceGender, annot=False, cmap="YlGnBu")
s.heatmap(trustPoliceGender, annot=trustPoliceGender, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(trustPoliceGender, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

#   Wie aus den Diagrammen ersichtlich, stimmt diese Aussage nicht
#   Tendenziell vertrauen Frauen der Polizei mehr als Männer
#   Und das obwohl auch ein größerer Anteil an Frauen keine Aussage dazu treffen wollten



#1.3 b
nCorrNucSun = df[["elgnuc", "elgsun"]]
dfNCorr = pd.crosstab(nCorrNucSun["elgnuc"], nCorrNucSun["elgsun"])

corr, p = sp.spearmanr(nCorrNucSun["elgnuc"], nCorrNucSun["elgsun"])
print(corr)

s.heatmap(dfNCorr, annot=False, cmap="YlGnBu")
s.heatmap(dfNCorr, annot=dfNCorr, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(dfNCorr, annot=False, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

print("Es gibt einen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr < 0 else "Es gibt einen positiven Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr > 0 else "Es gibt keinen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie")

#   Wie bereits durch die Berechnung des Zusammenhanges bekannt, hängen die zwei Energiearten negativ zusammen 
#   Das heißt, dass wenn es von einer dieser Energiequellen mehr Energie gibt, wird weniger von der anderen benötigt
#   Zusätztlich wird dieses Ergebnis durch das Diagramm bestätigt



#1.3 c
climateFeeling = df["ccgdbd"]
countries = df["cntry"].loc[df["cntry"].isin(["AT", "HU"])]
climateFeelingATHU = pd.crosstab(climateFeeling, countries, normalize="index")
climateFeelingATHU.plot.bar()
m.show()

chi, p, dof, expected = sp.chi2_contingency(climateFeelingATHU)
print(chi, "\n", p, "\n", dof, "\n", expected)

s.heatmap(climateFeelingATHU, annot=False, cmap="YlGnBu")
s.heatmap(climateFeelingATHU, annot=climateFeelingATHU, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(climateFeelingATHU, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

#   Wie aus den Diagrammen gut ersichtlich ist, wirkt der Klimawandel
#       schlechter auf Österreicher, als auf Ungarer
#   Diese Aussage wird durch die Berechung zusätzlich gefestigt



#1.3 d
baseIncome = df["basinc"]
baseIncGender = pd.crosstab(baseIncome, gender, normalize="index")
baseIncGender.plot.bar()
m.show()

stats, p = sp.mannwhitneyu(baseIncome.loc[df["gndr"] == "Male"], baseIncome.loc[df["gndr"] == "Female"])
print(stats, "\n", p,)

s.heatmap(baseIncGender, annot=False, cmap="YlGnBu")
s.heatmap(baseIncGender, annot=baseIncGender, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(baseIncGender, annot=False, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

#   Die Aussage, dass Frauen eher einem bedingungslosen Einkommmen zustimmen ist wahr
#   Dies wird besonders bei Betrachtung der Diagramme ersichtlich, da dort vor allem bei einer starken Bewertung (7-9)
#   der Anteil an Frauen bei weitem größer ist, als der Anteil an Männern



#1.3 e1
hydroEnergy = df["elghydr"]
countries = df["cntry"].loc[df["cntry"].isin(["AT", "DE"])]
hydroEnergyATDE = pd.crosstab(hydroEnergy, countries, normalize="index")
hydroEnergyATDE.plot.bar()
m.show()

chi, p, dof, expected = sp.chi2_contingency(hydroEnergyATDE)
print(chi, "\n", p, "\n", dof, "\n", expected)

s.heatmap(hydroEnergyATDE, annot=False, cmap="YlGnBu")
s.heatmap(hydroEnergyATDE, annot=hydroEnergyATDE, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(hydroEnergyATDE, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

#   Bei genauerer Untersuchung der Interessen der Bevölkerung zur Thematik der Wasserkraft, stellte sich heraus,
#   dass Deutsche bei weitem mehr daran interessiert sind einen Großteil ihrer Energie durch Wasskraft zu gewinnen
#   als Österreicher



#1.3 e2
attachedToCountry = df["atchctr"]
countries = df["cntry"].loc[df["cntry"].isin(["AT", "FR"])]
aTC_ATFR = pd.crosstab(attachedToCountry, countries, normalize="index")
aTC_ATFR.plot.bar()
m.show()

chi, p, dof, expected = sp.chi2_contingency(aTC_ATFR)
print(chi, "\n", p, "\n", dof, "\n", expected)

s.heatmap(aTC_ATFR, annot=False, cmap="YlGnBu")
s.heatmap(aTC_ATFR, annot=aTC_ATFR, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
s.heatmap(aTC_ATFR, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
m.show()

#   Sowohl Franzosen als auch Österreicher hängen stark an ihrem Land
#   Wie bereits aus dem Diagramm erischtlich, ist es eine sehr knappe Entscheidung
#   Österreicher hängen jedoch mit 51,35%, um etwa 2,7% mehr an ihrem Land als Franzosen  