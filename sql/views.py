from rest_framework import views, status, response
from sql.services import my_custom_sql, create_user
from sql.models import Company, Customer, Product
from django.shortcuts import render
from sql.forms import SqlForm


# Create your views here.
class TestApiView(views.APIView):

    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        query = request.data.get('test')
        result = my_custom_sql(query)
        print(result)
        create_user('student')
        return response.Response({'result': result}, status=status.HTTP_200_OK)


def sql_task(request, pk):
    form = SqlForm()
    if request.method == 'POST':
        form = SqlForm(request.POST)

        if form.is_valid():
            code_editor = form.cleaned_data['code_editor']
            print(code_editor)

    return render(request, 'sql-task.html', locals())
