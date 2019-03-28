import SchemDraw as schem
import SchemDraw.elements as e
d = schem.Drawing()

top = {'cnt':2,
       'labels':['+','-'],
       'plabels':['1','2'],
       'lblsize':12,
       }

Fan = e.blackbox(d.unit*2, d.unit*2, 
                   tinputs=top,leadlen=1.5, mainlabel='Fan')
T = d.add(Fan)

d.draw()