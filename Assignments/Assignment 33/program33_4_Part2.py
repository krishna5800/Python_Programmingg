import smtplib
from email.message import EmailMessage
import os

def Mail_Send(sender, app_password, receiver, subject, body, file_name):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail header
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Add automated mail sender 
    # filepath = "Marvellous_2026-03-03_23-43-39.log"
    
    # fobj = open("Marvellous_2026-03-03_23-43-39.log", "rb")

    # file_data = fobj.read()

    # msg.add_attachment(
    # file_data,
    # maintype='text',          # Use 'text' for .log or .txt files
    # subtype='plain',         # Use 'plain' for simple text logs
    # filename = "Marvellous_2026-03-03_23-43-39.log"       # The name as it will appear in the email
    # )   

    # 1. Use 'r' before the string to handle Windows backslashes correctly
    filepath = file_name

    # 2. Open and read the file in binary mode
    with open(filepath, "rb") as fobj:
        file_data = fobj.read()
        # Extract just the filename (Marvellous_...log) from the full path
        file_name = os.path.basename(filepath)

    # 3. Add the attachment to your msg object
    msg.add_attachment(
        file_data,
        maintype='text',
        subtype='plain',
        filename=file_name  # Using the extracted filename instead of the full path
    )

    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password
    smtp.login(sender, app_password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close the connection
    smtp.quit()
