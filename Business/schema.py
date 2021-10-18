import graphene
from graphene_django import DjangoObjectType

from B_info.models import Business

class CategoryType(DjangoObjectType):
    class Meta:
        model = Business
        fields = ("B_name","Owner_info","phone","email","address","employee_size")

#class IngredientType(DjangoObjectType):
 #   class Meta:
  #      model = Ingredient
   #     fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
  #  all_ingredients = graphene.List(IngredientType)
    #category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    categoryBusi = graphene.List(CategoryType)
    #def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
     #   return Ingredient.objects.select_related("category").all()

    def resolve_categoryBusi(root, info, **kwargs):
        try:
            return Business.objects.all()
        except Business.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)