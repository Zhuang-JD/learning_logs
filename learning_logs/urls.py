
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # ��ҳ
    path('', views.index, name='index'),
    
    #��ʾ���е�����
    path('topics/',views.topics,name='topics'),
    
    #�ض��������ϸҳ��
    path('topics/<topic_id>/',views.topic,name='topic'),

	#����������������ҳ
	path('new_topic/', views.new_topic, name='new_topic'),
	
	#�����������Ŀ��ҳ��
	path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
	
	#���ڱ༭��Ŀ��ҳ��
	path('edit_entry/<entry_id>/',views.edit_entry,name='edit_entry'),
]
