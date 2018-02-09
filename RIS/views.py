from django.shortcuts import render
from django.http import HttpResponse
from .forms import ResearchForm,fordtp
from .models import List_of_Res



id_list = []
def RIS_Home(request):
	return render(request,'RIS/RIS_Home.html')

def Add_Res(request):
	if request.method=='POST':
		form = ResearchForm(request.POST)
		dtp = fordtp()
		if form.is_valid:
			resAdd_save=form.save(commit=False)
			resAdd_save.save()

	else:
		form = ResearchForm()
	args = {'form':form,'dtp':fordtp}
	return render(request,'RIS/RIS_Add-Edit.html',args)
def View_Res(request):
	researches = List_of_Res.objects.all()
	args = {
		'researches':researches,
		'id_list': id_list
	}
	return render(request,'RIS/RIS_TableView.html', args)

def Edit_Res(request):
	if request.method=='GET':
		form = ResearchForm()
		model = List_of_Res.objects.get(pk=request.GET['res'])
		if form.is_valid():
			form.fields['prog_title'].initial = model.prog_title
			form.fields['proj_title'].initial = model.proj_title
			form.fields['stud_title'].initial = model.stud_title
			form.fields['prog_lead'].initial = model.prog_lead
			form.fields['stud_lead'].initial = model.stud_lead
			return render(request, 'RIS/RIS_EDIT.html', {'form':form})
	else:
		form = ResearchForm(request.POST)
		nModel = List_of_Res.objects.get(prog_title=request.POST.get('prog_title'))
		nModel.prog_title=form['prog_title'].value()
		nModel.proj_title=form['proj_title'].value()
		nModel.stud_title=form['stud_title'].value()
		nModel.prog_lead=form['prog_lead'].value()
		nModel.stud_lead=form['stud_lead'].value()
		if form.is_valid():
			nModel.save()
			return render(request, 'RIS/RIS_Home.html')
	#if request.method=='POST':
	#	selected_res = Researches.objects.get(pk=request.POST['res'])
	#	selected_res.prog_title = "ok na putang ina"
	#	selected_res.save()

	#return render(request, 'RIS/RIS_Home.html')
def NEdit_Res(request):
	if request.method=='GET':
		selected_res = List_of_Res.objects.get(pk=request.GET['res'])
		return render(request, 'RIS/RIS_EDIT.html', {'selected_res': selected_res})
	else:
		selected_res = List_of_Res.objects.get(pk=request.POST['res_id'])

		selected_res.prog_title= request.POST.get('res_progT')
		selected_res.proj_title= request.POST.get('res_projT')
		selected_res.stud_title = request.POST.get('res_studT')
		selected_res.prog_lead = request.POST.get('res_progL')
		selected_res.stud_lead= request.POST.get('res_studL')
		selected_res.clean()	
		selected_res.save()
		return render(request, 'RIS/RIS_Home.html')
def Delete_Res(request):
	if request.method=='POST':
		delete_selected = List_of_Res.objects.get(pk=request.POST['res'])
		delete_selected.delete()
	return render(request, 'RIS/RIS_Home.html')

def NAdd_Res(request):
	return render(request, 'RIS/RIS_Home.html')

