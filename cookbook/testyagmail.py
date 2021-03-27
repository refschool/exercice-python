import yagmail, ssl
yag = yagmail.SMTP(user='referencementschool@gmail.com', password='S9')
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('yvon.huynh@gmail.com', 'from python', contents)