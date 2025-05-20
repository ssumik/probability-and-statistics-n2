import pandas
import os
from sklearn import linear_model
import sys

print("\n")
csv = input("digite o nome do arquivo csv dentro da pasta 'dataset':")
csv_path = os.path.abspath('.' + '/dataset/' + csv)

try:
    csv_data = pandas.read_csv(csv_path)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
    sys.exit(1)
except pandas.errors.ParserError:
    print("Erro ao fazer o parse do CSV.")
    sys.exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    sys.exit(1)

print(csv_data)
"""
x = csv_data[['Hours Studied', 'Previous Scores','Extracurricular Activities','Sleep Hours','Sample Question Papers Practiced']]
y = csv_data['Performance Index']

linear_regretion = linear_model.LinearRegression()
linear_regretion.fit(x, y)

predictedPerformance = linear_regretion.predict(x)
coeficient = linear_regretion.coef_

print(coeficient)"""