from django.db import models


class List_of_Res(models.Model):
	Yes_no_Choices = (('YES','YES'),('NO','NO'))
	Stat_choices = (("COMPLETED","Completed"),("ON_GOING","On-Going"))
	Campus_choices = (
		("APARRI","Aparri"),
		("LASAM","Lasam"),
		("LALLO","Lal-lo"),
		("SANCHEZ_MIRA","Sanchez Mira"),
		("CARIG","Carig"),
		("ANDREWS","Andrews"),
		("PIAT","Piat")
		)
	Category_choices = (
		("BASIC","Basic"),
		("APPLIED","Applied"),
		("PILOT_TESTING","Pilot Testing"),
		("TECHNOLOGY_PROMOTION_COMMERCIALIZATION","Technology Promotion / Commercialization")
		)
	Classification_choices = (
		("AGRICULTURE","Agriculture"),
		("BIOTECHNOLOGY","Biotechnology"),
		("ICT","ICT"),
		("HEALTH_PRODUCTS","Health Products"),
		("ALTERNATIVE_ENERGY","Alternative Energy"),
		("CLIMATE_CHANGE","Climate Change"),
		("ENVIRONMENT","Environment"),
		("SOCIO_ECONOMIC","Socio-economic"),
		("NATURAL_PRODUCTS","Natural Products"),
		("OTHER","Other")
		)
	Source_fund_choices = (
		("CSU","CSU"),
		("CHED","CHED"),
		("DA_BAR","DA-BAR"),
		("DOST","DOST"),
		("PCCARRD","PCCARRD"),
		("PCIERD","PCIERD"),
		("PCHRD","PCHRD"),
		("DA","DA"),
		("OTHER","Other")
		)
	IPR_Type_choices = (
		("PATENT","Patent"),
		("UTILITY_MODEL","Utility Model"),
		("TRADEMARK_TRADENAME","Trademark/Tradename"),
		("COPYRIGHT","Copyright"),
		("OTHER","Other")
		)
	prog_title = models.CharField(max_length=1000)
	proj_title = models.CharField(max_length=1000)
	stud_title = models.CharField(max_length=1000)
	prog_lead = models.CharField(max_length=300)
	stud_lead = models.CharField(max_length=300)
	co_res = models.TextField()
	res_site = models.TextField()
	campus = models.CharField(max_length=50,choices=Campus_choices,default='ANDREWS')
	category_res = models.CharField(max_length=50,choices=Category_choices,default='BASIC')
	classif_res = models.CharField(max_length=50,choices=Classification_choices,default='ICT')
	amt_granted = models.TextField()
	date_started = models.DateField()
	res_status = models.CharField(max_length=10, choices=Yes_no_Choices, default='YES')
	date_completed = models.DateField()
	res_SF = models.TextField(choices=Source_fund_choices,default='CSU')
	res_pubstat = models.CharField(max_length=5,choices=Yes_no_Choices, default='YES')
	res_JN = models.TextField()
	res_JV = models.CharField(max_length=100)
	date_pub = models.DateField()
	res_iprstat = models.CharField(max_length=10, choices=Yes_no_Choices, default='YES')
	apptype = models.CharField(max_length=100,choices=IPR_Type_choices,default='PATENT')
	date_appl = models.DateField()
	date_pprv = models.DateField()
	app_pending = models.CharField(max_length=10, choices=Yes_no_Choices, default='YES')
	res_abs = models.CharField(max_length=5)

