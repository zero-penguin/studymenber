from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from .forms import CommentForm


def post_list(request):

    posts = Post.objects.all()
    comments = Comment.objects.all().order_by('-id')
    error = ""
    sorted_posts = []
    sort_by = request.GET.get('sort_by', 'studyday_type')
    selected_studyday_type = request.GET.get('studyday_type_filter', '')  # 選択された学習日タイプを取得
    current_time = timezone.now()  # 現在の日時を取得
    current_time = current_time - timedelta(seconds=50)

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
            error = "誰も居ませんでした"
        
    elif search_query and not selected_studyday_type:
        posts = posts.filter(
            Q(name__icontains=search_query) |  # 名前で部分一致検索
            Q(school__icontains=search_query) |  # 学校で部分一致検索
            Q(katakana__icontains=search_query) # カタカナで部分一致
        )
        if not posts:
            error = "誰も居ませんでした"
    
    elif not search_query and selected_studyday_type:
        posts = sorted_posts
        # 検索がかけられていない時にnone値ではなくデフォルトメッセージを表示する
        search_query = ""

        if not posts:
            error = "誰も居ませんでした"

    else:
        search_query = ""
        posts = []

        if not posts:
            error = "<img src='../static/image/work/attention.png' width='80%'>"

    
    

    return render(request, 'post_list.html', {
        'posts': posts,
        'sort_by': sort_by,
        'studyday_type_choices': studyday_type_choices,
        'search_query': search_query,
        'error': error,
        'comments':comments,
        'current_time': current_time,  # 現在の日時をコンテキストに追加
        })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('-id')[1:]
    ratest_comment = Comment.objects.filter(post_id=pk).last()
    return render(request, 'post_detail.html', {'post': post,'comments': comments,'ratest_comment':ratest_comment})

def post_new(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Postモデルと関連付け
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'post_edit.html', {'form': form})