from django.test import TestCase

# Create your tests here.

# ----- TATTOO BLOG SITE VIEWS TESTING ----- #

class TattooViews(TestCase):
    def test_tattoolist_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tattoo_gallery.html")
    
    def test_create_view(self):
        page = self.client.get("post/create/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tattoopost_create.html")
    
    def test_detail_view(self):
        page = self.client.get("<slug>/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tattoopost_detail.html")
    
    def test_update_view(self):
        page = self.client.get("<slug>/update/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tattoopost_form.html")
    
    def test_deleteconfirm_view(self):
        page = self.client.get("<slug>/delete/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tattoopost_confirm_delete.html")
