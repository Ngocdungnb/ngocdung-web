import mlab
from movie import Movie
from resource import Resource
from faker import Faker

faker = Faker("en_US")

# for _ in range(13):
#     print(faker.city())


mlab.connect()

# n = Resource.objects().with_id("5bf7fd9f5165d10c70d34d71")
# n.delete()

# r=Resource.objects().first()
# r.delete()

# movie_list = Movie.objects()
# for m in movie_list:
#     print (m.image, m.title, m.year, sep = "\n"



# resource_list = Resource.objects()
# for n in resource_list:
#     print(n.name, n.city, n.yob, n.height, n.weight, sep = "\n")

# m = Movie(title = "Phim Nguoi Nhon", year = 2018, image = "http://3.bp.blogspot.com/-6AUp-toxP5s/VE-HTTuY_7I/AAAAAAAAObA/ehrVzV9h5KY/s1600/nhung-hinh-anh-cuc-hai-huoc-26.jpg")
# m.save()
# a = Resource (name = " Ngoc Dung", city = " Ha Noi", yob = 1997, height = 170, weight = 60)
# b = Resource (name = " Ngoc An", city = " Ninh Binh", yob = 1997, height = 160, weight = 50)
# c = Resource (name = " Ngoc Khai", city = " Bac Ninh", yob = 1997, height = 180, weight = 65)
# # a.save()
# # b.save()
# # c.save()
from random import randint
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1970,2012)
#     height =  randint(150,200)
#     weight = randint(50,100)
#     r = Resource(name = name, city = city, yob = yob, height= height, weight = weight)
#     r.save()

# records = Resource.objects(height = 172)
# for i in records:
#     print(i.name)
#     print(i.city)

# print (len(records))
# for i in records:
#     print(i.city)
#     print(i.weight)
#     print(i.weight)

# records = Resource.objects (height__gt= 160, name__icontains = "Do")
# print (len(records))

# records = available
# for r in records:
#     r.update(set__available = False)

r = Resource.objects().with_id ("5bf80ce35165d11ed8ff1bf4")
r.update(set__available = True)
