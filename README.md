A program to send bulk emails

Usage -> 

```
$ python3 main.py --n <NUMBER-OF-FILES> --d <DELAY> --s <SUBJECT>
```

--n : Number of receivers file

--d : Delay between mails in secs

--s : Subject of mails

Format of receivers file->
  
```  
<sender_email>:<sender_app_pass>
<receiver_email>
<receiver_email>
.
.
.
```

Requirement for senders email

Step1: Enable 2 step authentication

go to home page> tap on name icon> manage your google acocount>  security> under signing in to google> 2-step verification

Step2: Create app password

go to home page> tap on name icon> manage your google acocount>  security> under signing in to google> App password> click on select device and select other(Custom)> give any name and click generate
