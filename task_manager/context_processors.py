from .models import Category

def pinned_categories(request):
    if request.user.is_authenticated:
        pinned = Category.objects.filter(user=request.user, is_pinned=True)
        return {"pinned_categories": pinned}
    return {}