<AM I Responsive overlay: https://ui.dev/amiresponsive>


## Table of contents
- [Django Bakery Introduction](#django-bakery-introduction)
  - Nested List Item                                          
- [UX](#ux)
  - Agile Methologies
  - User Stories (epic > >)
  - Wireframes
  - Database design
- [Technologies](#technologies) 
  - Languages
   -  
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Elephant SQL](#elephant-sql)
  - [Cloudinary](#cloudinary)
  - [Heroku](#heroku) 
  - [Forking with GitHub](#forking-with-github)
  - [Cloning with GitHub](#cloning-with-github)
- Fourth Item
- [Credits](#credits)



## Django Bakery Introduction
Django bakery is a website for lovers of baked goods to share their recipies and leave feedback to other contributors.
With a registered account users can like, submit, edit and delete posts. 
The live website can be accessed here <link>

## UX

## Technologies

## Features

## Testing

## Deployment

### Elephant SQL

Elephant SQL was used to host postgres databases and linked with Heroku:

1. Create an Elephant SQL account and login via elephantsql.com.
2. Select 'Create new instance' and choose the free plan 'Tiny Turtle'.
3. Select data center region closest to your geographical location.
4. Select 'Review' and if details are satisfactory select 'Create Instance'.
5. Select the newly created instance and open 'Details' section
6. Copy the postgres URL for this instance for later use with Heroku deployment.

### Cloudinary 

Cloudinary platform was used to host static files and media.

1. To create a Cloudinary account navigate to cloudinary.com.
2. Select 'Sign up for Free' and choose sign up option.
3. Select 'Create Account'.
4. From Cloudinary Dashboard copy 'API Environmental Variable' for later use with Heroku deployment.

### Heroku

Django Bakery was deployed to Heroku as per the below steps:
1. Create a Heroku account and login via id.heroku.com/login.
2. From 'Dashsboard' select 'New' and 'Create new app'.
3. Choose a name for the app and select region (Europe/United States).
4. Select 'Create app'.
5. To apply settings select the "Settings" button.
6. Select "Reveal Config Vars".
7. Add a Key called 'DATABASE_URL' and for the value enter the URL copied from elephantsql.com (Elephant SQL, step: 6.).
8. Add a Key called 'SECRET_KEY' and enter your choise of secret key value.
9. Add a Key called 'CLOUDINARY_URL' and for the value enter the 'API Environmental Variable' copied from cloudinary.com (Cloudinary, step: 4.).
10. Add a key called 'PORT' with a value of '8000'.
11. From the 'Deployment' tab select 'GitHub' in the 'Deployment method' section. Select 'Connect to GitHub' at the bottom of the page.
12. In the search field search for your GitHub repository name.
13. Select 'Connect' to link up with the GitHub repository.
14. Further down the page select deployment method automatic ('Enable Automatic Deploys') or manual ('Deploy branch').

### Forking with GitHub
1. Open [GitHub](https://github.com).
2. Navigate to the intended repository.
3. Select "Fork" in the top rigth corner of the page.
4. Select the owner of the fork repository in the drop menu provided.
5. Select the "Create Fork" button.
6. Your copy of the original repository has been created.

### Cloning with GitHub
1. Open [GitHub](https://github.com).
2. Navigate to the intended repository.
3. Select the "Code" button on the top of the repository page.
4. Select the copy button for one of the three options: "HTTPS", "SSH" or "GitHub CLI".
5. Open Terminal (or command line tool) on your local computer.
6. In Terminal change the current working directory to the directory where the clone will reside.
7. In Terminal type: "git clone" followed by a space. Paste the URL copied in (step 4.).
8. In Terminal press "Enter"/"Return" to create a local copy of the repository on your computer.

## Credits

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome sven-cork,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

### Django Bakery - Introduction