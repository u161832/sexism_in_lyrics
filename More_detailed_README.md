# Sexism in the lyrics of the most listened to songs in Spain

This repository contains code, data and information for an ongoing research project on sexism in music lyrics.

The research analyzed the lyrics of more than two thousand songs released throughout a period of about six decades (1960-2022). We used automatic text classification based on manually labeled training data to categorize music lyrics as sexist or non-sexist, while detecting broad categories of sexist speech present in them. The main findings show that sexism has been prevalent during the observation period, and has increased considerably over the last decade.

## Data Collection

In order to gather the data, an initial research phase was undertaken to identify the most popular songs in Spain for each decade spanning from 1960 to 2022. This effort resulted in a dataset that encompasses song titles, artists, hit years, languages, and data sources. Given the significant shifts in listening behaviors over the observation period, diverse data sources were employed to accommodate these changes. This study relied on three distinct sources to compile the list of the most listened-to songs in Spain: "Los40," "Los Superventas," and Spotify's top songs. Currently, people in Spain listen to music an average of 20 hours per week (https://www.promusicae.es/descarga-informes/engaging-with-music-2021-infografia-datos-de-espana-n237/). Indeed, most people listen to music on streaming platforms such as Spotify, TikTok or YouTube, although there are people who listen to it on the radio or by other means. Moreover, the digital music market in Spain has increased immensely in the last years, being now much more important than the physical one (https://www.promusicae.es/descarga-informes/mercado-musica-grabada-espana-2019-n204/). Therefore, for the most recent period (2010-2022), the data was obtained using the Spotify API (https://developer.spotify.com/documentation/web-api/). From 2010 to 2015, as well as for 2022, here were lists available of the top 100 tracks in Spain each year that could be downloaded (https://open.spotify.com/playlist/11H3xmArMqDAQf5sv7i8eD). Meanwhile, the playlists for the songs from 2017 to 2021 were available on a weekly basis (https://spotifycharts.com/regional/es/weekly/2016-12-23--2016-12-30). To find the top songs of each of those years, we automatically identified the songs that were repeated with the most frequency throughout the year. This allowed us to obtain the most streamed songs of each year. During the decades before 2010, the radio was the main channel that people in Spain used to listen to music. The democratization of radio in Spain transformed it into a powerful tool for promoting popular music. Initially, Spanish music dominated during the thirties, forties, and fifties. However, “Discoman ́ıa” and the rise of rock and roll from the 1960s onwards reshaped radio, paving the way for it to become a major disseminator of this new genre. Charts like “Los Superventas” section (Pintado, 2017) directly influenced

## Manual labeling and modeling

The process of manual labeling and model development was carried out iteratively, resulting in increasingly accurate models. To enhance labeling efficiency, each model version was utilized to stratify the data sample for labeling in the subsequent iteration.

**Pre-existing labeled datasets.** We acquired pre-existing datasets, summarized on Table I, with text labeled as sexist or not sexist. Most of these datasets are based on texts found in social media, such as Twitter postings (“tweets”) or Reddit comments, which are quite different from music lyrics. These datasets were used exclusively to train a preliminary classification model for detecting sexism, not for the final model. We found only one dataset comprised of lyrics which we used for testing our preliminary classification model. Nevertheless, the lyrics in this dataset were not organized into verses or paragraphs. 

**Learning scheme.** Our model operates as a supervised classification system, taking a music lyrics paragraph as input and generating a binary inference regarding the presence or absence of sexist language within it. While dynamic word embeddings such as BERT (Devlin and Chang, 2018) are sometimes more effective than other methods (Rudolph and Blei, 2018), for this model we chose to use Language-Agnostic Sentence Representations (LASER) embeddings (Artetxe and Schwenk, 2019). This is because LASER embeddings can be applied across multiple languages, and our sample is multilingual. As previously stated, we examined the performance of various models on several labeled pre-existing datasets. The Support- Vector Machine (SVM) (Cortes and Vapnik, 1995) classifier and the Long Short-Term Memory (LSTM) neural network classifier yielded the most favorable outcomes. We selected LSTM for its demonstrated effectiveness in text classification (Butt et al., 2021, Grosz and Conde- Cespedes, 2020, Sharifirad and Matwin, 2019). 

