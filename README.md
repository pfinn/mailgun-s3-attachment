mailgun-s3-attachment
=====================

## What This Is
A Heroku-ready Flask.py application that creates an HTTP endpoint for parsing and storing (Amazon S3) attachments from Mailgun.

## What This Is Not
Many, many things.

## Pre-Requisets
* Working credentials/accounts for Amazon AWS/S3, Heroku and Mailgun

## Getting Started
    C:\> git clone https://github.com/pfinn/mailgun-s3-attachment.git
    C:\> cd mailgun-s3-attachment

## Next Steps (Required!)
* Provide your AWS credentials (or set the proper environment variables) in lines 12 and 13 inside *app.py*

* Your will also need to provide a globally unique bucket name for storing attachments on line 14 of *app.py*

* Commit changes to git repo
## Launch

    C:\> heroku create
    C:\> git push heroku master
    C:\> heroku open

When your browser opens, you'll be greeted with an example on how to create a working Mailgun route to use with this Heroku instance.

## Notes
This works with the free plans of Heroku and Mailgun (as of 12/08/12).