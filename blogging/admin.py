from django.contrib import admin

from blogging.models import Post, Category


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "modified_date"
    inlines = [
        CategoriesInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
