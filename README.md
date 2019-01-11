# Flood Risk Dashboard V2
Advancing new methods in flood risk understanding.  

Produced with Plotly's Dash framework, served by Heroku, and available here: <insert link when live>

![Optional Text](../master/assets/screenshot.PNG)
    
deployment is generally handled following this workflow:
https://stackoverflow.com/questions/47949173/deploy-a-python-app-to-heroku-using-conda-environments-instead-of-virtualenv  
-git status  
-git add .  
-git commit -m "commit message here"  
-git push heroku master 
  
Procfile is required for heroku 
.slugignore identifies files to ignore in heroku slug  
environment.yml and requirements.txt identify required python packages for app  
assets folder holds css and image files
