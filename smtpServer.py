"""simple python smtp server for test purpose """

from datetime import datetime
import asyncore
from smtpd import SMTPServer
import sys

# don't forget to create a mail/ folder
folderForMail = "mail/"

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        f = open(folderForMail+filename, 'w')
        f.write(data)
        f.close
        print '%s saved.' % filename
        self.no += 1


def run(server,host):
    foo = EmlServer((server, int(port)), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':

        if len(sys.argv) != 3:
                print "USAGE: host port"
        else:
                _, server, port = sys.argv
                run(server,port)

