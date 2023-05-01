## Numerology

- Deployment [Numerology](https://numerology.herokuapp.com).

## User Experience (UX)

On this app, the user can insert their name and the system will calculate and reveal the number that belongs
to the user according to numerology. For each letter there is a number from 1 to 9, so the system will
calculate the final number by adding all the numbers of each letter.
This app is for users that are curious about numerology or already know the principles of numerology and
would like to calculate their number without having to calculate it themselves.

![Captura de tela 2023-05-01 031339](https://user-images.githubusercontent.com/74268139/235392233-75945269-696a-409f-b19a-a8399426fb48.jpg)

![Captura de tela 2023-05-01 031450](https://user-images.githubusercontent.com/74268139/235392447-8fc3bcd1-d262-497a-b465-919de63ae93c.jpg)



## User Expectation

- As a user, I expect to find an app that is easy to navigate and intuitive.
- As a user, I expect the app to be accurate when calculating my number from my name.

## Design

- Colour

The main colour is the basic of the command-line. The background is black and
the letters are white.

- Animation
There is a menu with a basic animation.

## Features
 - Responsive on all device sizes
 - Interactive elements

## Technologies Used

- Python
- CSS3
- Javascript
- Json

## Frameworks, Libraries & Programs Used
1. [Python Org](https://www.python.org/downloads).
 - I need to download in my computer and run the Command-line.

2. [Install Numerology](https://pypi.org/project/numerology).
- A simple multilanguage numerology

3. [Heroku](https://herokuapp.com)
-  Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern app

4. GitHub:
- GitHub is used to store the projects code after being pushed from Git

5. Gitpod
- Gitpod is an open source developer platform automating the provisioning of ready-to-code developer environments.

## Testing
I found an error when printing the result in line 62, because I was calling the wrong function. After that, I
found an error in line 46 because I didn’t close the bracket in the menu.
- [Extends Class](https://extendsclass.com/python-tester.html).
- [Online Python](https://www.online-python.com).

## Deployment
The project was deployed in HerokuApp.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Credits
 1. Code:
 - [Python](https://pythonbasics.org).
 - [Real Python](https://realpython.com).
 - Code Institute
 
 ## Acknowledgements
- Slack Code Institute.
- Tutor support at Code Institute for their support.
- Code Institute