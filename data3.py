import pandas as pd
import numpy as np
import yfinance as yf 
import matplotlib.pyplot as plt
yahoodata=yf.download(["AMXL.MX","PINFRA.MX","LABB.MX","CUERVO.MX","BOLSAA.MX","LIVEPOLC-1.MX","MEGACPO.MX","BBAJIOO.MX","KOFUBL.MX","ALSEA.MX","FEMSAUBD.MX","GCARSOA1.MX","ALFAA.MX","ORBIA.MX","GRUMAB.MX","PE&OLES.MX","GMEXICOB.MX","GFNORTEO.MX","WALMEX.MX","GFINBURO.MX","CEMEXCPO.MX","TLEVISACPO.MX","GAPB.MX","ELEKTRA.MX","ASURB.MX","KIMBERA.MX","BIMBOA.MX","OMAB.MX","AC.MX"],start="2020-01-01",end="2022-07-29",interval="1mo")
data=pd.DataFrame(yahoodata).drop(["Volume","Low","High","Close","Open"],axis=1).dropna()
data
plt.plot(data)
data_plot=plt.show()
referencia=pd.DataFrame(data.iloc[0,:]).reset_index()
referencia
referencia=np.array(referencia.iloc[:,2])
referencia
plot_cambios=data.pct_change()
plt.plot(plot_cambios)
cambios_plot=plt.show()
cambios_porcentuales=pd.DataFrame(data.pct_change().fillna(0).transpose().reset_index())
cambios_porcentuales.head()
rend_1=np.array(cambios_porcentuales.iloc[:,2])
rend_1
rend_2=np.array(cambios_porcentuales.iloc[:,3])
rend_2
rend_3=np.array(cambios_porcentuales.iloc[:,4])
rend_4=np.array(cambios_porcentuales.iloc[:,5])
rend_5=np.array(cambios_porcentuales.iloc[:,6])
rend_6=np.array(cambios_porcentuales.iloc[:,7])
rend_7=np.array(cambios_porcentuales.iloc[:,8])
rend_8=np.array(cambios_porcentuales.iloc[:,9])
rend_9=np.array(cambios_porcentuales.iloc[:,10])
rend_10=np.array(cambios_porcentuales.iloc[:,11])
rend_11=np.array(cambios_porcentuales.iloc[:,12])
rend_12=np.array(cambios_porcentuales.iloc[:,13])
rend_13=np.array(cambios_porcentuales.iloc[:,14])
rend_14=np.array(cambios_porcentuales.iloc[:,15])
rend_15=np.array(cambios_porcentuales.iloc[:,16])
rend_16=np.array(cambios_porcentuales.iloc[:,17])
rend_17=np.array(cambios_porcentuales.iloc[:,18])
rend_18=np.array(cambios_porcentuales.iloc[:,19])
rend_19=np.array(cambios_porcentuales.iloc[:,20])
rend_20=np.array(cambios_porcentuales.iloc[:,21])
rend_21=np.array(cambios_porcentuales.iloc[:,22])
rend_22=np.array(cambios_porcentuales.iloc[:,23])
rend_23=np.array(cambios_porcentuales.iloc[:,24])
rend_24=np.array(cambios_porcentuales.iloc[:,25])
rend_25=np.array(cambios_porcentuales.iloc[:,26])
rend_26=np.array(cambios_porcentuales.iloc[:,27])
rend_27=np.array(cambios_porcentuales.iloc[:,28])
rend_28=np.array(cambios_porcentuales.iloc[:,29])
rend_29=np.array(cambios_porcentuales.iloc[:,30])
rend_30=np.array(cambios_porcentuales.iloc[:,31])
rend_31=np.array(cambios_porcentuales.iloc[:,32])
len(referencia)
weights=(pd.read_csv("files/2020_01_2022_07 (1)/NAFTRAC_20200131.csv",skiprows=2))
weights=(weights.loc[:,["Ticker","Peso (%)"]]).drop([36,37,2,9,16,17,33,22,28])
###weights
len(weights)
weights["Precio"]=referencia
####weights
cash=1000000*0.0466
cash
comision=0.00125
weights["Capital asignado"]=(weights.loc[:,"Peso (%)"]/100)*(1000000)
weights["Titulos comprados"]=(weights.loc[:,"Capital asignado"]/(weights.loc[:,"Precio"]*(1+comision))).apply(np.floor)
weights
weights["Capital usado"]=((weights.loc[:,"Titulos comprados"]*weights.loc[:,"Precio"])*0.00125)+(weights.loc[:,"Titulos comprados"]*weights.loc[:,"Precio"])
weights
weights["Capital spread"]=weights.loc[:,"Capital asignado"]-weights.loc[:,"Capital usado"]
weights

