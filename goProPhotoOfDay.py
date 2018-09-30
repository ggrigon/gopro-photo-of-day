import requests
import os
import sys
qtd = int(sys.argv[1])
url = "https://api.gopro.com/v2/channels/feed/playlists/photo-of-the-day.json?platform=web&page=1&per_page=";
url = url + str(qtd)


for x in range(qtd):
	print('Baixando a foto {0}' .format(x+1))
	image_index = x;
	obj = requests.get(url);
	data = obj.json();
	image_name = data['media'][image_index]['permalink']+'.jpg';
	image_url = data['media'][image_index]['thumbnails']['full']['image'];
	image_obj = requests.get(image_url);
	image_path = ''+image_name;
	with open(image_path, 'wb') as f:
			f.write(image_obj.content);

print('Script finalizado, aqui é rockz fiii')
