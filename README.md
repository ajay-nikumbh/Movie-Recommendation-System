# Movie-Recommendation-System

### 1. Streamlit Ui 


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
web: sh setup.sh && streamlit run iris_streamlit_demo.py
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

```py

```
