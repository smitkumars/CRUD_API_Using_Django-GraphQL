from django.urls import reverse, resolve

class Testurls:

    def test_detail_url(self):
        path= reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'

    def test_index_url(self):
        path= reverse('index')
        assert resolve(path).view_name == 'index'

    def test_index_url(self):
        path= reverse('create')
        assert resolve(path).view_name == 'create'

