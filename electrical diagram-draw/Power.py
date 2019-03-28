import SchemDraw as schem
import SchemDraw.elements as e
d = schem.Drawing()

top = {'cnt':9,
       'labels':['L','N','Gnd','-v','-v','-v','+v','+v','+v'],
       'plabels':['4','8'],
       'lblsize':12,
       }

Power = e.blackbox(d.unit*2.5, d.unit*4.5, 
                   tinputs=top,leadlen=1, mainlabel='Power')
T = d.add(Power)

d.draw()