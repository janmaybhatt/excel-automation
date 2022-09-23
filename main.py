from email.message import EmailMessage
import smtplib


if __name__ == '__main__':
    var = int(input('Enter 1 for first email or 2 for second email format: '))
    msg = EmailMessage()
    msg['Subject'] = 'This is my email for multiple people'
    msg['From'] = 'jrbhatt18p10@gmail.com'
    msg['To'] = ['dealslover999@gmail.com']
    if var == 1:
        msg.set_content('''
    <!DOCTYPE html>
    <html>
        <body>
            <div style="background-color:#eee;padding:10px 20px;">
                <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
            </div>
            <div style="padding:20px 0px">
                <div style="height: 500px;width:400px">
                    <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                    <div style="text-align:center;">
                        <h3>Article 1</h3>
                        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                        <a href="#">Read more</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    ''', 'html', 'utf-8')
    elif var == 2:
        msg.set_content('''
        <!DOCTYPE html>
    <html>
        <body>
            <div style="background-color:#eee;padding:10px 20px;">
                <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
            </div>
            <div style="padding:20px 0">
                <div style="height: 500px;width:400px">
                    <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;" alt="dummy">
                    <div style="text-align:center;">
                        <h3>Article 2</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut beatae debitis ea et ex ipsa itaque iure, quae rem sunt.</p>
                        <a href="#">Read more</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
        ''', 'html', 'utf-8')
    msg.add_attachment('test.xlsx')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('jrbhatt18p10@gmail.com', 'lsiuxunnobxrdici')
        smtp.send_message(msg)
