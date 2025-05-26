from random import randint
import lyricsgenius as genius
import csv
import time



# Insert client ID
api = genius.Genius('<YOUR API KEY HERE>', timeout = 10000)

with open('No_results.csv', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            item_artist = row[1]
            item_song = row[0]
            # print(f'\t{row[0]}\t{row[1]}')
            song = api.search_song(item_song,item_artist)
            filename = item_song.replace("/","_") + "_" + item_artist.replace("/","_")
            if song is not None:
                song.save_lyrics(filename='lyrics/txt/'+filename+'.txt',extension='txt')
                # song.save_lyrics(filename='lyrics/json/'+filename+'.json',extension='json')
                time.sleep(randint(10,40))

            line_count += 1
    print('Processed {line_count} lines.')
