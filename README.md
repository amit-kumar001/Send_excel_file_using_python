# Send_excel_file_using_python
## Key feature
<ol>
<li>Now we have to send .txt files or excel files in the mail using python language.</li>
<li><strong> smtplib </strong> module is used to make communication with a mail server to send mail.</li>
<li><strong>from email.mime.multipart </strong> package is used to make MIME conventions for the multipart data or it can be created by a client as part of creating a new MimeMessage.We used MIME for enhanced message security.</li>
<li>MIMEMultipart() method is used to  encodes ['From'], ['To'], and ['Subject'] in the Python documentation.</li>
<li>Now we can attach the body of the email to the MIME message.</li>
<li>Provide the name of the file that we want to send via mail.</li>
<li>In <strong> open() </strong>method we have to provide the path of a file with permission of rb . Here 'r' means just for read the file, We can also open a file in <strong>“rb”</strong> (read binary), “w” (write), “a” (append), or “wb” (write binary). Note that if you use either “w” or “wb”, Python will overwrite the file.</li>
<li>It used for application or a document that must be opened in an application, such as a spreadsheet or word processor. application/octet-stream attachment help to open all kind of content in an email.</li>
<li><strong>set_payload </strong> will load the file from a given path with reading permission</li>
<li>Encode data by calling the <strong>encode_base64()</strong> function. We encode our 'p' variable in which we load a spreadsheet.</li>
<li><strong>Content-Disposition </strong> is a header indicating. It used to display our attachment in which we store the path of a file. The file will be stored in string format.</li>
<li>Now a message attached with the file </li>
<li>Create SMTP connection with the help of server request and port no </li>
<li><strong> s.starttls()</strong> method is used to start <strong>TLS</strong> (Transfer layer security) security. </li>
<li>Now provide sender mail id with password.</li>
<li><strong>msg.as_string()</strong> method is used to convert multipart message into string</li>
<li><strong>sendmail() </strong> method is used to send mail.</li>
</ol>  

### Required Permission in google account
To send file using python language, we have to give some permission in google account.
open sender google account -> select security option ->click on Less secure app access ->Allow less secure apps: ON This permission allows us to send mail.  

### Result in mail    

![img3](https://user-images.githubusercontent.com/47202519/53322260-dbaf6900-3900-11e9-967a-b4914e7a4674.png)  

### How to run this file  
 Since this is a python file, hence it can be run using following command

python mail2.py

python3 mail2.py

