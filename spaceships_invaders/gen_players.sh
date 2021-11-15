#!/bin/bash
i=1
echo "<odoo><data>"
while read line
do
    nom=$(echo $line | cut -d',' -f1)
    birthday=$(echo $line | cut -d',' -f2)
    echo "<record id='spaceships_invaders.player$i'  model='spaceships_invaders.player'>"
    echo "<field name='name'>$nom</field>"
    echo "<field name='birth_date'>$birthday</field>"
    #echo "<field name='planet' ref='spaceships_invaders.planet$i'></field>"
    echo "</record>"
    let i=i+1
done
echo "</data></odoo>"