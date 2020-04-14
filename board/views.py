from math import ceil
from board.models import Board
from django.shortcuts import redirect, render
from django.db.models import Q
from django.utils import timezone as dtimezone


def show_list(request):
    page = request.GET.get('pg', 1)
    list_count = 12

    if int(page) < 1:
        return redirect('show_list')

    current_page = int(page) - 1
    start_at = current_page * list_count
    end_at = start_at + list_count

    if request.user.is_active:
        q = Q(created_at__lte=dtimezone.now())
    else:
        q = Q(status='1normal') & Q(created_at__lte=dtimezone.now())

    total = Board.objects.filter(q).count()
    lists = Board.objects.filter(q).order_by('-created_at')

    index_total = int(ceil(float(total) / list_count))
    index_begin = (int((current_page / list_count))) * list_count + 1
    index_end = (int((current_page / list_count))) * list_count + list_count

    mindex_end = index_total

    if index_end - index_begin >= list_count:
        index_end = index_begin + list_count - 1

    mindex_begin = int((current_page / list_count) * list_count + 1)
    if mindex_end - mindex_begin >= list_count:
        mindex_end = mindex_begin + list_count - 1

    return render(request,
                  'board/index.html',
                  {
                      'lists': lists,
                      'total': total,
                      'page': current_page + 1,
                      'index_begin': index_begin,
                      'index_end': index_end + 1,
                      'mindex_begin': mindex_begin,
                      'mindex_end': mindex_end + 1,
                      'index_total': index_total,
                      "list_count": list_count,
                      "path": "media"
                  }
                  )