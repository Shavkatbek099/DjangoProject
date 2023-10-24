from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

admin.site.register([CategoryNewsTitle, NewsTitle,
                     EntertainmentPost, BusinessPost,
                     TravelPost, LifeStylePost,
                     CommentNewsTitle, Item,
                     MostPopularPost, FeaturedVideoPost,
                     TagsPost, LatestArticlesPost])


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
