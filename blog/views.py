from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

#https://di-acc2.com/programming/python/2534/を参考に
from django.views.generic import TemplateView # テンプレートタグ
from .forms import CommentForm,AccountForm, AddAccountForm,ChangeDayForm
# サインイン・ログインに必要なライブラリをDjangoからインポート
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('post_list'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))

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
        return render(request,"register.html",context=self.params)

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

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"login.html",context=self.params)

# ↓は通常の画面   
@login_required
def post_list(request):

    posts = Post.objects.all()
    comments = Comment.objects.all().order_by('-id')
    error = ""
    user = request.user.username
    print(user)
    user_profile = Post.objects.filter(userid=user)
    sorted_posts = []
    sort_by = request.GET.get('sort_by', 'studyday_type')
    selected_studyday_type = request.GET.get('studyday_type_filter', '')  # 選択された学習日タイプを取得
    current_time = timezone.now()  # 現在の日時を取得
    current_time = current_time - timedelta(days=7)

    # 学習日タイプの選択肢
    studyday_type_choices = [
        ('Tuesday 17:00', 'Tuesday 17:00'),
        ('Tuesday 18:00', 'Tuesday 18:00'),
        ('Wednesday 17:00', 'Wednesday 17:00'),
        ('Wednesday 18:00', 'Wednesday 18:00'),
        ('Friday 17:00', 'Friday 17:00'),
        ('Friday 18:00', 'Friday 18:00'),
        ('Saturday 10:00', 'Saturday 10:00'),
        ('Saturday 11:00', 'Saturday 11:00'),
        ('Saturday 13:00', 'Saturday 13:00'),
        ('Saturday 14:00', 'Saturday 14:00'),
    ]

    if sort_by == 'studyday_type':
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('studyday_type')
    else:
        # ソート条件が 'studyday_type' 以外の場合も、デフォルトは studyday_type でソート
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('studyday_type')

    # 選択された学習日タイプに基づいてフィルタリング
    if selected_studyday_type:
        sorted_posts = posts.filter(studyday_type=selected_studyday_type)

    # 検索機能
    # クエリパラメータから検索キーワードを取得
    search_query = request.GET.get('q')

    # 検索キーワードがある場合、名前と学校で部分一致検索を実行
    if search_query and selected_studyday_type:
        posts = sorted_posts.filter(
            Q(name__icontains=search_query) |  # 名前で部分一致検索
            Q(school__icontains=search_query) | # 学校で部分一致検索
            Q(katakana__icontains=search_query) # カタカナで部分一致
        )
        if not posts:
            error = "<img src='../static/image/work/noting.png' width='50%'>"
        
    elif search_query and not selected_studyday_type:
        posts = posts.filter(
            Q(name__icontains=search_query) |  # 名前で部分一致検索
            Q(school__icontains=search_query) |  # 学校で部分一致検索
            Q(katakana__icontains=search_query) # カタカナで部分一致
        )
        if not posts:
            error = "<img src='../static/image/work/noting.png' width='50%'>"
    
    elif not search_query and selected_studyday_type:
        posts = sorted_posts
        # 検索がかけられていない時にnone値ではなくデフォルトメッセージを表示する
        search_query = ""

        if not posts:
            error = "<img src='../static/image/work/noting.png' width='50%'>"

    else:
        search_query = ""
        posts = []

        if not posts:
            # home画面の画像
            error = "<img src='../static/image/work/attention.png' width='80%'>"

    
    

    return render(request, 'post_list.html', {
        'posts': posts,
        'sort_by': sort_by,
        'studyday_type_choices': studyday_type_choices,
        'search_query': search_query,
        'error': error,
        'comments':comments,
        'current_time': current_time,  # 現在の日時をコンテキストに追加
        'user_profile': user_profile, #　生徒用のPost取得用
        })

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('-id')[1:]
    ratest_comment = Comment.objects.filter(post_id=pk).last()
    return render(request, 'post_detail.html', {'post': post,'comments': comments,'ratest_comment':ratest_comment})

# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.published_date = timezone.now()
#             comment.save()
#             return redirect('post_list')
#     else:
#         form = CommentForm()
#     return render(request, 'post_new.html', {'form': form})


backurl = []  # 空のリストを作成

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # request.META.get() で取得した値をリストに追加
    backurl.append(request.META.get('HTTP_REFERER', 'post_list'))

    largest_odd_index = -1  # 一番大きい偶数の順番を格納する変数
    largest_odd_value = -1  # 一番大きい偶数の値を格納する変数

    # バックURLリスト内の要素を順番に走査
    for index, url in enumerate(backurl):
        # URLの順番が偶数の場合かつ、現在の偶数が一番大きい場合
        if index % 2 == 0 and index > largest_odd_index:
            largest_odd_index = index
            largest_odd_value = index

    # 一番大きい偶数の順番を持つURLを取得
    if largest_odd_index != -1:
        largest_odd_url = backurl[largest_odd_index]
        print("一番大きい偶数の順番のURL:", largest_odd_url)
    else:
        print("条件を満たすURLが見つかりませんでした。")
        
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Postモデルと関連付け
            comment.published_date = timezone.now()
            comment.save()
            
            return redirect(largest_odd_url)
    else:
        form = CommentForm()
    return render(request, 'post_edit.html', {'form': form})

# コメントの削除ボタン
@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # コメントの削除処理
    if request.method == 'POST':
        comment.delete()

    # 削除後に戻るURLを取得し、リダイレクト
    referer = request.META.get('HTTP_REFERER', 'post_list')
    return redirect(referer)

@login_required
# 通塾時間変更用view
def change_day(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = ChangeDayForm(request.POST)
        if form.is_valid():
            studyday_type = form.cleaned_data['studyday_type']
            post.studyday_type = studyday_type  # studyday_typeのみを変更
            post.save()  # 保存
            return redirect('post_list')
    else:
        form = ChangeDayForm()
    
    return render(request, 'change_day.html', {'form': form})