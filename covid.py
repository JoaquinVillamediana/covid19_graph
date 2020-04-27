from bokeh.plotting import figure, output_file, show
import requests
import json
if __name__ == '__main__':
  output_file('graficado.html')
  fig = figure()
  times = int(input('Cuantos paises desea graficar (max 5):'))
  colors = ['blue','red','green','orange','black']
  if times > 5:
    times = 5
  for j in range(times):
    country = input('Pais que desea consultar en ingles:')
    response = requests.get(f'https://api.covid19api.com/total/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z')
    while str(response) != '<Response [200]>':
      country = input('Pais Incorrecto, vuelva a ingresar un pais:')
      response = requests.get(f'https://api.covid19api.com/total/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z')
    datta = json.loads(response.content)
  
    x_vals = []
    y_vals = []
    for i in range(len(datta)):
      dict = datta[i]
      x_vals.append(i)
      y_vals.append(dict['Cases'])
    fig.line(x_vals, y_vals, line_width=2 , line_color=colors[j])
  
  show(fig)


  
