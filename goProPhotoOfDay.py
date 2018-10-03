# -*- coding: utf-8 -*-

import requests
import os
import sys
import sqlite3

DB_LOC = 'backup.db'
DB_NAME = 'download_history'

qtd = int(sys.argv[1])
url = "https://api.gopro.com/v2/channels/feed/playlists/photo-of-the-day.json?platform=web&page=1&per_page=";
url = url + str(qtd)
obj = requests.get(url);
data = obj.json();


conn = sqlite3.connect(DB_LOC)
with conn:
    conn.execute('CREATE TABLE IF NOT EXISTS download_history (url text)')

for x in range(qtd):
    print('Baixando a foto {0}' .format(x+1))
    image_index = x;
    image_name = data['media'][image_index]['permalink']+'.jpg';
    image_url = data['media'][image_index]['thumbnails']['full']['image'];

    cursor = conn.execute('SELECT url FROM {} WHERE url = ?'.format(DB_NAME), (image_url, ))

    is_downloaded = cursor.fetchone() is not None

    if not is_downloaded:

        image_obj = requests.get(image_url);
        image_path = ''+image_name;
        with open(image_path, 'wb') as f:
            f.write(image_obj.content);
        with conn:
            conn.execute('INSERT INTO {} (url) VALUES (?)'.format(DB_NAME), (image_url, ))

    else:
        print('{} downloaded. Skip.'.format(image_url))

print('Script finalizado, aqui é rockz fiii')
