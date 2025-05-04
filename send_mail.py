import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your email and recipient
from_email = "@gmail.com" # your email
from_name = "Facebook Team"
to_email = "1@gmail.com" # Target email

# Gmail SMTP credentials
app_password = "paste your password"  # Use Gmail App Password

# Setup MIME
msg = MIMEMultipart("alternative")
msg['Subject'] = "Action Needed: Your Facebook Account Was Accessed"
msg['From'] = f"{from_name} <{from_email}>"
msg['To'] = to_email

# HTML Email Body
html = """
<!DOCTYPE html>
<html>
  <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f0f2f5;">
    <div style="max-width: 600px; margin: 30px auto; background: #ffffff; padding: 30px; border-radius: 10px; box-shadow: 0px 0px 10px #ccc;">
      <h2 style="color: #1877f2; margin-bottom: 10px;">Facebook Security Alert</h2>
      <p style="font-size: 16px; color: #333;">We've detected suspicious activity on your account from a new location. If this wasn't you, please secure your account immediately.</p>
      <div style="text-align: center; margin: 30px 0;">
        <a href="https://facebook.com/" style="
          background-color: #1877f2;
          color: white;
          padding: 14px 30px;
          border-radius: 6px;
          text-decoration: none;
          font-size: 16px;
          font-weight: bold;
          display: inline-block;
          transition: background 0.3s ease-in-out;
        " onmouseover="this.style.backgroundColor='#145dbf'" onmouseout="this.style.backgroundColor='#1877f2'">Recover Your Account</a>
      </div>
      <p style="font-size: 14px; color: #888;">If this was you, you can safely ignore this message.</p>
      <p style="font-size: 14px; color: #888;">— Facebook Security Team</p>
    </div>
  </body>
</html>
"""

# Attach HTML part
msg.attach(MIMEText(html, "html"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, app_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", str(e))