spread_capitales=weights.loc[:,"Capital spread"].sum()
spread_capitales
weights["Rendimiento mes 1"]=weights.loc[:,"Precio"]*rend_1
weights["Rendimiento mes 2"]=weights.loc[:,"Precio"]*rend_2
weights["Nuevo Valor 2"]=weights.loc[:,"Precio"]*rend_2+weights.loc[:,"Precio"]
weights["Rendimiento mes 3"]=weights.loc[:,"Nuevo Valor 2"]*rend_3
weights["Nuevo Valor 3"]=weights.loc[:,"Nuevo Valor 2"]*rend_3+weights.loc[:,"Nuevo Valor 2"]
weights["Rendimiento mes 4"]=weights.loc[:,"Nuevo Valor 3"]*rend_4
weights["Nuevo Valor 4"]=weights.loc[:,"Nuevo Valor 3"]*rend_4+weights.loc[:,"Nuevo Valor 3"]
weights["Rendimiento mes 5"]=weights.loc[:,"Nuevo Valor 4"]*rend_5
weights["Nuevo Valor 5"]=weights.loc[:,"Nuevo Valor 4"]*rend_5+weights.loc[:,"Nuevo Valor 4"]
weights["Rendimiento mes 6"]=weights.loc[:,"Nuevo Valor 5"]*rend_6
weights["Nuevo Valor 6"]=weights.loc[:,"Nuevo Valor 5"]*rend_6+weights.loc[:,"Nuevo Valor 5"]
weights["Rendimiento mes 7"]=weights.loc[:,"Nuevo Valor 6"]*rend_7
weights["Nuevo Valor 7"]=weights.loc[:,"Nuevo Valor 6"]*rend_7+weights.loc[:,"Nuevo Valor 6"]
weights["Rendimiento mes 8"]=weights.loc[:,"Nuevo Valor 7"]*rend_8
weights["Nuevo Valor 8"]=weights.loc[:,"Nuevo Valor 7"]*rend_8+weights.loc[:,"Nuevo Valor 7"]
weights["Rendimiento mes 9"]=weights.loc[:,"Nuevo Valor 8"]*rend_9
weights["Nuevo Valor 9"]=weights.loc[:,"Nuevo Valor 8"]*rend_9+weights.loc[:,"Nuevo Valor 8"]
weights["Rendimiento mes 10"]=weights.loc[:,"Nuevo Valor 9"]*rend_10
weights["Nuevo Valor 10"]=weights.loc[:,"Nuevo Valor 9"]*rend_10+weights.loc[:,"Nuevo Valor 9"]
weights["Rendimiento mes 11"]=weights.loc[:,"Nuevo Valor 10"]*rend_11
weights["Nuevo Valor 11"]=weights.loc[:,"Nuevo Valor 10"]*rend_11+weights.loc[:,"Nuevo Valor 10"]
weights["Rendimiento mes 12"]=weights.loc[:,"Nuevo Valor 11"]*rend_12
weights["Nuevo Valor 12"]=weights.loc[:,"Nuevo Valor 11"]*rend_12+weights.loc[:,"Nuevo Valor 11"]
weights["Rendimiento mes 13"]=weights.loc[:,"Nuevo Valor 12"]*rend_13
weights["Nuevo Valor 13"]=weights.loc[:,"Nuevo Valor 12"]*rend_13+weights.loc[:,"Nuevo Valor 12"]
weights["Rendimiento mes 14"]=weights.loc[:,"Nuevo Valor 13"]*rend_14
weights["Nuevo Valor 14"]=weights.loc[:,"Nuevo Valor 13"]*rend_14+weights.loc[:,"Nuevo Valor 13"]
weights["Rendimiento mes 15"]=weights.loc[:,"Nuevo Valor 14"]*rend_15
weights["Nuevo Valor 15"]=weights.loc[:,"Nuevo Valor 14"]*rend_15+weights.loc[:,"Nuevo Valor 14"]
weights["Rendimiento mes 16"]=weights.loc[:,"Nuevo Valor 15"]*rend_16
weights["Nuevo Valor 16"]=weights.loc[:,"Nuevo Valor 15"]*rend_16+weights.loc[:,"Nuevo Valor 15"]
weights["Rendimiento mes 17"]=weights.loc[:,"Nuevo Valor 16"]*rend_17
weights["Nuevo Valor 17"]=weights.loc[:,"Nuevo Valor 16"]*rend_17+weights.loc[:,"Nuevo Valor 16"]
weights["Rendimiento mes 18"]=weights.loc[:,"Nuevo Valor 17"]*rend_18
weights["Nuevo Valor 18"]=weights.loc[:,"Nuevo Valor 17"]*rend_18+weights.loc[:,"Nuevo Valor 17"]
weights["Rendimiento mes 19"]=weights.loc[:,"Nuevo Valor 18"]*rend_19
weights["Nuevo Valor 19"]=weights.loc[:,"Nuevo Valor 18"]*rend_19+weights.loc[:,"Nuevo Valor 18"]
weights["Rendimiento mes 20"]=weights.loc[:,"Nuevo Valor 19"]*rend_20
weights["Nuevo Valor 20"]=weights.loc[:,"Nuevo Valor 19"]*rend_20+weights.loc[:,"Nuevo Valor 19"]
weights["Rendimiento mes 21"]=weights.loc[:,"Nuevo Valor 20"]*rend_21
weights["Nuevo Valor 21"]=weights.loc[:,"Nuevo Valor 20"]*rend_21+weights.loc[:,"Nuevo Valor 20"]
weights["Rendimiento mes 22"]=weights.loc[:,"Nuevo Valor 21"]*rend_22
weights["Nuevo Valor 22"]=weights.loc[:,"Nuevo Valor 21"]*rend_22+weights.loc[:,"Nuevo Valor 21"]
weights["Rendimiento mes 23"]=weights.loc[:,"Nuevo Valor 22"]*rend_23
weights["Nuevo Valor 23"]=weights.loc[:,"Nuevo Valor 22"]*rend_23+weights.loc[:,"Nuevo Valor 22"]
weights["Rendimiento mes 24"]=weights.loc[:,"Nuevo Valor 23"]*rend_24
weights["Nuevo Valor 24"]=weights.loc[:,"Nuevo Valor 23"]*rend_24+weights.loc[:,"Nuevo Valor 23"]
weights["Rendimiento mes 25"]=weights.loc[:,"Nuevo Valor 24"]*rend_25
weights["Nuevo Valor 25"]=weights.loc[:,"Nuevo Valor 24"]*rend_25+weights.loc[:,"Nuevo Valor 24"]
weights["Rendimiento mes 26"]=weights.loc[:,"Nuevo Valor 25"]*rend_26
weights["Nuevo Valor 26"]=weights.loc[:,"Nuevo Valor 25"]*rend_26+weights.loc[:,"Nuevo Valor 25"]
weights["Rendimiento mes 27"]=weights.loc[:,"Nuevo Valor 26"]*rend_27
weights["Nuevo Valor 27"]=weights.loc[:,"Nuevo Valor 26"]*rend_27+weights.loc[:,"Nuevo Valor 26"]
weights["Rendimiento mes 28"]=weights.loc[:,"Nuevo Valor 27"]*rend_28
weights["Nuevo Valor 28"]=weights.loc[:,"Nuevo Valor 27"]*rend_28+weights.loc[:,"Nuevo Valor 27"]
weights["Rendimiento mes 29"]=weights.loc[:,"Nuevo Valor 28"]*rend_29
weights["Nuevo Valor 29"]=weights.loc[:,"Nuevo Valor 28"]*rend_29+weights.loc[:,"Nuevo Valor 28"]
weights["Rendimiento mes 30"]=weights.loc[:,"Nuevo Valor 29"]*rend_30
weights["Nuevo Valor 30"]=weights.loc[:,"Nuevo Valor 29"]*rend_30+weights.loc[:,"Nuevo Valor 29"]
weights["Rendimiento mes 31"]=weights.loc[:,"Nuevo Valor 30"]*rend_31
weights["Nuevo Valor 31"]=weights.loc[:,"Nuevo Valor 30"]*rend_31+weights.loc[:,"Nuevo Valor 30"]
weights
fechas=pd.DataFrame(data.reset_index())
fechas.iloc[:,0]
df_pasiva=pd.DataFrame(columns=["Fecha","Capital"])
df_pasiva["Fecha"]=fechas.iloc[:,0]
df_pasiva["Capital"]=[1000000,(weights.loc[:,"Nuevo Valor 2"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 3"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 4"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 5"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 6"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 7"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 8"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 9"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 10"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 11"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 12"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 13"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 14"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 15"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 16"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 17"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 18"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 19"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 20"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 21"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 22"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 23"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 24"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 25"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 26"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 27"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 28"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 29"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 30"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales,(weights.loc[:,"Nuevo Valor 31"]*weights.loc[:,"Titulos comprados"]).sum()+cash+spread_capitales]
df_pasiva["Rendimientos"]=[weights.loc[:,"Rendimiento mes 1"].sum(),weights.loc[:,"Rendimiento mes 2"].sum(),weights.loc[:,"Rendimiento mes 3"].sum(),weights.loc[:,"Rendimiento mes 4"].sum(),weights.loc[:,"Rendimiento mes 5"].sum(),weights.loc[:,"Rendimiento mes 6"].sum(),weights.loc[:,"Rendimiento mes 7"].sum(),weights.loc[:,"Rendimiento mes 8"].sum(),weights.loc[:,"Rendimiento mes 9"].sum(),weights.loc[:,"Rendimiento mes 10"].sum(),weights.loc[:,"Rendimiento mes 11"].sum(),weights.loc[:,"Rendimiento mes 12"].sum(),weights.loc[:,"Rendimiento mes 13"].sum(),weights.loc[:,"Rendimiento mes 14"].sum(),weights.loc[:,"Rendimiento mes 15"].sum(),weights.loc[:,"Rendimiento mes 16"].sum(),weights.loc[:,"Rendimiento mes 17"].sum(),weights.loc[:,"Rendimiento mes 18"].sum(),weights.loc[:,"Rendimiento mes 19"].sum(),weights.loc[:,"Rendimiento mes 20"].sum(),weights.loc[:,"Rendimiento mes 21"].sum(),weights.loc[:,"Rendimiento mes 22"].sum(),weights.loc[:,"Rendimiento mes 23"].sum(),weights.loc[:,"Rendimiento mes 24"].sum(),weights.loc[:,"Rendimiento mes 25"].sum(),weights.loc[:,"Rendimiento mes 26"].sum(),weights.loc[:,"Rendimiento mes 27"].sum(),weights.loc[:,"Rendimiento mes 28"].sum(),weights.loc[:,"Rendimiento mes 29"].sum(),weights.loc[:,"Rendimiento mes 30"].sum(),weights.loc[:,"Rendimiento mes 31"].sum()]
df_pasiva["Rendimientos acumulados"]=df_pasiva.loc[:,"Rendimientos"].cumsum()
df_pasiva

#################################################################

yahoodata2=yf.download(["AMXL.MX","PINFRA.MX","LABB.MX","CUERVO.MX","BOLSAA.MX","LIVEPOLC-1.MX","MEGACPO.MX","BBAJIOO.MX","KOFUBL.MX","ALSEA.MX","FEMSAUBD.MX","GCARSOA1.MX","ALFAA.MX","ORBIA.MX","GRUMAB.MX","PE&OLES.MX","GMEXICOB.MX","GFNORTEO.MX","WALMEX.MX","GFINBURO.MX","CEMEXCPO.MX","TLEVISACPO.MX","GAPB.MX","ELEKTRA.MX","ASURB.MX","KIMBERA.MX","BIMBOA.MX","OMAB.MX","AC.MX"],start="2020-01-31",end="2022-07-29",interval="1d")
data2=pd.DataFrame(yahoodata2).drop(["Volume","Low","High","Adj Close","Open"],axis=1).dropna()
data2
precios_portafolio_año1=data2.iloc[:251,:]
precios_portafolio_año1
rendimientos_logaritmicos=np.log(precios_portafolio_año1/precios_portafolio_año1.shift()).dropna()
rendimientos_logaritmicos
plt.plot(rendimientos_logaritmicos)
logar_plot=plt.show()
rendimientos_logaritmicos.mean()
volatilidad_diaria=(precios_portafolio_año1.pct_change()).std()
volatilidad_diaria
cash=1000000*0.0466
cash
Tickers=(pd.read_csv("files/2020_01_2022_07 (1)/NAFTRAC_20200131.csv",skiprows=2)).drop([36,37,2,9,16,17,33,22,28])
Tickers
Tickers=pd.DataFrame(Tickers).transpose()
Tickers=Tickers.iloc[0,:]
Tickers
len(Tickers)