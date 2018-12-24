from .models import Obj, Spec


def get_object_specs(object):
    return Spec.objects.filter(link__name=object.name)


def set_specs_unactual(object, date):
    get_object_specs(object).filter(date__lte=date, is_actual=True).update(is_actual=False)


def set_obj_for_deleting():
    for object in Obj.objects.filter(is_deleted=False):
        if object.spec_set.filter(is_actual=True).count() == 0:
            object.is_deleted=True
            object.save()



def delete_objects():
    Obj.objects.filter(is_deleted=True).delete()



# TODO Для существующей моделей, необходимо написать функции
# TODO (объект и характеристика, это модели в аппке):
# TODO
# TODO Принимает объект и возвращает все его актуальные характеристики.
# TODO Возвращает queryset c актуальными спеками на текущую дату.
# TODO Возвращает queryset объектов с актульными спеками.
# TODO Принимает объект и помечает спеки объектов как не актульные, для даты меньше указаной.
# TODO Помечать на удаление объекты у которых нет актуальных спек.
# TODO Удалять объекты которые помечены на удаление.
# TODO
