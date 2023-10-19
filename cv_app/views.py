from django.shortcuts import render


def index_views(request):
    # chon template ltr bood english por kardam va az yek seri template haye amadeye resume estefade kardam agar eshkal nadare.information sample
    # https://resumeworded.com/ , https://www.resumebuilder.com/
    context = {
        'fullname': 'Ehsan Sedigh',
        'skils': 'Web Developer, Graphic Designer,  Photographer',
        'about': 'An innovative programmer with two years of experience, specializing in UX design, Python, JavaScript, and Object-oriented Design (OOD). Adept at performing quality assurance (QA) reviews and identifying root causes of complex technical issues.',
        'age': '34',
        'email': 'ehsan.sedigh@gmail.com',
        'phone': '09123456789',
        'address': 'Karaj , jahanshahr , golha no 34',
        'language': 'Persian , English',
        # ajib bood.har siti raftam lorem english nadashtan va hamintori latina bood !
        'lorem': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Egestas purus viverra accumsan in nisl nisi Arcu cursus vitae congue mauris rhoncus aenean vel elit scelerisque In egestas erat imperdiet sed euismod nisi porta lorem mollis Morbi tristique senectus et netus Mattis pellentesque id nibh tortor id aliquet lectus proin Sapien faucibus et molestie ac feugiat sed lectus vestibulum'

    }
    return render(request, "index.html", context)
