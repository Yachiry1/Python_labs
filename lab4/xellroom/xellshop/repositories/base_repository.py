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
        try:
            if obj:
                obj.delete()
                return True
            return False
        except Exception as e:
            print(f"Помилка при видаленні: {e}")
            return False

    def delete_by_id(self, pk):
        obj = self.get_by_id(pk)
        if obj:
            obj.delete()
            return True
        return False