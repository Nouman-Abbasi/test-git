# home/pagination_utils.py

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def paginate_queryset(queryset, page_number, page_size=None):
    """
    Paginate a queryset.
    
    :param queryset: The queryset to paginate
    :param page_number: The current page number
    :param page_size: The number of items per page. If None, uses default from settings.
    :return: A dictionary with paginated items and page information
    """
    if page_size is None:
        page_size = settings.PAGINATION_SETTINGS['DEFAULT_PAGE_SIZE']

    paginator = Paginator(queryset, page_size)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return {
        'items': page_obj.object_list,
        'page': page_obj.number,
        'total_pages': paginator.num_pages,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
    }
