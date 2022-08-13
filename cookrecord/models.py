from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# Create your models here.
class RecordModel(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField(auto_now=True)
    cookingimages_1 = models.ImageField(upload_to='cook_pics',null=True, blank=True,)
    cookingimages_2 = models.ImageField(upload_to='cook_pics',null=True, blank=True,)
    cookingimages_3 = models.ImageField(upload_to='cook_pics',null=True, blank=True,)
    ingredients = models.TextField()
    recepi = models.TextField()
    memo = models.TextField(null=True, blank=True,)
    author = models.CharField(max_length=50,null=True, blank=True,)
    editor = models.CharField(max_length=50,null=True, blank=True,)

    def __str__(self):
        return self.title



# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    # ユーザー(ユーザー名、パスワード、メールアドレス）
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
    