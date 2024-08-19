from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import blog, Comment , User
from .forms import blogForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import AdminSignupForm, AdminLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib import messages
from .forms import EditUserForm
from .forms import CustomLoginForm

# Helper function to check if the user is an admin
def user_is_admin(user):
    return user.is_superuser

# Create your views here.
def index(request):
    latest_posts = blog.objects.all().order_by('-created_at')[:6]
    return render(request, 'my_app/index.html', {'latest_posts': latest_posts})

def all_posts(request):
    posts = blog.objects.all().order_by('-created_at')
    return render(request, 'my_app/all_posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(blog, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail',  pk=pk)
        else:
            return redirect('login')  # Redirect to login if user is not authenticated
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'my_app/post_detail.html', context)

# @login_required
# @user_passes_test(user_is_admin)
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = blogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show')
        else:
            form = blogForm()
        return render(request, 'admin/add_post.html', {'form': form})

# show page
# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def show(request):
    if request.user.is_authenticated:
        Posts = blog.objects.all()
        return render(request, "admin/view.html", {'Posts': Posts})

# edit page
@login_required
@user_passes_test(user_is_admin)
def edit(request, id):
    if request.user.is_authenticated:
        Posts = blog.objects.get(id=id)
        return render(request, 'admin/edit.html', {'Posts': Posts})

@login_required
@user_passes_test(user_is_admin)
def update(request, id):
    if request.user.is_authenticated:
        posts = get_object_or_404(blog, id=id)
        if request.method == 'POST':
            form = blogForm(request.POST, instance=posts)
            if form.is_valid():
                    form.save()
                    return redirect("show")
        else:
            form = blogForm(instance=posts)

        context = {
            'form': form,
            'posts': posts
        }
        return render(request, 'admin/edit.html', context)

@login_required
@user_passes_test(user_is_admin)
def delete_post(request, id):
    if request.user.is_authenticated:
     posts = get_object_or_404(blog, id=id)
     if request.method == 'POST':
         posts.delete()
         return redirect("show")
     return render(request, 'admin/delete.html', {'posts': posts})

def test_ckeditor(request):
    post = blog.objects.first()
    return render(request, 'my_app/test_ckeditor.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'my_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                # return redirect('profile')
                return render(request, 'my_app/login.html', {'form': form, 'redirect': True})
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'my_app/login.html', {'form': form})

@login_required
def user_dashboard(request):
    
    if request.user.is_authenticated:
        # return redirect('login_view')
        user_comments = request.user.comment_set.all()
        
    try:
        # Try to get the user from the database
        user = get_object_or_404(User, id=request.user.id)
    except:
        # If the user is not found, redirect to the registration page
        return render(request, 'my_app/register.html')
        # redirect('register')
    # context = {
    #     'user': user,
    # }
    return render(request, 'my_app/user_dashboard.html', {'comments': user_comments, 'user':user})

@login_required
def profile(request):
    if request.user.is_authenticated:
        return redirect('login_view')
    try:
        # Try to get the user from the database
        user = get_object_or_404(User, id=request.user.id)
    except:
        # If the user is not found, redirect to the registration page
        return render('register')
    context = {
        'user': user,
    }
    return render(request, 'my_app/user_dashboard.html', context)

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'admin/signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Login successful. Redirecting to the dashboard...')
                # return redirect('admin_dashboard')
                return render(request, 'admin/login.html', {'form': form, 'redirect': True})

            else:
                messages.error(request, 'You do not have admin privileges.')
            
            
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AdminLoginForm()
    
    return render(request, 'admin/login.html', {'form': form})


def admin_dashboard(request):
    if request.user.is_authenticated:
        post_count = blog.objects.count()
        comment_count = Comment.objects.count()
        users_count = User.objects.count()
        posts = blog.objects.all()
        users = User.objects.all()
        comments = Comment.objects.all()  # Retrieve all comments

        if request.method == 'POST':
            if 'delete' in request.POST:
                post_id = request.POST.get('delete')
                post = get_object_or_404(blog, id=post_id)
                post.delete()
                return redirect('admin_dashboard')

        context = {
            'post_count': post_count,
            'comment_count': comment_count,
            'users_count': users_count,
            'posts': posts,
            'users': users,
            'comments': comments, 
            'form': blogForm(),
        }
        return render(request, 'admin/admin_dashboard.html', context)
    return redirect('admin_login')

# def view_user(request):
#     if request.user.is_authenticated:
#         users = User.objects.all()
#         # context = {
#         #         'users': users,
#         # }
#     #  return render(request, 'admin/view_users.html', context)
#     return render(request, 'admin/view_users.html', {'users': users})

# @login_required
def view_user(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'admin/view_users.html', context)


def edit_user(request, id):
    if request.user.is_authenticated:
        user_detail = get_object_or_404(User, id=id)
        
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user_detail)
            if form.is_valid():
                user = form.save()
                # Logout the user if they remove themselves from staff or admin
                logout(request)
                
                # Check if the current user is changing their own status
                if request.user.id == user.id:
                    if not user.is_staff or not user.is_superuser:
                        messages.success(request, 'Your profile was updated, and you have been logged out due to permission changes.')
                        return redirect('admin_login')  # Redirect to the login page

                messages.success(request, 'User details updated successfully.')
                return redirect('edit_user', id=id)
        else:
            form = EditUserForm(instance=user_detail)
        
        return render(request, 'admin/edit_user.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to edit users.')
        return redirect('admin_login')

def delete_users(request, id):
    if request.user.is_authenticated:
        user_detail = get_object_or_404(User, id=id)
        if request.method == 'POST':
            user_detail.delete()
            # if request.user == user_to_delete:
            logout(request)
            messages.success(request, 'You have successfully deleted a user profile.')
            return redirect('view_user')
        else:
            messages.success(request, 'sucess')
        
        return render(request, 'admin/delete_user.html', {'user_detail':user_detail})
        
    
    else:
        messages.error(request, 'You must be logged in to edit users.')
        return redirect('admin_login')
        

def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save() 
            return redirect('comments')
        else:
            print("Form errors:", form.errors)  
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'admin/edit_comment.html', {'form': form, 'comment': comment})

def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect after updating
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'my_app/edit_comment.html', {'form': form, 'comment': comment})

def comments(request):
    comments = Comment.objects.all()  # Retrieve all comments
    context = {
        'comments': comments,  # Add comments to context
        'form': blogForm(),
    }
    return render(request, 'admin/comments.html', context)


@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments')
    return render(request, 'admin/delete_comment.html', {'comment': comment})

@login_required
def settings(request):
    return render(request, 'admin/settings.html')

def admin_logout(request):
    if request.user.is_staff:  # Ensure only admin can use this logout
        logout(request)
    return redirect('admin_login')  # Redirect to admin login after logout
    # return redirect('user_dashboard')  # Redirect non-admin users to user dashboard

def user_logout(request):
    logout(request)
    return redirect('login_view')  # Redirect to user login after logout



def test(request):
    return render(request, 'user/test.html')