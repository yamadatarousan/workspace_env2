# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    # ホーム
    url(r'^home/$', views.home, name='home'),
    # マイペ
    url(r'^mypage/$', views.mypage, name='mypage'),
    # 同じものを利用
    url(r'^session/$', views.session, name='session'),
    # お気に入りの感想
    url(r'^favorite/$', views.favorite, name='favorite'),
    # 相性
    url(r'^match/$', views.match, name='match'),
    # その他
    url(r'^other/$', views.other, name='other'),
    # 書籍
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除
    # 感想
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.ImpressionList.impression_edit, name='impression_add'),        # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.ImpressionList.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.ImpressionList.impression_del, name='impression_del'),   # 削除
)