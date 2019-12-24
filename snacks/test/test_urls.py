from django.test import SimpleTestCase
from django.urls import reverse, resolve
from snacks.views import allListView
from snacks.views import SearchListView, FavouritesListView, ProductDetailView


class TestUrls(SimpleTestCase):
    """Class Test - TestUrls - Testing URLs"""

    # Testing Function based url
    def test_search_all_view_url_resolves(self):
        url = reverse('snacks-allsearch')
        self.assertEquals(resolve(url).func, allListView)

    # Testing Class based url
    def test_SearchListView_url_resolves(self):
        url = reverse('snacks-search')
        self.assertEquals(resolve(url).func.view_class, SearchListView)

    def test_FavouritesListView_url_resolves(self):
        url = reverse('snacks-favourites')
        self.assertEquals(resolve(url).func.view_class, FavouritesListView)

    def test_ProductDetailView_url_resolves(self):
        url = reverse('snacks-detail', args=['9'])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)