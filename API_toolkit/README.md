# APIs-for-Media
Developed the content generation via ```Django-RestAPI```
![demo](https://github.com/Dhiraj240/APIs-for-Media/blob/master/API_toolkit/pictures/demo.gif)

Add ```requirements.txt``` using
```
pip3 freeze > requirements.txt
```
Admin will need a login authorisation because i have used ```createsuperuser``` django command.
To change it use :
```
cd API_toolkit
python manage.py  createsuperuser
```
Everything is provided in the gif.

# Execution in local Machine
For this you need atleast ```django 1.11.6``` 


```
git clone https://github.com/Dhiraj240/APIs-for-Media.git
cd APIs-for-Media
cd API_toolkit
python manage.py runserver
```
