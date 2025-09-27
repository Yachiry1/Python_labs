class Category:
    def __init__(self, name,description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    def display_info(self):
        return f"Категорія: {self.__name}, опис: {self.__description}"

    def update_description(self, new_desc):
        self.__description = new_desc
        return f"Опис категорії '{self.__name}' оновлено"

    @staticmethod
    def category_type():
        return "Основна категорія"

class ElectronicsCategory(Category):
    def __init__(self, name, description, warranty_info):
        super().__init__(name, description)
        self.warranty_info = warranty_info

    def display_info(self):
        return f"{super().display_info()}, гарантія: {self.warranty_info}"

class DiscountMixin:
    def apply_discount(self, percent):
        if not (0 < percent < 100):
            raise ValueError("Відсоток знижки має бути між 0 та 100")
        return f"Знижка {percent}% застосована!"

class ClothingCategory(Category, DiscountMixin):
    def __init__(self, name, description, size_range):
        super().__init__(name, description)
        self.size_range = size_range

    def display_info(self):
        return f"{super().display_info()}, розміри: {self.size_range}"

if __name__ == "__main__":
    electronics = ElectronicsCategory("Смартфони", "Мобільні телефони та аксесуари", "1 рік гарантії")
    clothing = ClothingCategory("Футболки", "Одяг для чоловіків та жінок", "S-XL")

    print(electronics.display_info())
    print(clothing.display_info())

    clothing.update_description("Новий опис категорії одягу")
    print(clothing.display_info())

    print(clothing.apply_discount(20))

    print(Category.category_type())
    print(ElectronicsCategory.category_type())
