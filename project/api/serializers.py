from datetime import datetime

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.db.models import Count, Q, Sum

from newsapp.models import News, Category, Like

# сериализатор для модели News, описанный вручную
# (реализация внутренней логики сериализатора, унаследованного от ModelSerializer)
# class NewsSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     content = serializers.CharField()
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return News.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title')
#         instance.content = validated_data.get('content')
#         instance.category_id = validated_data.get('category_id')
#         instance.save()
#         return instance


class NewsSerializer(serializers.ModelSerializer):

    # скрытое автогенерируемое поле
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='title')
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    """
    SerializerMethodField определяет поле только для чтения,
    значение которого определяется с помощью указанного метода 
    """
    user_str = serializers.SerializerMethodField(method_name='get_user')
    image_path = serializers.SerializerMethodField(method_name='get_photo_url')
    likes_count = serializers.SerializerMethodField(method_name='get_likes_count')

    def get_likes_count(self, obj):
        filtered_news = Like.objects.filter(news=obj)
        filtered_news = filtered_news.annotate(count=Count('news'))
        filtered_news = filtered_news.aggregate(Sum('count'))
        return filtered_news['count__sum'] if filtered_news['count__sum'] else 0

    def get_user(self, obj):
        return f'{obj.user}'

    def get_photo_url(self, obj):
        # request = self.context.get('request')
        return obj.image.url if obj.image else ''

    class Meta:
        model = News
        # fields = '__all__' # ('title', 'content', 'category_id') # '__all__'
        exclude = ('is_published', 'image')
