import pandas
import mpld3
import matplotlib.pyplot as plt
import plotly.express as px
var1= pandas.read_csv("covid.csv")
var= var1.sort_values(by='age')
age=var['age']
DurationOfTreatment= var[' DurationOfTreatment']
CostOfTreatment= var[' CostOfTreatment']
DidTheyDie= var[' DidTheyDie']
fig = plt.figure(figsize = (9,4))

#scatter1
plt.subplot(2,2,1)
xage = age
ydur =  DurationOfTreatment
plt.scatter(xage, ydur, color='yellow')
plt.title("Age and duration of treatment")
plt.ylabel("Duration in days")
plt.xlabel("Age in years")
plt.savefig('bank_data.png')
plt.savefig('bank_data.png')


#scatter2
plt.subplot(2,2,2)
x = DurationOfTreatment
y = CostOfTreatment
plt.title('Duration to Cost')
plt.xlabel('Duration in Days')
plt.ylabel('Cost in Rs.')
plt.scatter(x, y, color='Blue')
plt.savefig('bank_data.png')

#scatter3
plt.subplot(2,2,3)
x = DidTheyDie
y = age
plt.title('Mortality')
plt.xlabel('age')
plt.ylabel('1 for Alive 0 for deceased')
plt.scatter(y, x,color='Red')
plt.savefig('bank_data.png')
#scatter 4
plt.subplot(2,2,4)
x = CostOfTreatment
y = age
plt.title('Mortality')
plt.xlabel('1 for Alive 0 for deceased')
plt.ylabel('age')
plt.scatter(x, y,color='Green')
plt.savefig('bank_data.png')

#save the image of subplotd


#mpld3
html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()

