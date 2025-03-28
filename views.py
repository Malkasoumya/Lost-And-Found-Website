from django.shortcuts import render,redirect
from lost.models import itemlost
from lost.models import itemfound
from users.models import itemfoundfull,itemlostfull
#from .forms import lostform , foundform,RegistrationForm
from .forms import lostform , foundform
#from.models import RegistrationData 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

from users.forms import lostfullform, foundfullform

from users.models import Profile

from django.core.paginator import Paginator
@login_required
def lost_view(request,*args,**kwargs):
    obj=itemlost.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }
    return render(request,"lostlist.html",context)
@login_required
def lost_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict1=request.POST.copy()
        dict1['username']=request.user.username
        form=lostform(dict1 or None)
        if form.is_valid():
            formfull=lostfullform(dict1 or None)
            formfull.save()
            form.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form=lostform()
    context={
        'form':form
        }
    return render(request,"lost.html",context)
@login_required
def found_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict2=request.POST.copy()
        dict2['username']=request.user.username
        form1=foundform(dict2 or None,user=request.user)
        if form1.is_valid():
            formfull1=foundfullform(dict2 or None)
            formfull1.save()
            form1.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form1=foundform(user=request.user)
    context={
        'form1':form1
        }
    
    return render(request,"found.html",context)
@login_required
def found_view(request,*args,**kwargs):
    obj=itemfound.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }

    return render(request,"foundlist.html",context)





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import itemfound  # Import your model
from .forms import ClaimForm  # Import your claim form
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
@login_required
def available_items(request):
    
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        
        if form.is_valid():
            
            item_id = request.POST.get('item_id')
            
            try:
                item = itemfound.objects.get(id=item_id)
                key_details = form.cleaned_data['key_details']
                claimant_name = request.user.username
                claimant_email = request.user.email
                posted_user = User.objects.get(username = item.username)
                posted_user_email = posted_user.email
                
                
                
                
                poster_email = posted_user_email # Assuming 'owner' is a ForeignKey to User

                # Send email to the poster
                send_mail(
                    'Item Claim Notification',
                    f'Hello,\n\nYour item "{item.product_title}" has been claimed.\n\n'
                    f'Claimant Name: {claimant_name}\n'
                    f'Claimant Email: {claimant_email}\n'
                    f'Key Details: {key_details}',
                    'kranthisidda3@gmail.com',  # Replace with your sender email
                    [poster_email],
                    fail_silently=False,
                )

                messages.success(request, 'Your claim has been submitted and the poster has been notified.')
                
                return redirect('available_items')  # Redirect to the same or another page
            except itemfound.DoesNotExist:
                messages.error(request, 'Item not found.')
        
    else:
        form = ClaimForm()

        items = itemfound.objects.all()  # Retrieve available items
        context = {
            'items': items,
            'form': form,
        }
        return render(request, 'available_items.html', context)
