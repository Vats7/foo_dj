from django.contrib import admin
from django.urls import path, include
from home import views
from order import views as OrderView
from user import views as UserView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('shopcart/', OrderView.shopcart, name='shopcart'),
    path('login/', UserView.login_form, name='login_form'),
    path('logout/', UserView.logout_func, name='logout_func'),
    path('signup/', UserView.signup_form, name='signup_form'),
    
]