import lyricsgenius as genius
import csv
from random import randint
import time


# Insert client ID
api = genius.Genius('<YOUR API KEY HERE>', timeout = 1000)


# opens file in read mode and creates a reader
with open('No_results.csv', 'r', encoding='mac_roman') as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')

    # opens file in write mode and creates a writer
    with open('df_no_results.csv', 'w', encoding='utf-8', newline="") as csv_output:
        csv_writer = csv.writer(csv_output, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

        # line counter
        line_count = 0

        # iterate over every line
        for row in csv_reader:
            # read item in row
            item_artist = row[1]
            item_song = row[0]

            # write header to csv
            if line_count == 0:
                print('Writing csv header')
                csv_writer.writerow([item_artist,item_song,"Lyrics"])
                # time.sleep(randint(10,40))

                # add to counter
                line_count += 1

            # write other lines to csv
            else:
                # search api for lyrics
                lyrics = api.search_song(item_song,item_artist)

                # check if lyrics returned a true-ish response
                if lyrics:
                    # True, proceed to writing row with lyrics
                    print('Result found. Writing row {} to csv'.format(line_count))
                    csv_writer.writerow([item_artist,item_song,lyrics])
                    # time.sleep(randint(10,40))
                else:
                    # False, proceed to writing row without lyrics
                    print('Result found. Writing row {} to csv'.format(line_count))
                    csv_writer.writerow([item_artist,item_song,"No results"]) 
                    # time.sleep(randint(10,40))

                # add to counter
                line_count += 1

        print('Processed {} lines.'.format(line_count))