**Iterative modeling and labeling process.** We created three versions of the model. The first version was based on the pre-existing labeled datasets summarized on Table I. We used this version to sample paragraphs from songs from the years 1960-1969 (664 samples), and 2021 (1451 samples), which provide a diverse range of vocabulary. The sample was stratified by probability of being sexist, with roughly one third high probability, one third low probability, and one third medium probability. This hierarchization was instrumental in revealing the initial model’s inability to accurately categorize paragraphs. Considering this, we resorted to manual labeling as our approach. This manual annotation process entailed categorizing paragraphs as either exhibiting sexism or not, along with specifying the particular category of sexism if applicable. In this regard, we adhered to the established criteria for evaluating whether a paragraph exhibited sexist content. Specifically, a paragraph was categorized as sexist if it fell within one of the analytical categories of sexism against women depicted on Table II. In instances where there was uncertainty regarding whether a paragraph should be classified as sexist, we refrained from labeling it as such to prevent ambiguity during the training process. The annotations were carried out by one author of this paper, and any borderline cases were deliberated upon in consultation with another author of this paper. 
The second version of the model was created using only these new labels, discarding the labels from previous work, which involved domains different from the one under study. We used it to sample, again in a stratified manner, about 100 randomly selected paragraphs from each decade (600 paragraphs in total). This information was then used to train the model that would detect racialization in lyrics. We added these samples to our training set, and used it to train the third version of the model. 


Table I: Pre-existing labeled datasets with sexist/not sexist categories, used for the preliminary classification model.

|Dataset|Source|#Entries|Language|
|---|---|---|---|
|Lyrics|Slim (2019)|532|EN|
|Reddit comments|Guest (2021)|6567|EN|
|Tweets (EXIST) TRAIN|EXIST (2021)|6977|EN, ES|
|Tweets (EXIST) TEST|EXIST (2021)|4368|EN, ES|
|Tweets (MeTwo)|Rodriguez (2020)|3333|ES|


