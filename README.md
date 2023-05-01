### Numerology

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


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!