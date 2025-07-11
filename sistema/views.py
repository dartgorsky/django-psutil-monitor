from django.shortcuts import render
import psutil
import platform

def index(request):
    try:
        
        cpu_uso= psutil.cpu_percent(interval=1)

        memoria_ram= psutil.virtual_memory()
        ram_total= round(memoria_ram.total/(1024**3),2) 
        ram_usada= round(memoria_ram.used/(1024**3),2)
        ram_porcentaje= memoria_ram.percent

        disco_duro= psutil.disk_usage('/')
        disco_total= round(disco_duro.total/(1024**3),2)
        disco_usada= round(disco_duro.used/(1024**3),2)
        disco_libre= round(disco_duro.free/(1024**3),2)

        cantidad_de_nucleos= psutil.cpu_count()
        sistema_operativo= platform.system()

        context= {
            'cpu_uso': cpu_uso,
            'ram_total': ram_total,
            'ram_usada': ram_usada,
            'ram_porcentaje': ram_porcentaje,
            'disco_total': disco_total,
            'disco_usada': disco_usada,
            'disco_libre': disco_libre,
            'cantidad_de_nucleos': cantidad_de_nucleos,
            'sistema_operativo': sistema_operativo,
        }

    except Exception as e:
        context = {'error': str(e)}

    return render(request, 'sistema/index.html', context)
