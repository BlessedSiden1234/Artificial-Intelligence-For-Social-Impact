<div align="center">

# AI For Social Good

## Suicidal Ideation Detection In Online Social Content

<img src="Assets/web.gif" > 
</div>

---

## Getting Started

The rapid growth of social media and online communities has provided anonymous and supportive spaces where individuals openly discuss their mental health, emotions, and personal struggles. To support suicide prevention efforts, it is crucial to identify suicide-related content and signs of suicidal ideation in online environments using Natural Language Processing techniques. This project focuses on platforms such as Reddit and Twitter, where user-generated posts are analyzed and classified as either indicating potential suicide risk or showing no suicidal intent through text feature extraction, machine learning, and deep learning approaches.

## Datasets

Collected two sets of data from Reddit and Twitter. The Reddit data set includes (2958) suicidal ideation samples and a number of non-suicide texts (5381). The Twitter dataset has a total (3000) tweets with suicidal ideation.
Reddit Data was scraped from subreddits like 'suicide watch', 'depression', 'anxiety' etc. Twitter data was collected by querying keywords like 'end my life', 'die' etc.

**The Twitter word cloud (left) and Reddit word cloud (right) are shown as follow:**

<div align="center">
 <img alt="Demo" src="./WordClouds/twitter.png" height="300px" width="400px" />
 &nbsp; &nbsp;
 <img alt="Demo" src="./WordClouds/reddit.png" height="300px" width="400px"/>
</div>

## Feature Processing and Training

- Performed text cleaning and removed some corpus-specific stopwords. And plotted word cloud to visualize the frequently occurring words in a corpus.
- Performed vectorization using Both Bag of Words and TFIDF Vectorizer.
- Used grid search cv to find the best parameters to train the model using Random Forest Classifier and archived an accuracy of 96%.
- Trained the model using Multilayer Bidirectional LSTM with GLOBE embedding to attain an accuracy of 97%.

## Results

Results of different methods applied

| Model        | Acc. | Pre. | Rec. | F1   |
| ------------ | ---- | ---- | ---- | ---- |
| RF + TFIDF   | 0.96 | 0.96 | 0.96 | 0.96 |
| LSTM + GLOBE | 0.97 | 0.97 | 0.97 | 0.97 |

## Usage

- `Dataset` : All the collected and cleaned dataset
- `Data_Collection` : Code for scraping data from reddit and twitter
- `Src` : All The source code for text preprocessing and building ml models
- `Pretrained_Models` : All the Pretrained Models and tokenizers
- `Flask`: Code for server and model deployment

### To run the server:

- `cd Flask`
- `python app.py`

## License

Distributed under the MIT License. See `LICENSE` for more information.<br/>
