# Project Dataset README

## Complete Dataset - Paragraphs

The `complete_dataset_paragraphs.csv` file contains a comprehensive collection of paragraphs, each labeled either manually or automatically, enriched with the following information:

- **paragraph_id**: Unique identifier for each paragraph.
- **paragraph**: Text of the paragraph under consideration.
- **label_sexist**: Binary label indicating sexism; 1 if the probability of sexism exceeds 0.5, else 0. This field is used for determining whether a song is deemed sexist or not (refer to the paper or main README.md for detailed information).
- **probability_sexist**: The model derived probability of sexism. For manually labeled paragraphs, this field mirrors the value in the 'label_sexist' column.
- **label_racialized**: Binary label indicating racialization; 1 if the probability of racialization exceeds 0.5, else 0.
- **probability_racialized**: The algorithmically derived probability of racialization. Similar to 'probability_sexist,' manually labeled paragraphs have matching values in this field and the 'label_racialized' column.
- **labeling_method_sexist**: Indicates whether the paragraph was labeled as sexist manually or automatically using the model.
- **labeling_method_racialized**: Specifies the manual or automatic labeling method for racialization.
- **Reason**: Categorization of manually labeled paragraphs as sexist, providing additional context.
- **Song Name**: The title of the song associated with the paragraph.
- **Song Artist**: The artist(s) behind the song.

## Complete Dataset Information - Songs

The `complete_dataset_information_songs.csv` file comprehensively documents information related to each song:

- **Song Name:** The title of the song.
- **Language:** The language in which the lyrics of the song are written, following the two-letter language code (refer to [ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
- **Hit Year:** The year in which the song was most listened to, which may differ from the song's release year.
- **Song Artist:** The name of the artist(s) associated with the song.
- **Source:** The platform (radio/programme or streaming platform) where the song was available and listened to during the hit year.
- **Decade:** The decade to which the hit year belongs. Note that the last decade (2020) includes only the years 2020, 2021, and 2022.
