import pytest 

from B_info.models import Business

class TestModels:

    @pytest.mark.django_db
    def test_create(self):
        business_name = Business.objects.create(B_name="Wipro")
        assert business_name.B_name == "Wipro"

   # @pytest.mark.django_db
    @pytest.fixture
    def test_detail(db):
        business_name = Business.objects.get(B_name="Wipro")
        assert business_name.B_name == "Wipro"

    @pytest.fixture
    def test_update_category(db):
        business_name = Business.objects.create(B_name="IRCTC")
        business_name.B_name = "HCL"
        business_name.save()
        busi_db = Business.objects.get(B_name="HCL")
        assert busi_db.B_name == "HCL"

    @pytest.fixture
    def test_filter(db):
        Business.objects.create(B_name="Reliance")
        assert Business.objects.filter(B_name="Reliance").exists()



