from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import RecordModel
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView
from .forms import AccountForm, AddAccountForm


# Create your views here.

def Cooksignupfunc(request):
    if request.method == "POST":
        UserID = request.POST['userID']
        Password = request.POST['password']
        try:
            user = User.objects.create_user(UserID, '', Password)
            return render(request, 'cooksignup.html', {'message':'successfully signed up'})
        except IntegrityError:
            return render(request, 'cooksignup.html', {'message':'you already signed up'})

    return render(request, 'cooksignup.html')

def Cookloginfunc(request):
    if request.method == "POST":
        userID = request.POST['userID']
        password = request.POST['password']
        user = authenticate(request, username=userID, password=password)
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return redirect('list')
            else:
                # アカウント利用不可 
                return render(request, 'cooklogin.html', {'message':'not loged in'})
        # ユーザー認証失敗
        else:
            return render(request, 'cooklogin.html', {'message':'userID or password is invalid.'})
    # GET
    else:
        return render(request, 'cooklogin.html', {'message':''})

@login_required      
def Cooklistfunc(request):
    object_list = RecordModel.objects.all()
    return render(request, 'cooklist.html', {'object_list':object_list})

@login_required
def Cookdetailfunc(request, pk):
    object = get_object_or_404(RecordModel, pk=pk)
    return render(request, 'cookdetail.html', {'object':object})

@login_required
def Cooklogoutfunc(request):
    logout(request)
    # ログイン画面遷移
    return redirect('login')


class CookCreate(CreateView):
    template_name = 'cookcreate.html'
    model = RecordModel
    fields = ('title', 'cookingimages_1', 'cookingimages_2', 'cookingimages_3', 'ingredients', 'recepi', 'memo', 'author')
    success_url =reverse_lazy('list')


class CookDelete(DeleteView):
    template_name = 'cookdelete.html'
    model = RecordModel
    success_url = reverse_lazy('list')


class CookEdit(UpdateView):
    template_name = 'cookedit.html'
    model = RecordModel
    fields = ('title', 'cookingimages_1', 'cookingimages_2', 'cookingimages_3', 'ingredients', 'recepi', 'memo', 'editor')
    success_url = reverse_lazy('list')


class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"cookregister.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"cookregister.html",context=self.params)