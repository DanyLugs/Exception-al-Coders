from django.contrib.auth.mixins import UserPassesTestMixin

class AdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').count() > 0

class RepartidorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='repartidor').count() > 0

class ClienteMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='cliente').count() > 0
