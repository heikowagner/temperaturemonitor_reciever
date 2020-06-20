#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from waveshare_2inch_LCD import ST7789
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.INFO)

from sanic import Sanic
from sanic.response import json
import time
import asyncio
import random

import pandas as pd
cols= ['LastUpdate', 'Name', 'Temperature']
current_stats=pd.DataFrame(columns=cols)

#rows_list = []

async def print_temp(device, temp, disp):
    # Clear display.
    # disp.clear()
    print(temp['Temperatur'])
    temperature=int(temp['Temperatur'])/1000
    new_data=pd.DataFrame({'LastUpdate': temp['Time'], 'Name': temp['Hostname'], 'Temperature': temperature}, index=[temp['Hostname']])

    global current_stats
    if not temp['Hostname'] in current_stats.index:
        current_stats = current_stats.append(new_data)
    else:
        current_stats.update(new_data)
    print(current_stats)

        
    #rows_list.append(dict1)
    #print(rows_list)
    # image = Image.new('RGB', (disp.width,disp.height), (255,255,255)) 
    image = Image.new('RGB', (disp.height,disp.width), (000,000,000)) 

    draw = ImageDraw.Draw(image)

    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    print ("***draw line")
    #draw.line([(40,20),(200,20)], fill = "BLUE",width = 5)
    #draw.line([(40,20),(40,200)], fill = "BLUE",width = 5)
    #draw.line([(40,200),(200,200)], fill = "BLUE",width = 5)
    #draw.line([(200,20),(200,200)], fill = "BLUE",width = 5)
    print ("***draw rectangle")
    draw.rectangle([(50,30),(250,70)],fill = "BLUE")
    
    print ("***draw text")
    draw.text((60,30), u'Cluster Stats', font = font30, fill = "WHITE")
    
    position=75
    for row in current_stats.head().itertuples():
        print(row)
        print_out=row.Index + ': '+ str( row.Temperature)  +' C'
        print(print_out)
        draw.text((50, position), print_out, font = font18, fill = "lightgrey")
        position=position+20
    #draw.text((75, 110), '2.0inch LCD ', font = font15, fill = "BLUE")
    #draw.text((72, 140), 'Test Program ', font = font15, fill = "BLUE")

    image=image.rotate(180) 
    disp.ShowImage(image)

    # read bmp file 
    #bmp = Image.open(os.path.join(picdir, 'LCD_2inch.bmp')) 
    #image.paste(bmp, (0,0))  
    #image=image.rotate(190)
    #disp.ShowImage(image)


app = Sanic(name='Reciever')

PORT = 65432        # The port used by the server

print ("2inch LCD Module")
disp = ST7789.ST7789()
# Initialize library.
disp.Init()
    
@app.route('/')
async def hello_world(request):
    print(request)
    print(request.json)
    print(json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string }))
    temp=random.randint(0, 10)
    
    await print_temp('pi1', request.json , disp) #Die Berechnung
    return json({"status": "SUCCESS", "msg": "Berechnung schon fertig:))))"}, status=200)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=PORT)