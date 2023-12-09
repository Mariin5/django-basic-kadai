from django.db import models #DB構造を定義するためのmodels。models.Modelクラスを継承してDB構造を取り決める
from django.urls import reverse

class Category(models.Model):
     name = models.CharField(max_length=200)
 
     def __str__(self):
         return self.name
    
#モデルクラス命名：名詞単数
class Product(models.Model):
    #モデルクラス内の属性を「モデルフィールド」と呼ぶ(各列の取り決め、文字列etc)
    #左の属性名（フィールド名）が、DBのカラム名になる
    #=以降はフィールドの制約、型を指定
    #name → models.CharField：文字列、max_length=200：最大200文字、デフォルトで入力必須
    #price → models.PositiveIntegerField：数値型、（Positive：正の整数）
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')
    detail = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    #return f"{self.name} {self.price}"で両方表示

    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
         return reverse('list')

