from utils.paginations import BasePagination


class BooksPagination(BasePagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
