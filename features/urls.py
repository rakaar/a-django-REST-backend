from django.urls import path
from . import views

urlpatterns = [
	path('learnlists/', views.AllLearnLists.as_view(), name='get_all_learnlists'),
	path('learnlist/<int:id>', views.IndivLearnList.as_view(), name='get_indiv_learnlist')

]