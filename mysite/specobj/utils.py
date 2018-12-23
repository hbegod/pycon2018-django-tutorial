from .models import Obj, Spec



def get_object_specs(object):
    #  Person.object - менеджер модели
    #  qs_person - это QuerySet
    qs_specs = Obj.


    
    qs_person = Person.objects.filter(last_name__contains=surname)
    try:
        #  person - инстанс модели Рerson.
        person =  qs_person.get(first_name__contains=name)
        # обработка отсутствия записи в базе
    except Person.DoesNotExist as e:
        raise VseSlomalosExeption("Это кто вообще?")
    except Person.MultipleObjectsReturned as e:
        raise VseSlomalosExeption("А что их несколько?")
    return





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
