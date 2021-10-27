from apps.accounts.models import Customer, Gender

g1 = Gender(gender='Male')
g2 = Gender(gender='Female')
g1.save()
g2.save()

c1 = Customer(gender=Gender.objects.get(gender='Male'), name='Bob')
c1.save()
