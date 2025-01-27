from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage
)


class HardLimitPagePaginator(Paginator):
    def page(self, number):
        try:
            number = self.validate_number(number)
        except PageNotAnInteger:
            number = 1
        except EmptyPage:
            number = 1 if number < 1 else self.num_pages
        return super().page(number)


class PaginationMixin:
    paginate_by = 5
    MIN_PER_PAGE = 3
    MAX_PER_PAGE = 10

    paginator_class = HardLimitPagePaginator

    def get_paginate_by(self, queryset=None):
        per_page = (
            self.request.GET.get("per_page")
            or self.request.session.get("per_page")
        )
        if per_page and per_page.isdigit():
            per_page = max(
                self.MIN_PER_PAGE,
                min(int(per_page), self.MAX_PER_PAGE)
            )
        else:
            per_page = self.paginate_by

        if self.request.session.get("per_page") != per_page:
            self.request.session["per_page"] = str(per_page)
        return per_page


class PaginationURLMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        per_page = self.get_paginate_by()

        context["per_page"] = per_page

        query_params = self.request.GET.copy()
        query_params["per_page"] = per_page
        if "page" in query_params:
            query_params.pop("page")
        context["query_string"] = query_params.urlencode()
        return context
