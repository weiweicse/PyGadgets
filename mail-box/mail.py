import imaplib
import email

def unicode_conv(s, encoding):
    if encoding is None:
        return unicode(s)
    else:
        return unicode(s, encoding)

def parse_from(mail):
    frm = mail["From"].split()
    if len(frm) == 2:
        from_name = email.Header.decode_header(frm[0])
        return unicode_conv(from_name[0][0], from_name[0][1]), frm[1]
    else:
        return "", frm[0]

def parse_date(mail):
    return mail["Date"]

def parse_subject(mail):
    subject = email.Header.decode_header(mail["Subject"])
    subject = unicode_conv(subject[0][0], subject[0][1])
    return subject

def get_charset(mail):
    return mail.get_content_charset()

def parse_content(mail):
    for part in mail.walk():
        if not part.is_multipart(): # is_multipart returns true if the message's payload is a list of sub-Message objects
            filename = part.get_filename()
            if filename:
                pass
            else:
                content_type = part.get_content_type()
                charset = get_charset(part)
                if content_type in ['text/plain', 'text/html']:
                    if content_type == 'text/plain':
                        suffix = '.txt'
                    elif content_type == 'text/html':
                        suffix = '.html'
                    if charset is None:
                        content = part.get_payload(decode=True)
                    else:
                        content = part.get_payload(decode=True).decode(charset)
    return (content, suffix)

class MailBox:
    def __init__(self, server, username, password, ssl=False):
        if ssl:
            self.imap = imaplib.IMAP4_SSL(server)
        else:
            self.imap = imaplib.IMAP4(server)

        try:
            response, message = self.imap.login(username, password)
            print message[0]
            self.imap.select()
        except:
            print 'Failed to login.'

    # status: ALL, Unseen, Seen, Recent, Answered, Flagged
    def search_by_status(self, status):
        if status.lower() in ["all", "unseen", "seen", "recent", "answered", "Flagged"]:
            _, mail_list = self.imap.search(None, status)
            mail_list = mail_list[0].split()
            return (True, mail_list)
        else:
            print "Status should be one of ALL, UNSEEN, RECENT, ANSWERED, or FLAGGED"
            return (False, [])

    def fetch(self, mail_id):
        _, mail = self.imap.fetch(mail_id, "(RFC822)")
        mail = email.message_from_string(mail[0][1])
        from_name, from_addr = parse_from(mail)
        date = parse_date(mail)
        subject = parse_subject(mail)
        content, suffix = parse_content(mail)
        print "FROM: " + from_name + " " + from_addr
        print "DATE: " + date
        print "SUBJECT: " + subject
        return content, suffix
