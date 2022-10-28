# Subreddit Parsing and Classification

## Problem Statement

To someone unfamiliar with the genre, fantasy literature all seems the same. Most people are familiar with the common tropes: magic, swords, knights, dragons and adventures. While these things are common to most fantasy novels, there must be distinguishing factors that determine the popularity of potential fantasy series. To book publishers such as Tor and HarperCollins, these differences matter greatly. In terms of marketing: how do we reach potential customers? what keywords are popular among the fanbase? do certain topics, terms or names attract the interests of potential readers? In terms of deciding what to publish: Will any book with the common tropes suffice? Are series-specific jargon a signifier of success? Is being able to sustain an active fan community vital to high sales? In this report, I will analyze the fanbases active on Reddit of two popular fantasy series: A Song of Ice and Fire (known for the popular TV adaption A Game of Thrones) and The Stormlight Archives (written by Brandon Sanderson and one of the highest selling fantasy series to date). By collecting and parsing Reddit posts from their respective subreddits, and building a classifier that can identify what truly distinguishes these series and fanbases, I hope to answer some of these questions.

## Data Structure
The data for this project was collected from two subreddits: r/asoiaf, and r/Stormlight_Archive. For the sake of brevity, these will be frequently referred to as GT and SA respectively in my notebooks. Over 1000 posts were collected from each Subreddit and combined into seperate Dataframes, stored in the data directory as SA_data.csv and GT_data.csv. These were later engineered and combined into book_data.csv, which contained all the data that will be used. In final modelling, Count Vectorized DataFrames were generated to train my classification models.

## Data Dictionary
Below is a dictionary of the columns in the book_data.csv, after cleaning and feature engineering. The data used in predictions was Count Vectorized based on the words in each post and contain 5,000 columns, each representing a word or word pair.

| feature | dtype |Description
| --- | --- | --- |
| selftext | object |This column contains the raw text of each post
| subreddit | object |This column contains the subreddit the text originated from. It is the final y value.
| title | object |The title of each post
| tokenized_text | object |Post text seperated into tokens. This removed punctuation and other symbols
| tokenized_text_clean | object |tokenized text with engligh stopwords removed
| char_count | int64 |The character count of each post
| word_count | int64 |The word count of each post
| tagged_tokens | object |cleaned tokenized text with parts of speach for each word
| lemmatized_words | object |Cleaned, tokenized text reduced to the root form of each word


## Work Flow

### Retrieving and Combining Reddit Data
#### 01Retrieving_and_Combining_Data.ipynb

Using the python requests library, I accessed PushShiftAPI to collect 250 posts from each subreddit for each month in 2020 until enough data was collected. These were parsed into post text, title and subreddit, and combined into DataFrames. Rows without text, "removed" text, or NA values were dropped. These were then written to csvs for further analysis.

### Data Processing and Feature Engineering
#### 02Processing_and_Feature_Engineering.ipynb

Here the data was prepared. All post text was converted into lower case for easier handling. Using the RegexpTokenizer, another column was created with tokenized words from each post. English stopwords were identified and removed from these words and put into a new column. Columns containing word and character counts from the original posts were created as well. The cleaned text was then lemmatized, or reduced to the root words for each word, and put into yet another column. This is the text from which Count Vectorization will be done later. Finally, the DataFrames were combined into one, shuffled, and written to a new csv: book_data.csv.

### Exploratory Data Analysis and Visualization
#### 03EDA_and_Visualization.ipynb

In this notebook, I explored and visualized the data I had prepared. First I generated a series of histograms and bar charts that explored the distribution of word and character counts for each subreddit. I noticed that SA posts were on average about half the length of GT posts, and there was a large concentration of short SA posts. There were some outlier posts going into 1,000s and words and 100s of 1,000s of characters, but these were relatively rare. Next, I began to look at the text itself. Using a count vectorizor for exploratory purposes, I gathered the most popular words and word pairs in each subreddit. I noticed that many of these were terms specific to their respective books and did not make sense outside of that context. Others were character, book, or author names. Both when looking at pairs of words, and when using a Tfidf vectorizer to identify more original words, these series specific terms were even more dominant. Normal everyday words were only common when looking at single words from normal Count Vectorization.

### Modelling and Predictions
#### 04Modelling.ipynb

Here I began to use two different classification models to identify patterns in the subreddits. I Count Vectorized my data into 5,000 columns, each signifying the presence of a word or term, and began to model. I first chose Random Forest Classifier. This model is known for having a high classification accuracy, and is especially good at dealing with large data consisting of thousands of variables, which is what I had. Random Forest works by generating multiple decision trees, each modeling a subset of the rows and columns, and merging them together for more accurate predictions. By swapping in and out data, individual trees may be able to find patterns and splits in the data that can be important to the classification, but would normally be lost among stronger signals. I Chose Support Vector Machine for my second model. This model is also good with high dimensional data, and especially unstructured data. It works by creating a hyperplane that can seperate the two classes. It is also able to add extra dimensionality to the data so that clusters of classes can be more easily seperated by the hyperplane. 

I grid searched number of estimators and max depth for Random Forest, and the C value for SVM in order to find the best hyperparameters. After cross validation and test data prediction, Random Forest achieved the highest accuracy of about 0.93. Since the classes were evenly balanced (51% vs 49%) I decided accuracy was a useful metric.


## Conclusions

My research here was revealing about the interests of fans and customers in their reading habits. Having an active fanbase is an extremely important signifier for the success and popularity of a series, and this correlates strongly with their communities on reddit, how much the fans interact, and what they talk about. By analyzing these subreddits I took a useful snapshot of how potential customers behave.

The first factor of note is book adaptions. The Song of Ice and Fire series was always popular, but activity skyrocketted when popular television adaptions of these books began to come out. Although A Game of Thrones ended several years ago, activity in this subreddit remains high. Adapting a series, or publishing more books in an already adapted series, is a good way to ensure high interest. 

Another important factor is frequency of book releases. The Stormlight Archives series publishes regularly every 3 years, and published a book in the year 2020 from which the data was collected. The title of said book, Rythym of War, was very high in frequency when analyzing the text. Likewise, the most recently published book in the Game of Thrones series was mentioned often. Extra priority should be given in terms of marketing and publishing to series that regularly come out with new books.

Having series specific jargon seems to be a sure way to gather a fanbase. These were by far the most common popular terms discussed in the reddit texts. This relationship is simple: give fans something specific to discuss and theorize about, and they will. The community will be more active, more engaged, and probably more likely to purchase new books as they come out. Character names were also occured very frequently, because fans love to discuss their favorite characters and what may happen to them in the future. In short, give the fans something to get attached to.

By following these guidelines, publishers have a useful roadmap of what to publish and continue publishing. The series I analyzed are two of the most popular fiction book series IN HISTORY, and this does not happen by accident. Though these series are different in detail, as shown by the success of my classification models, they can be identified and distinguished by the same types of factors. By looking at what they did right, and what the fans are attracted to, future books can follow in their success as well.
