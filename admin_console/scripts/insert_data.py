from apps.accounts.models import Customer, Gender, ZipCode, Status

# Insert lookup tables
def add_gender_lookup(gender_list):
    for gender in gender_list:
        try:
            g = Gender(gender=gender)
            g.save()
        except BaseException as e:
            print(e)

gender_list = ['Male', 'Female']
add_gender_lookup(gender_list)


# Add zip code lookup
def add_zip_lookup(zip_list):
    for zip in zip_list:
        try:
            g = ZipCode(zip_code=zip)
            g.save()
        except BaseException as e:
            print(e)

zip_list = ['11111', '22222']
add_zip_lookup(zip_list)


# Add customers (many to one relationship)
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

# Add active status (many to many relationship)
def add_status(name, gender, zip_code, status):
    gender_id = Gender.objects.get(gender=gender)
    customer = Customer.objects.get(gender=gender_id, name=name)
    zip_code = ZipCode.objects.get(zip_code=zip_code)
    status = Status(customer=customer, zip_code=zip_code, active=status)
    status.save()


add_status('Bao', 'Unicorn', '11111', True)


