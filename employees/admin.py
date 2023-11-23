from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from openpyxl.reader.excel import load_workbook
from hr_sphere.forms import XlsxImportForm
import datetime as dt


from .models import *

admin.site.register(Organization)
# admin.site.register(Subdivision)
admin.site.register(Position)
admin.site.register(Employee)

class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'parent_subdivision', 'org_id')
    change_list_template = 'hr_sphere/subdivision_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        # Добавляем URL нашего обработчика импорта.
        my_urls = [
            path('import-records-from-xlsx/', self.import_records_from_xlsx),
        ]
        return my_urls + urls

    def import_records_from_xlsx(self, request):
        context = admin.site.each_context(request)
        if request.method == 'POST':
            xlsx_file = request.FILES['xlsx_file']

            workbook = load_workbook(filename=xlsx_file, read_only=True)
            worksheet = workbook.active

            # Читаем файл построчно и создаем объекты.
            records_to_save = []
            for row in worksheet.rows:
                if not Subdivision.objects.filter(code=row[0].value).exists():
                    new_obj = Subdivision(
                        code=row[0].value, 
                        name=row[1].value,  
                        org_id=Organization.objects.get(id=1),
                    )
                    records_to_save.append(new_obj)
            Subdivision.objects.bulk_create(records_to_save)
            
            for row in worksheet.rows:
                if Subdivision.objects.filter(code=row[0].value).exists():
                    cur_obj = Subdivision.objects.get(code=row[0].value)
                    if Subdivision.objects.filter(code=row[2].value).exists():
                        cur_obj.parent_subdivision = Subdivision.objects.get(code=row[2].value)
                    cur_obj.save()

            self.message_user(request, f'Импортировано строк: {len(records_to_save)}.')
            return redirect('/admin/employees/subdivision/')

        context['form'] = XlsxImportForm()
        return render(request, 'hr_sphere/add_records_form.html', context=context)


admin.site.register(Subdivision, SubdivisionAdmin)
