import pandas as pd
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import turicreate

from sklearn.metrics.pairwise import pairwise_distances



# pass in column names for each CSV as the column name is not given in the file and read them using pandas.
# You can check the column names from the readme file
#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(r"C:\Users\Administrator.DESKTOP-PNFBAJ5\Desktop\ml-100k\u.user", sep='|', names=u_cols,encoding='latin-1')
#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(r"C:\Users\Administrator.DESKTOP-PNFBAJ5\Desktop\ml-100k\u.data", sep='\t', names=r_cols,encoding='latin-1')
#Reading items file:
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb \
URL', 'unknown', 'Action', 'Adventure',\
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',\
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',\
'War', 'Western']
items = pd.read_csv(r"C:\Users\Administrator.DESKTOP-PNFBAJ5\Desktop\ml-100k\u.item", sep='|', names=i_cols,encoding='latin-1')

print(users.shape)
print(users.head())

print(ratings.shape)
print(ratings.head())

print(items.shape)
print(items.head())

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_train = pd.read_csv(r"C:\Users\Administrator.DESKTOP-PNFBAJ5\Desktop\ml-100k\ua.base", sep='\t', names=r_cols,encoding='latin-1')
ratings_test = pd.read_csv(r"C:\Users\Administrator.DESKTOP-PNFBAJ5\Desktop\ml-100k\ua.test", sep='\t', names=r_cols,encoding='latin-1')

print(ratings_train.shape)
print(ratings_test.shape)


n_users = ratings.user_id.unique().shape[0]
n_items = ratings.movie_id.unique().shape[0]


# print(n_users)
# print(n_items)



data_matrix = np.zeros((n_users, n_items))
for line in ratings.itertuples():
    data_matrix[line[1]-1, line[2]-1] = line[3]

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

# print(user_similarity)
# print(item_similarity)

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #We use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) /np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred

user_prediction = predict(data_matrix, user_similarity, type='user')
item_prediction = predict(data_matrix, item_similarity, type='item')


#第五部分
train_data = turicreate.SFrame(ratings_train)
test_data = turicreate.Sframe(ratings_test)

popularity_model = turicreate.popularity_recommender.create(train_data,user_id='user_id', item_id='movie_id', target='rating')


popularity_recomm = popularity_model.recommend(users=[1,2,3,4,5],k=5)
popularity_recomm.print_rows(num_rows=25)


#Training the model
item_sim_model = turicreate.item_similarity_recommender.create(train_data,
user_id='user_id', item_id='movie_id', target='rating', similarity_type='cosine')
#Making recommendations
item_sim_recomm = item_sim_model.recommend(users=[1,2,3,4,5],k=5)
item_sim_recomm.print_rows(num_rows=25)


##########################################################

class MF():

    #Initializing the user-movie rating matrix, no.of latent features, alpha and beta.
    def __init__(self, R, K, alpha, beta, iterations):
        self.R = R
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    # Initializing user-feature and movie-feature matrix    
    def train(self):
        self.P = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1./self.K, size=(self.num_items, self.K))
        # Initializing the bias terms
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.R[np.where(self.R != 0)])

        # List of training samples
        self.samples = [
        (i, j, self.R[i, j])
        for i in range(self.num_users)
        for j in range(self.num_items)
        if self.R[i, j] > 0
        ]


        # Stochastic gradient descent for given number of iterations

        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))
            if (i+1) % 20 == 0: 
                print("Iteration: %d ; error = %.4f" % (i+1, mse))
        return training_process


        # Computing total mean squared error
    def mse(self):
            xs, ys = self.R.nonzero()
            predicted = self.full_matrix()
            error = 0
            for x, y in zip(xs, ys):
                error += pow(self.R[x, y] - predicted[x, y], 2)
            return np.sqrt(error)


    def sgd(self):
            for i, j, r in self.samples:
                prediction = self.get_rating(i, j)
                e = (r - prediction)
                self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
                self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])
                self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta *
                self.P[i,:])
                self.Q[j, :] += self.alpha * (e * self.P[i, :] - self.beta *
                self.Q[j,:])

        # Ratings for user i and moive j
    def get_rating(self, i, j):
            prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j,
            :].T)
            return prediction

        # Full user-movie rating matrix
    def full_matrix(self):
            return mf.b + mf.b_u[:,np.newaxis] + mf.b_i[np.newaxis:,] + mf.P.dot(mf.Q.T)


R= np.array(ratings.pivot(index = 'user_id', columns ='movie_id', values ='rating').fillna(0))
mf = MF(R, K=20, alpha=0.001, beta=0.01, iterations=100)
training_process = mf.train()
print()
print("P x Q:")
print(mf.full_matrix())
print()