Table II: Categories of sexism found in our music lyrics (own elaboration), from most frequent to least frequent in the manually-labeled training set
|Category|Lyrics Examples|
|---|---|
|Control and possession behaviour|	Baby I'm preying on you tonight.|
|Hyper-sexualization|Un movimiento muy sexy (sexy). (A very sexy movement.)|
|Attribute stereotyping|Tú sabiendo que e' una diabla, diabla. (You knowing that she's a demon, demon.)|
|Women objectification|Tu cuerpo a mí me aloca. Quiero por siempre tenerte, tenerte. (Your body drives me crazy. I want forever to have you, to have you.)|
|Body shaming|Con su trasero supo ganarse la admiración. (With her ass she was able to earn admiration.)|
|Physical violence|Solía amarla, pero tuve que matarla, tuve que enterrarla seis pies bajo tierra y aún puedo oír cómo se queja. (I used to love her, but I had to kill her, I had to bury her six feet under and I can still hear her moaning.)|
|Sexual assault,  excluding rape|Que tengo la polla en candela y quiero comerte ese culo. ( I've got my dick on fire and I want to eat your ass.)|
|Sexual harassment, excluding assault|Let me bend that ass over.|
|Slut shaming|Te veo enseñar el culo y las tetas a los tíos delante de mi cara. (I see you flashing your ass and tits at guys in front of my face.)|
|Victim blaming|Carolina trátame bien, o al final te tendré que comer. (Carolina treat me well, or I'll have to eat you in the end.)|
|Rape|Tendría que besarte, desnudarte, pegarte y luego violarte hasta que digas sí. (I would have to kiss you, strip you, beat you and then rape you until you say yes.)|
|Threats|Pues si quiero hacerte daño, solo falta que yo quiera.(Well, if I want to hurt you, I only need to want to.)|
|Gaslighting|Ella se hace la más boba. (She plays the fool.)|
|Role stereotyping|Ella sabe hacerlo todo en la casa. (She knows how to do everything in the house.)|
|Motherhood-related discrimination|Fuck you, hijueputa. ( Fuck you, motherfucker.)|


## Further explorations

Inquisitively, we conducted and exploratory analysis and observed that the majority of songs that have between two and all of their paragraphs labeled as sexist belong to the 2010s to 2020s period (refer to Table III). In addition, our analysis reveals that 92% of the featured artists in these songs are men. Among the most prevalent genres in the songs from the last decades, Urban Latin stands out, although Pop is the only genre that appears across all decades. Conversely, we did a brief examination of 41 randomly selected non-sexist songs (see Table IV for details), and we found that although Pop music remains dominant, other music genres represented are more diverse than in the sample of sexist songs. Anecdotally, we observe in the sample of sexist songs from Table III a larger prevalence of male artists than in the sample of non-sexist songs of Table IV. 


Table III: Titles with random sample of songs with 100% of paragraphs marked as sexist (shaded rows are songs by female artists)
| Title                                       | Artist            | Decade | Genre       |
| ------------------------------------------- | ------------------ | ------ | ----------- |
| Twist and shout                             | The Beatles        | 1960   | Rock        |
| Quince años tiene mi amor                   | Duo Dinamico       | 1960   | Pop         |
| Balada gitana                               | Duo Dinamico       | 1960   | Pop         |
| Tonight my love tonight                     | Paul Anka          | 1960   | Pop         |
| Delilah                                     | Tom Jones          | 1960   | Pop         |
| Gorrion                                     | Miguel Gallardo    | 1970   | Pop         |
| Can the can                                 | Suzi Quatro        | 1970   | Rock        |
| Brother Louie                               | Modern Talking     | 1980   | Pop         |
| Somethig bout you baby I like               | Status Quo         | 1980   | Pop         |
| A woman loves a man                        | Joe Cocker         | 1980   | Country     |
| Maria                                       | Blondie            | 1990   | Pop         |
| Bumpy Ride                                  | Mohombi            | 2010   | Dance-Pop   |
| Rude Boy                                    | Rihanna            | 2010   | Dance       |
| Cosas locas                                 | Danny Romero       | 2010   | House       |
| Sugar                                       | Maroon 5           | 2010   | Pop         |
| Gyal you a party animal                    | Charly Black       | 2010   | Dance       |
| Traicionera                                 | Sebastian Yatra    | 2010   | Urban Latin |
| Unica                                       | Ozuna              | 2010   | Urban Latin |
| La Rubia                                    | La Nueva Escuela   | 2020   | Urban Latin |
| Relacion                                    | Sech               | 2020   | Urban Latin |
| Yo perreo sola                              | Bad Bunny          | 2020   | Urban Latin |
| PAM                                         | Justin Quiles      | 2020   | Urban Latin |
| Flamenkito                                  | Lerica             | 2020   | Pop         |
| Rutina                                      | Myke Towers        | 2020   | Urban Latin |
| Diosa                                       | Myke Towers        | 2020   | Urban Latin |
| Explicito                                   | Myke Towers        | 2020   | Urban Latin |
| Hola                                        | Dalex              | 2020   | Urban Latin |
| La dificil                                  | Bad Bunny          | 2020   | Urban Latin |
| Loco                                        | Beéle              | 2020   | Pop         |
| Indeciso                                    | Reik               | 2020   | Urban Latin |
| China                                       | Annuel AA          | 2020   | Urban Latin |
| Kesi                                        | Camilo             | 2020   | Urban Latin |
| Tutu                                        | Camilo             | 2020   | Urban Latin |
| Travesuras                                  | Nio Garcia         | 2020   | Urban Latin |
| A donde vamos                               | Morat              | 2020   | Pop         |
| Nathy Peluso Bzrp Music Sessions Vol. 36    | Bizarrap           | 2020   | Urban Latin |
| Reloj                                       | Rauw Alejandro     | 2020   | Urban Latin |
| Veneno                                      | Delaossa           | 2020   | Urban Latin |

Table IV: Titles with 41 random non-sexist songs (shaded rows are songs by female artists)
| Title                                       | Artist            | Decade | Genre       |
| ------------------------------------------- | ------------------ | ------ | ----------- |
| Si je chante                                | Sylvie Vartan      | 1960   | Pop         |
| Soy rebelde                                 | Jeanette           | 1970   | Latin ballad|
| Melina                                      | Camilo Sesto       | 1970   | Latin ballad|
| Stayin alive                                | Bee gees           | 1970   | Disco       |
| Algo mas                                    | Camilo Sesto       | 1970   | Pop         |
| Esta noche me quiero descolgar              | Trupita            | 1980   | Techno      |
| Breakthoven                                 | Baron Rojo         | 1980   | Heavy Metal |
| Never gonna give you up                    | Rick Astley        | 1980   | Dance-pop   |
| Old before I die                           | Robbie Williams    | 1990   | Rock        |
| Pump up the jam                            | Technotronic       | 1990   | House       |
| Go west                                    | Pet Shop Boys     | 1990   | Disco       |
| Have you seen her                          | Mc Hammer          | 1990   | Hip-hop     |
| Baby I love you                           | Big Mountain       | 1990   | Reggae      |
| La deuda de la mentira                    | Danza Invisible    | 1990   | Rock/Pop    |
| The man who sold the world                | Nirvana            | 1990   | Glam rock   |
| Fields of Gold                            | Sting              | 1990   | Rock        |
| Don't speak                               | No doubt           | 1990   | Pop         |
| Dalai lama                                | Mecano             | 1990   | Pop         |
| Chihuahua                                 | Dj bobo            | 2000   | Eurodance   |
| Quiero ser                               | Amaia Montero      | 2000   | Pop         |
| You're beautiful                          | James Blunt        | 2000   | Rock/Pop    |
| Aunque no te pueda ver                    | Alex Ubago         | 2000   | Pop         |
| Musica para una boda                      | Nacho Cano         | 2000   | Pop         |
| Te busqué                                 | Nelly Furtado      | 2000   | Reggae      |
| Dream on                                  | Depeche Mode       | 2000   | Electronic  |
| Whenever, whenever                        | Shakira            | 2000   | Pop         |
| Flames                                    | David Guetta       | 2010   | Electropop  |
| It's time                                 | Imagine Dragons    | 2010   | Rock/Pop    |
| Mi verdad                                 | Maná and Shakira   | 2010   | Rock/Pop    |
| Reality                                   | Lost frequencies and Janieck Devy | 2010 | Electronic |
| Terriblemente Cruel                       | Leiva              | 2010   | Indie/Rock  |
| Antes de que cuente diez                  | Fito y Fitipaldis  | 2010   | Rock        |
| Live your life                            | Mika               | 2010   | Hip-hop     |
| Roar                                      | Katy Perry         | 2010   | Pop         |
| Sing                                      | Ed Sheeran         | 2010   | R\&B        |
| Thunder                                   | Imagine Dragons    | 2010   | Electropop  |
| Wake me up                                | Avicii             | 2010   | House       |
| Malibu                                    | Miley Cyrus        | 2010   | Electropop  |
| Ain't nobody loves me better             | Felix Jaehn        | 2010   | Electronic  |
| Con la mano levanta'                      | Macaco and Estopa  | 2010   | Latin pop   |
| Where have you been                      | Rihanna            | 2010   | Dance-pop   |


## References
Devlin, Jacob, y Ming-Wei Chang. «Open sourcing BERT: State-of-the-art pre-training for natural language processing.» _Google AI Blog 2_ (2018).

Rudolph, Maja, and David, Blei. «Dynamic embeddings for language evolution.» _In Proceedings of the 2018 World Wide Web Conference_ (pp. 1003–1011).2018.

Artetxe, Mikel, y Holger Schwenk. «Massively multilingual sentence embeddings for zero-shot cross-lingual transfer and beyond.» _Transactions of the Association for Computational Linguistics_ (MIT Press) 7 (2019): 597–610.

Cortes, Corinna, y Vladimir Vapnik. «Support-vector networks.» _Machine learning_ (Springer) 20 (1995): 273–297.

Butt, Sabur, Noman Ashraf, Grigori Sidorov, y Alexander Gelbukh. «Sexism identification using BERT and data augmentation-EXIST2021.» _International Conference of the Spanish Society for Natural Language Processing SEPLN 2021, IberLEF 2021._ 2021.

Grosz, Dylan, y Patricia Conde-Cespedes. «Automatic detection of sexist statements commonly used at the workplace.» _Pacific-Asia Conference on Knowledge Discovery and Data Mining._ 2020. 104–115.

Sharifirad, Sima, y Stan Matwin. «When a tweet is actually sexist. A more comprehensive classification of different online harassment categories and the challenges in NLP.» _arXiv preprint arXiv:1902.10584_, 2019.

Slim, Kammoun. «Feminism vs. Sexism in Lyrics: A Portrait of Women in Recent Music.» _Feminism vs. Sexism in Lyrics: A Portrait of Women in Recent Music._ GitHub, 2019.

Guest, Ella. «online-misogyny-eacl2021.» _online-misogyny-eacl2021._ GitHub, 2021.

EXIST. «EXIST: sEXism Identification in Social neTworks.» _EXIST: sEXism Identification in Social neTworks._ 2021.

Rodriguez, Francisco. «MeTwo: Machismo and Sexism Twitter Identification dataset.» _MeTwo: Machismo and Sexism Twitter Identification dataset._ GitHub, 2020.
