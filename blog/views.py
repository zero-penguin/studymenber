from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.db.models import Q

def post_list(request):

    posts = Post.objects.all()
    error = ""
    sorted_posts = []
    sort_by = request.GET.get('sort_by', 'studyday_type')
    selected_studyday_type = request.GET.get('studyday_type_filter', '')  # 選択された学習日タイプを取得

    # 学習日タイプの選択肢
    studyday_type_choices = [
        ('火曜１７時', '火曜１７時'),
        ('火曜１８時', '火曜１８時'),
        ('水曜１７時', '水曜１７時'),
        ('水曜１８時', '水曜１８時'),
        ('金曜１７時', '金曜１７時'),
        ('金曜１８時', '金曜１８時'),
        ('土曜１０時', '土曜１０時'),
        ('土曜１１時', '土曜１１時'),
        ('土曜１３時', '土曜１３時'),
        ('土曜１４時', '土曜１４時'),
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
            Q(school__icontains=search_query)  # 学校で部分一致検索
        )
        
    elif search_query and not selected_studyday_type:
        posts = posts.filter(
            Q(name__icontains=search_query) |  # 名前で部分一致検索
            Q(school__icontains=search_query)  # 学校で部分一致検索
        )
    
    elif not search_query and selected_studyday_type:
        posts = sorted_posts
        # 検索がかけられていない時にnone値ではなくデフォルトメッセージを表示する
        search_query = ""
    else:
        error = "誰も居ませんでした、、"
        print(error)
        search_query = ""
        posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts': posts, 'sort_by': sort_by, 'studyday_type_choices': studyday_type_choices,'search_query': search_query, 'error': error})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})