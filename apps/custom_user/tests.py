from django.test import TestCase


# Create your tests here.
class UserTest(TestCase):

    def add_an_existing_as_beneficiary(self):
        """
        Try adding an existing beneficiary to the beneficiary list.

        The email provided to add the beneficiary is already in the user's beneficiary list.
        """
        raise NotImplementedError

    def add_an_notified_user_as_beneficiary(self):
        """
        Try adding a previously notified beneficiary to the list of beneficiaries.

        The email provided to add the beneficiary previously has been sent a notification of intention to transfer, but
        the user has not registered in the system. In this case the notification has not expired.
        """
        raise NotImplementedError

