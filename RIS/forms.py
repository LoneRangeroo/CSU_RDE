from django import forms
from .models import List_of_Res

class fordtp(forms.Form):
	month_choices=(
		('JAN','January'),
		('FEB','February'),
		('MAR','March'),
		('APR','April'),
		('MAY','May'),
		('JUN','June'),
		('JUL','July'),
		('AUG','August'),
		('SEP','September'),
		('NOV','November'),
		('DEC','December'),
		)
	day_choices=(('1','1'))
	year_choices=[]
	for yyy in range(1990,2099):
		year_choices.append(str(yyy))
	month = forms.ChoiceField(choices = month_choices)
	year = forms.ChoiceField(choices = year_choices)
	day = forms.ChoiceField(choices = day_choices)
class ResearchForm(forms.ModelForm):
	class Meta:
		model = List_of_Res
		fields={
			'prog_title',
			'proj_title',
			'stud_title',
			'prog_lead',
			'stud_lead',
			'co_res',
			'res_site',
			'campus',
			'category_res',
			'classif_res',
			'amt_granted',
			'date_started',
			'res_status',
			'date_completed',
			'res_SF',
			'res_pubstat',
			'res_JN',
			'res_JV',
			'date_pub',
			'res_iprstat',
			'apptype',
			'date_appl',
			'date_pprv',
			'app_pending',
			'res_abs'
		}
		widgets = {
		'prog_title': forms.TextInput(),
		'proj_title': forms.TextInput(),
		'stud_title': forms.TextInput(),
		'prog_lead': forms.TextInput(),
		'stud_lead': forms.TextInput(),
		'co_res': forms.Textarea(),
		'res_site': forms.Textarea(),
		'campus': forms.RadioSelect(),
		'category_res': forms.RadioSelect(),
		'classif_res': forms.RadioSelect(),
		'amt_granted': forms.TextInput(),
		'date_started': forms.DateInput(),
		'res_status': forms.RadioSelect(),
		'date_completed': forms.DateInput(),
		'res_SF': forms.CheckboxSelectMultiple(),
		'res_pubstat': forms.RadioSelect(),
		'res_JN': forms.TextInput(),
		'res_JV': forms.TextInput(),
		'date_pub': forms.DateInput(),
		'res_iprstat':forms.RadioSelect(),
		'apptype':forms.RadioSelect(),
		'date_appl':forms.DateInput(),
		'date_pprv':forms.DateInput(),
		'app_pending': forms.RadioSelect(),
		'res_abs': forms.Textarea()
		}


#class CustomeResForm(forms.ModelForm):
#	class Meta:
#		model = List_of_Res
#	Yes_no_Choices = ('YES','NO')
#	Stat_choices = ('Completed','On-Going')
#	Campus_choices = (
#		'Aparri',
#		'Lasam',
#		'Lal-lo',
#		'Sanchez Mira',
#		'Carig',
#		'Andrews',
#		'Piat'
#		)
#	Category_choices = (
#		'Basic',
#		'Applied',
#		'Pilot Testing',
#		'Technology Promotion / Commercialization'
#		)
#	Classification_choices = (
#		'Agriculture',
#		'Biotechnology',
#		'ICT',
#		'Health Products',
#		'Alternative Energy',
#		'Climate Change',
#		'Environment',
#		'Socio-economic',
#		'Natural Products',
#		'Other'
#		)
#	Source_fund_choices = (
#		'CSU',
#		'CHED',
#		'DA-BAR',
#		'DOST',
#		'PCCARRD',
#		'PCIERD',
#		'PCHRD',
#		'DA',
#		'Other'
#		)
#	IPR_Type_choices = (
#		'Patent',
#		'Utility Model',
#		'Trademark/Tradename',
#		'Copyright'
#		'Other'
#		)
#	progT = forms.CharField(max_length=1000)
#	projT = forms.CharField(max_length=1000)
#	studT = forms.CharField(max_length=1000)
#	progL = forms.CharField(max_length=1000)
#	studL = forms.CharField(max_length=1000)
#	co_res = forms.CharField(help_text="One name per line", widget=forms.Textarea)
#	res_site = forms.CharField(help_text="One site per line",widget=forms.Textarea)
#	campus = forms.ChoiceField(choices=Campus_choices, widget=forms.RadioSelect())
#	cat_res = forms.ChoiceField(choices=Category_choices, widget=forms.RadioSelect())
#	classif_res = forms.ChoiceField(choices=Classification_choices, widget=forms.RadioSelect())
#	res_sf = forms.ChoiceField(choices=Source_fund_choices, widget=forms.CheckboxSelectMultiple())
#	amt_grant = forms.CharField(max_length=100)
#	res_stat = forms.ChoiceField(choices=Stat_choices, widget=forms.RadioSelect())
#	date_S = forms.DateField()
#	date_C = forms.DateField()
#	respub_stat = forms.ChoiceField(choices=Yes_no_Choices,widget=forms.RadioSelect())
#	J_name = forms.CharField(max_length=500,initial="")
#	J_vol = forms.CharField(max_length=500,initial="")
#	J_datepub = forms.DateField()
#	ipr_stat = forms.ChoiceField(choices=Yes_no_Choices, widget=forms.RadioSelect())
#	ipr_type = forms.ChoiceField(choices=IPR_Type_choices, widget=forms.RadioSelect())
#	ipr_DateAppl=forms.DateField()
#	ipr_DateApprv=forms.DateField()
#	ipr_pending=forms.ChoiceField(choices=Yes_no_Choices, widget=forms.RadioSelect())
#	res_abs=forms.CharField(widget=forms.Textarea)




#class KTMform(forms.ModelForm):
#	class Meta:
#		model = List_of_Res
#		prog_title = forms.CharField(max_length=1000)
