from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# 使うルータークラスのインスタンスを定義し、register()でURLのルートに当たる部分(例えば~/usersと/users/<int:pk>/のようなルーティングを作るのであればr`users`と定義する)と使うViewSetを引数に指定する。
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # 基本はこれだけでいい
    path('', include(router.urls)),
    # 認証用のルーティングはCRUDの外のことなので個別に設定
    path('api-auth/', include('rest_framework.urls')),
]
