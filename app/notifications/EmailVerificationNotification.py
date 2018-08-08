''' A EmailVerificationNotification Notification '''
from notifications import Notifiable

class EmailVerificationNotification(Notifiable):

    def mail(self):
        return self.subject('New account signup!') \
            .driver('smtp') \
            .heading('Masonite App With User Verification') \
            .line('In order to use your account, you have to validate your email address.') \
            .line('Please click on the link below.') \
            .action('Validate my account', href=self._link)