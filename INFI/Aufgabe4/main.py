import numpy as np
import pandas as pa
import statsmodels.api as sm
from matplotlib import pyplot as p

data = pa.read_excel("INFI\Aufgabe4\data/bev_meld.xlsx")

#Task 2.1
growth = data.values[:,3:].sum(axis=0)
p.title("Gesamtbevölkerung pro Jahr")
p.plot(data.columns[3:], growth)
p.xlabel("Jahr")
p.ylabel("Bevölkerungszahl")
p.savefig("INFI/Aufgabe4/pics/Task_2-1")
p.show()


#Task 2.2
# Task 5
# Der hier dargestellt Boxplot zeigt einen guten Mittelwert zwischen der Differenz
# aller Punkte (in Task 4 ist dies am besten zu sehen, da zuerst die genauen Werte dargestellt wurden
# und dann die Werte der Regressionsgerade dargestellt wurden)
def getModel(y, v):
    df_reg=pa.DataFrame({"years": y, "bev":v})
    model =  sm.OLS.from_formula('bev ~ years', df_reg).fit()
    return model
    
def predictGrowth(y, v, year):
    model = getModel(y, v)
    print(model.summary())
    # avgGrowthPerYear = []  
    # for i in range(len(v)-1):
    #     avgGrowthPerYear.append(v[i+1]-v[i])
    # avgGrowth = sum(avgGrowthPerYear)/len(avgGrowthPerYear)   
    # return str((year - y[0]) * avgGrowth + v[0])
    return str(model.params[1]*year + model.params[0])
    
print("Prediction 2030: " + predictGrowth(pa.to_numeric(data.columns[3:]), pa.to_numeric(growth), 2030))
#print("Predictions 2030 - 2100: " + str(getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(growth)).predict(pa.DataFrame({"years":np.arange(2030,2100)}))))
#print("Predictions from 2030 - 2100:")
#for i in range(2030,2101):
#    print("Prediction " + str(i) + ": " + predictGrowth(pa.to_numeric(data.columns[3:]), pa.to_numeric(growth), i))
p.plot(np.arange(2030,2100), getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(growth)).predict(pa.DataFrame({"years":np.arange(2030,2100)})))
p.title("Prediction 2030 - 2100")
p.savefig("INFI/Aufgabe4/pics/Task_2-2")
p.show()


#Task 3
# Task 5
# Der hier dargestellt Boxplot zeigt einen guten Mittelwert zwischen der Differenz
# aller Punkte (in Task 4 ist dies am besten zu sehen, da zuerst die genauen Werte dargestellt wurden
# und dann die Werte der Regressionsgerade dargestellt wurden)
print("\nPrediction Wörgl 2030: " + predictGrowth(pa.to_numeric(data.columns[3:]), pa.to_numeric(data.values[139,3:]), 2030))
#print("Predictions Wörgl 2030 - 2100: " + str(getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(data.values[139,3:])).predict(pa.DataFrame({"years":np.arange(2030,2100)}))))
p.plot(np.arange(2030,2100), getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(data.values[139,3:])).predict(pa.DataFrame({"years":np.arange(2030,2100)})))
p.title("Prediction Wörgl 2030 - 2100")
p.savefig("INFI/Aufgabe4/pics/Task_3")
p.show()


#Task 4
fig, axes = p.subplots(2,1)

t1 = data.values[1:24, 3:].sum(axis=0)
d1 = pa.DataFrame({"Bevölkerungszahl":t1})
t2 = data.values[110:139, 3:].sum(axis=0)
d2 = pa.DataFrame({"Bevölkerungszahl":t2})

d1.plot(ax=axes[0], title="Gemeine IM")
d2.plot(ax=axes[1], title="Gemeinde KU")

# Task 5
# Wie hier zusehen ist, bilden die Regressionsgeraden eine recht präzise Gerade,
# welche ein gutes Mittel der Punkte der Ursprungswerte wiederspiegelt

fig.tight_layout()
p.savefig("INFI/Aufgabe4/pics/Task_4-1")
p.show()

p.plot(data.columns[3:], d1, label="IM")
p.plot(data.columns[3:], d2, label="KU")
p.legend()
p.savefig("INFI/Aufgabe4/pics/Task_4-2")
p.show()

p.plot(data.columns[3:], getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(data.values[1:24,3:].sum(axis=0))).predict(pa.DataFrame({"years":np.arange(1993,2022)})), label="IM")
p.plot(data.columns[3:], getModel(pa.to_numeric(data.columns[3:]), pa.to_numeric(data.values[110:139,3:].sum(axis=0))).predict(pa.DataFrame({"years":np.arange(1993,2022)})), label="KU")
p.legend()
p.savefig("INFI/Aufgabe4/pics/Task_4-3")
p.show()