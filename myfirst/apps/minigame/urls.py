from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name = 'index'),
	path('1/',views.page1, name = 'page1'),
	path('2y/',views.page2, name = 'page2'),
	path('3y/',views.page3, name = 'page3'),
	path('4y/',views.page4, name = 'page4'),
	path('5y/',views.page5, name = 'page5'),

	path('2/',views.page2n, name = 'page2n'),
	path('3/',views.page3n, name = 'page3n'),
	path('4/',views.page4n, name = 'page4n'),
	path('5/',views.page5n, name = 'page5n'),

]