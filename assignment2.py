from imdbpie import Imdb

imdb = Imdb()

# print(imdb.search_for_title("The Dark Knight"))
# reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])

def get_imdb_reviews(movie_title):
    """
    Function that returns all the reviews for a given movie title
    """
    movie = imdb.search_for_title(movie_title)[0]
    imdb_id = movie['imdb_id']
    reviews = imdb.get_title_user_reviews(imdb_id)
    return reviews

# print(get_imdb_reviews("Parasite"))

def get_review_text(reviews):
    """
    Function that returns a random review from the first 20 reviews of a movie
    """
    import random
    random_number = random.randint(1, 20)
    review_text = reviews['reviews'][random_number]['reviewText']
    return review_text

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(review_text):
    """ 
    Function that returns a tiple contianing the review text and the sentiment analysis score it recieved
    """
    score = SentimentIntensityAnalyzer().polarity_scores(review_text)
    return review_text, score

def lexical_diversity(review_text):
    return len(set(review_text)) / len(review_text)


def main():
    reviews = get_imdb_reviews("Parasite")
    # print(reviews)
    review_text = get_review_text(reviews)
    # print(review_text)
    sentiment = sentiment_analysis(review_text)
    # print(sentiment)
    lexical_div = lexical_diversity(review_text)
    print(lexical_div)


if __name__ == '__main__':
    main()