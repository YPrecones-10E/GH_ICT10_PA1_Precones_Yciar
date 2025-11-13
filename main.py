# Working with Sets
from pyscript import display

socsci = {'Carl', 'Gino', 'Alejandro', 'Miguel', 'Aurelia', 'Aisha'}
comarts = {'Carl', 'Gino', 'Alejandro','Yciar', 'Kaitlyn', 'Kyla'}

display(socsci, target = 'one.one')
display(comarts, target = 'one.two')
display(socsci|comarts, target ='two')
display(socsci&comarts, target ='three')
display(socsci-comarts, target ='four')
display(comarts-socsci, target ='five')
display(socsci^comarts, target ='six')













