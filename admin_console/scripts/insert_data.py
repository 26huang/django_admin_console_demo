from apps.accounts.models import Customer, Gender

def add_gender_lookup(gender_list):
    for gender in gender_list:
        try:
            g = Gender(gender=gender)
            g.save()
        except BaseException as e:
            print(e)

gender_list = ['Male', 'Female']
add_gender_lookup(gender_list)


c1 = Customer(gender=Gender.objects.get(gender='Male'), name='Bob')
c1.save()


def add_customer(name, gender):
    try:
        if Customer.objects.filter(gender=Gender.objects.get(gender=gender), name=name).exists():
            return 'Record already exists'
        else:
            gender_id = Gender.objects.get(gender=gender)
            c = Customer(gender=gender_id, name=name)
            c.save()
            return 'Customer {} has been added.'.format(name)

    except BaseException as e:
        g = Gender(gender=gender)
        g.save()
        add_customer(name, gender)
        return e


add_customer('Bao', 'Female')
add_customer('Bao', 'Unicorn')
add_customer('Bao', 'Wizard')

