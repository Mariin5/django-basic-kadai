#テンプレートをレンダリングする関数
from django.shortcuts import render 
#テンプレートを表示させるための処理、TemplateViewを継承してビュークラスをつくる
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

#TopVIewが処理名、TopVIew内に書かれてる内容が具体的処理
#ビュークラスの命名：処理内容にViewをつける
class TopView(TemplateView):
    #レンダリングするテンプレート名を指定、TempViewを継承してtemplate_nameにファイルを指定して表示
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3

class ProductCreateView(CreateView):
     model = Product
     fields = "__all__"

class ProductUpdateView(UpdateView):
     model = Product
     fields = "__all__"
     template_name_suffix = "_update_form"

class ProductDeleteView(DeleteView):
     model = Product
     success_url = reverse_lazy("list")

class ProductDetailView(DetailView):
     model = Product
     temlpate_name = "Product/product_detail.html"