from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from math import ceil, floor


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data, success=True, error=None, message=None):
        return Response(OrderedDict([
            ('success', success),
            ('error', error),
            ('message', message),
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('total_pages', self.page.paginator.num_pages),
            ('per_page', self.page.paginator.per_page),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class BaseLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 1000

    def get_paginated_response(self, data, success=True, error=None, message=None):
        return Response(OrderedDict([
            ('success', success),
            ('error', error),
            ('message', message),
            ('count', self.count),
            ('current', floor(self.offset / self.limit) + 1),
            ('total_pages', ceil(self.count / self.limit)),
            ('per_page', self.limit),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
