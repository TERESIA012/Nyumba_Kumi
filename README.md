# Nyumba-Kumi

#### Created By Teresia King'ori 

## Description

A django application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Setup Requirements

- Git
- Web-browser or your choice
- Github
- Django 3.2.7
- Pip
- Python 3.8
- PostgreSQL
- Cloudinary (for image upload)

```
   - CLOUD_NAME
   - API_KEY
   - API_SECRET
```

## Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3.8 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

```
pip install -r requirements.txt
```

- To copy .env.example to .env

```
cp .env.example .env
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver
```

- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action

## Technologies Used

The following languages have been used on this project:

- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL

## Setup/Installation Requirements

- Live link to view the project <a target="_blank" href="">Live Link</a>

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link on te navbar and fill the form  | If login is successful, user is navigated to home page | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Edit profile | On the account link, click on the   profile to update| Redirected to the profile page and edit your profile |
| Click on join hood| Redirects to the view/leave hood page | if user clicks on join hood,he/she can view post/business and add post/business|
|Add a new new hood|Click on the new hood at the navbar  redirected to the add hood form|the post will be rendered to the neighborhood  page
| Click on log Out in the accounts| Redirects to the home page | Logs out user  |

## Known Bugs

So far so good there are no bugs related to this project 

## Support and contact details 

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: kingoriteresia@gmail.com


## License

Copyright (c) 2021 Teresia King'ori
