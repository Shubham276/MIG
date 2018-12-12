from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def restaurant(request):
    if request.method == 'POST':
        name_form = NameForm(request.POST)
        emp_form = EmpForm(request.POST, request.FILES)
        if name_form.is_valid():
            print(name_form)
        if emp_form.is_valid():
            emp_form.save()
            return HttpResponse('<h1>Thank You</h1>')
        restaurant_name = request.POST['restaurant_name']
        street = request.POST['street']
        number = int(request.POST['number'])
        city = request.POST['city']
        zipcode = int(request.POST['zipcode'])
        state = request.POST['state']
        country = request.POST['country']
        telephone = request.POST['telephone']
        restaurant_save = Restaurant(name=restaurant_name, street=street, number=number, city=city, zipcode=zipcode,
                                     stateorProvince=state, country=country, telephone=telephone)
        restaurant_save.save()
        return redirect('/renderHTML')
    else:
        name_form = NameForm()
        emp_form = EmpForm()
    res = restaurant_data()
    return render(request, 'restaurant.html', {'restaurants': res, 'name_form': name_form, 'emp_form': emp_form})


def dish(request, restaurant_id):
    dish_data = Dish.objects.filter(restaurant=restaurant_id)
    if request.method == 'POST':
        dish_name = request.POST["dish_name"]
        description = request.POST["description"]
        price = request.POST["price"]
        pic = request.FILES["pic"]
        d = Dish(name=dish_name, description=description, price=price, image=pic,
                 restaurant=Restaurant.objects.get(id=restaurant_id))
        d.save()
        return redirect('/renderHTML/dish/'+str(restaurant_id))
    return render(request, 'dish.html', {'dishes': dish_data, 'restaurant_id': restaurant_id})


def review(request, dish_id):
    review_data = Review.objects.filter(dish=dish_id)
    if request.method == 'POST':
        choice = request.POST["choices"]
        comment = request.POST["comment"]
        r = Review(rating=choice, comment=comment)
        r.save()
        return redirect('/renderHTML/review/'+str(dish_id))
    # r = review_data()
    return render(request, 'review.html', {'reviews': review_data}, 'dish_id', dish_id)


# def review_data():
#     r = Review.objects.all()
#     return r


def restaurant_data():
    res = Restaurant.objects.all()
    return res


def delete_restaurant_data(request, restaurant_id):
    delete_restaurant = Restaurant.objects.get(id=restaurant_id)
    delete_restaurant.delete()
    return redirect('/renderHTML')


def delete_dish_data(request, pk, dish_id):
    # print(pk)
    delete_dish = Dish.objects.get(id=dish_id)
    delete_dish.delete()
    return redirect('/renderHTML/dish/' + str(pk))


def delete_review_data(request, pk, review_id):
    delete_review = Review.objects.get(id=review_id)
    delete_review.delete()
    return redirect('/renderHTML/review/' + str(pk))


def update_restaurant_data(request, restaurant_id):
    update_restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        restaurant_name = request.POST['restaurant_name']
        street = request.POST['street']
        number = int(request.POST['number'])
        city = request.POST['city']
        zipcode = int(request.POST['zipcode'])
        state = request.POST['state']
        country = request.POST['country']
        telephone = request.POST['telephone']
        Restaurant.objects.filter(id=restaurant_id).update(name=restaurant_name, street=street, number=number, city=city
                                                           , zipcode=zipcode, stateorProvince=state, country=country,
                                                           telephone=telephone)
        return redirect('/renderHTML')
    return render(request, "update_restaurant.html", {'restaurants': update_restaurant})


def update_dish_data(request, pk, dish_id):
    up = Dish.objects.get(id=dish_id)
    if request.method == 'POST':
        dish_name = request.POST["dish_name"]
        description = request.POST["description"]
        price = request.POST["price"]
        pic = request.FILES["pic"]
        print(pic)
        Dish.objects.filter(id=dish_id).update(name=dish_name, description=description, price=price, image=pic)
        return redirect('/renderHTML/dish/' + str(pk))
    return render(request, "update_dish.html", {'dishes': up})


def update_review_data(request, id):
    update = Review.objects.get(id=id)
    if request.method == 'POST':
        choice = request.POST["choices"]
        comment = request.POST["comment"]
        Review.objects.filter(id=id).update(rating=choice, comment=comment)
        return redirect('/renderHTML/review')
    return render(request, "update.html", {'review': update})


@login_required()
def show_data(request):
    data = Employee.objects.all()
    return render(request, 'show.html', {'employees': data})


def search(request):
    # print(search_box)
    if request.method == 'POST':
        search_box = request.POST['search_text']
    else:
        search_box = ''
    data = Employee.objects.filter(ename__icontains=search_box)
    return render(request, 'show.html', {'employees': data})


def delete_data(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    messages.success(request, f'Employee {id} has been deleted')
    return redirect('/renderHTML/show/')


def update_data(request, id):
    data = Employee.objects.get(id=id)
    emp = EmpForm(instance=data)
    messages.success(request, f'Employee {id} has been updated')
    return redirect('/renderHTML/')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            subject = 'Confirmation Mail'
            msg = 'Hello Dear, Thanks'
            send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
            User.objects.create_user(username=username, email=email,
                                     first_name=first_name, last_name=last_name,
                                     password=password)
            return HttpResponse('Thank You')
            # return redirect('/renderHTML/login/')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/renderHTML/show/')
        else:
            return HttpResponse('<h1>Invalid User</h1>')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'login.html')

