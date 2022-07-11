# [Email Sender](https://mail-sender-jai91.azurewebsites.net)

*WebApp built on DJango and deployed temporarily on Azure Which can Send Group Emails seperated by categories*

### [Live](https://mail-sender-jai91.azurewebsites.net)


## Features 

- [x] - Can Add N number of categories and send Emails to different groups of people

- [x] - Initially , Sender details and details will be hidden . By Clicking on Category name you can expand it to show 

- [x] - Can be run on localhost (Should clone , run as django server)

- [x] - Saves Your previous details like subject , message so that you can easily modify data and send mail's again

- [x] - Mails can be sent to any available Domains 

- [x] - Works on send_mail module [Learn More](https://docs.djangoproject.com/en/4.0/topics/email/) 

## Limitations 

-  Should add all the categories in the begginging itself , else Data gets wiped at every Category

-  Only outlook SMTP is supported at the moment [Guide](https://kinsta.com/blog/outlook-smtp-settings/)

-  Category once added cannot be deleted

## Bugs 

- By clicking on a category name for expansion , other category properties getting changed(Reason: querySelectorAll in L#173 of we*/index.html

- Data will get wiped if added a new category in between

- Yet to find 


<div align="center">
  <sub>If you found a new bug / have a solution for one / have some improvments, feel free to send a PR!</sub>
</div>
