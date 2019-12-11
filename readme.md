![alt text](static/3.png "")

##This is a django-backend test project from [SplineStudio](https://splinestudio.com/)

*You must complete as many task blocks as possible. Good luck ;)*

Http request with `content-type = application/json`

![alt text](static/2.png "")

1.1. After `git clone` you must create [virtual environment](https://virtualenv.pypa.io/en/latest/) for your project. 
Based on [Python3.6 or latest](https://www.python.org/)

1.2 Install all dependency from `test_project1/requirements.txt` 

1.3 [Create model user with field and migrate](https://docs.djangoproject.com/en/2.1/intro/tutorial02/) to sqlite3: 
* id - primary key
* name - char(string)
* email - char(string) with validation
* password - char(string) with validation and encrypt 

1.4 Create Rest-Api View **([RAV](https://www.django-rest-framework.org/tutorial/3-class-based-views/))** for registration user `method=POST`.

1.5 Create RAV for login (authentication) user in system `method = POST`.

1.5.1 After success authentication user receive authorization token ([JWT](https://pyjwt.readthedocs.io/en/latest/)) for next action.

1.5.2 JWT token should have `user_id` and `expired-time = 7day`.

1.5.3 JWT token should have `refresh-token = 30day`

1.6 Create RAV for refresh current token after expired `method=POST`.

1.7 Create RAV for get user date `method=GET`.
   
![alt text](static/4.png "")

2.1 Create model Album. With relationship user - album.

2.2 Create model Pictures. With relationship album - picture. 

2.3 User can create album for himself.

2.4 User can receive all his album.

2.5 User can sortable his album, filter and pagination.

2.6 User can upload image and save to album.

2.6.1 From `content-type="multipart/form-data"`

2.6.2 From `base64`

2.7 User can receive all his pictures from album.

2.8 User can sortable his pictures, filter and pagination.

2.9 User can change album and picture name.

2.10 User can delete album and picture
 
![alt text](static/5.png "")
 
3.1 Project division on 3-Layer Architecture.

3.2 Project run with gunincorn or uwsgi.

3.3 Simple ws-connect.

3.4 Simple task-manager

3.5 Coverage unittest RAV = 90%