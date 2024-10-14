from django.shortcuts import render,redirect
from django.db.models import Sum
from django.shortcuts import render
from .forms import vehicleForm,CategoryForm,VehicleSearchForm
from .models import Category, AddVehicle
from django.contrib.auth import logout
from django.contrib import messages
from .models import Admin
from django.contrib.auth.hashers import check_password,make_password

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Fetch the admin user from the Admin model
            admin_user = Admin.objects.get(username=username)

            # Verify password
            if check_password(password, admin_user.password):  # Compare the entered password with the hashed one
                # Store admin user in the session
                request.session['admin_id'] = admin_user.id
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'adminlogin.html')



# def adminlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password')
        
#     return render(request, 'adminlogin.html')


# # views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from .forms import LoginForm

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard URL
#             else:
#                 # Invalid credentials
#                 return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
#     else:
#         form = LoginForm()
    
#     return render(request, 'login.html', {'form': form})







def logout_view(request):
    logout(request)
    return redirect('adminlogin')



def dashboard(request):
    vehicles_parked = AddVehicle.objects.count()
    departed_vehicles = AddVehicle.objects.filter(status='Departed').count() 
    available_categories = Category.objects.count()
    total_earnings = AddVehicle.objects.all().aggregate(total=Sum('parking_charge'))['total']
    total_records = AddVehicle.objects.count()
    total_parking_slots = 100  
    context = {
        'vehicles_parked': vehicles_parked,
        'departed_vehicles': departed_vehicles,
        'available_categories': available_categories,
        'total_earnings': total_earnings,
        'total_records': total_records,
        'total_parking_slots': total_parking_slots,
    }

    return render(request, 'dashboard.html', context)
def addvehicle(request):
    form = vehicleForm()
    if request.method =='POST':
        form =vehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')#url patterns  name=showproducts


    context={
        'form':form
    }
    return render(request, 'vehicleentry.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'category_list.html', {'form': form})
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def search_vehicle(request):
    form = VehicleSearchForm()
    vehicles = None

    if request.method == 'GET' and 'vehicle_number' in request.GET:
        form = VehicleSearchForm(request.GET)
        if form.is_valid():
            vehicle_number = form.cleaned_data['vehicle_number']
            vehicles = AddVehicle.objects.filter(vehicle_no=vehicle_number)
        else:
            messages.error(request, 'Invalid vehicle number')

    context = {
        'form': form,
        'vehicles': vehicles,
    }
    return render(request, 'search_vehicle.html', context)



def account_settings(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        # Get the logged-in admin (assuming admin ID is stored in session)
        admin_id = request.session.get('admin_id')
        if not admin_id:
            messages.error(request, 'You are not logged in.')
            return redirect('adminlogin')
        
        try:
            admin_user = Admin.objects.get(pk=admin_id)
            
            # Check if the current password matches
            if not check_password(current_password, admin_user.password):
                messages.error(request, 'Current password is incorrect.')
                return redirect('account_settings')

            # Check if the new password and confirm password match
            if new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
                return redirect('account_settings')

            # Update the password
            admin_user.password = make_password(new_password)
            admin_user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('dashboard')

        except Admin.DoesNotExist:
            messages.error(request, 'Admin not found.')
            return redirect('adminlogin')

    return render(request, 'account_settings.html')


def num_parking_slots(request):
   slots_area = Parkingslots.objects.all()
   return render(request,'parking_slot.html',{'slot_list':slots_area})
