#!/bin/bash
i=1
echo "<odoo><data>"
while read line
do
    echo "<record id='spaceships_invaders.planet$i'  model='spaceships_invaders.planet'>"
    echo "<field name='name'>$line</field>"
    echo "<field name='photo'>$(base64 planeta.jpg)</field>"
    echo "</record>"
    let i=i+1
done
echo "</data></odoo>"