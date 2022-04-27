from django.test import TestCase

# Create your tests here.


# ----- ACCOUNT VIEWS TESTING ----- #
class AccountViews(TestCase):
    def test_login_view(self):
        page = self.client.get("login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


    def test_signup_view(self):
        page = self.client.get("signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "signup.html")


    def test_logout_view(self):
        page = self.client.get("logout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "logout.html")


    def test_profile_view(self):
        page = self.client.get("profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")


    def test_delete_view(self):
        page = self.client.get("profile/delete-account")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "delete_account.html")

