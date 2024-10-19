from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AuthorMixin:

    def get_queryset(self):

        qs = super().get_queryset()
        return qs.select_related("message").filter(author=self.request.user.pk)
