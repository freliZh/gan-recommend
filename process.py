#encoding:utf8
from collections import defaultdict
import pandas as pd
def process_data():
    user_ratings = pd.read_csv("data/ml-latest-small/ratings.csv")
    data = user_ratings.pivot(index='user_id',columns='movie_id',values='rating').replace('NaN', 0)
    print(data)

    # #initial user ratings all equals 0,671 users ,9125 movies
    # user_ratings = defaultdict(list)
    # for i in range(1,9226):
    #     user_ratings[i] = [0 for j in range(9126)]
    #
    # #fill user movie rating matrix
    # with open("data/ml-latest-small/ratings.csv") as f:
    #     for line in f:
    #         try:
    #             parts = line.split(",")
    #             user_id,movie_id,rating = int(parts[0]),int(parts[1]),float(parts[2])
    #             user_ratings[user_id][movie_id] = rating
    #         except Exception as e:
    #             print(parts)
    #             break
    # #print(user_ratings)

if __name__ == "__main__":
    process_data()