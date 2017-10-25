from ..models import Post
from django import template

register = template.Library()

@register.inclusion_tag('index.html')
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
