# xellshop/repositories/base_repository.py

class BaseRepository:
    model = None  # Конкретна модель задається в насліднику

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, pk):
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        obj.save()
        return obj

    def update(self, obj):
        obj.save()
        return obj

    def delete(self, obj):
        obj.delete()