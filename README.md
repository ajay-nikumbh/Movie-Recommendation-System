# Movie-Recommendation-System

![image](https://user-images.githubusercontent.com/37560890/183598989-45e431c6-c66f-40c3-8bfc-606a78880a4d.png)
![aja](https://user-images.githubusercontent.com/37560890/183597991-1d0820b1-c5c2-4f1a-b599-c9f2323e3e7d.png)

#### A. Content Based Filtering
1. They suggest similar items based on a particular item. 
2. This system uses item metadata, such as genre, director, description, actors, etc.
3. For movies, to make these recommendations. 
4. The general idea behind these recommender systems is that if a person liked a particular item
he or she will also like an item that is similar to it.

#### B. Collaborative Filtering

1. This system matches persons with similar interests and provides recommendations based on this matching.
2. Collaborative filters do not require item metadata like its content-based counterparts.

### 1. Project Overview

A. Data collection : [Tmdb 5000 dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

![image](https://user-images.githubusercontent.com/37560890/183575278-fc9da1e9-b9cf-44e9-a953-8c082108d028.png)

B. Data set after cleaning text

![image](https://user-images.githubusercontent.com/37560890/183575485-ef3bd59d-6121-46e6-9f64-2a9678551ce4.png)

C. Recommend function

```py
def recommend(movie):
    
    # Fetch the index
    movie_index= new_df[new_df['title'] == movie].index[0]
    
    # Fetch the distances
    distances = similarity[movie_index]
    
    # Get the 5 similar movies 
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    # Now print the first indexe's of the top 5 similar movies
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

```

### 2. Streamlit Ui 


![image](https://user-images.githubusercontent.com/37560890/183477463-4c1b6778-1f2c-4166-9971-381ba284c217.png)
![image](https://user-images.githubusercontent.com/37560890/183476828-a751733c-11b3-436f-be30-409a8e1cba3a.png)
![image](https://user-images.githubusercontent.com/37560890/183477100-9334723e-ea9d-421f-b14d-8bef998e97d9.png)

### 2. Deploying a Streamlit app to Heroku

1. Folder structure

![image](https://user-images.githubusercontent.com/37560890/183566414-2271d181-461a-4fa7-a127-93d447a751b8.png)

2. setup.sh file

`
‘setup.sh’ specifies the commands to be executed to configure the environment before running the app. 
In our ‘setup.sh’, we first create a ‘.streamlit’ directory to store the credentials and config files. 
Then, we specify the e-mail registered with streamlit.io and write it to a ‘credentials.toml’ file.
Then, we add the config details to the ‘config.toml’ file. 
Both these files reside in the ‘.streamlit’ directory.
`

```sh
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"email@domain\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

```

3. Procfile

`
‘Procfile’ lists the commands to be executed to start the app. 
In our ‘Procfile’, we’ll first run ‘setup.sh’ that creates the required config files.
Then run the app using the ‘streamlit run’ command.
`

```py
web: sh setup.sh && streamlit run app.py
```

4. Heroku commands

```py 
$ heroku login
$ git init
$ heroku git:remote -a mrs-ajay
$ git add .
$ git commit -am "make it better"
$ git push heroku master

```
