import re
from fastapi import HTTPException


#دانشجو
def stu_valid(stu):
    
    ScourseIds= stu.Scourseids.split(",")
    Lids= stu.LIDs.split(",")
    names= r"[آ-ی\s]+"
    stid= r"^(401|402|403)114150([01-99]{2})$"
    birth= r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    ids= r"([0-9]{6})\/([آ-ی])[0-9]{2}"
    id= r"^[1-9]\d{9}$"
    borncity= r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    department= r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی|شیمی|علوم انسانی)"
    major= r"(مهندسی کامپیوتر|مهندسی پلیمر|مهندسی مکانیک|مهندسی عمران|مهندسی معدن|مهندسی شیمی|مهندسی برق|مهندسی نفت)"
    cphone= r"^(09|\+989)(\d{9})$"
    hphone= r"^(0[1-9][0-9])([1-9]\d{7})$"
    married= r"(متاهل|مجرد)"
    def stu_id(ID):
        sum = 0 
        l = 10
        for i in range(0 , l - 1):
            c = ord(ID[i])
            c -= 48
            sum = sum + c * (l - i)
        r = sum % 11
        c = ord(ID[l - 1])
        c -= 48
        if r > 2:
            r = 11 - r
        if r == c:
            return True
        else:
            return False
        
    error_for_stu= {}
    if re.match(pattern= stid , string= stu.STID) == None or len(stu.STID) != 11:
        error_for_stu["STID"]= 'شماره دانشجویی نادرست است'

    if re.match(pattern= names , string= stu.Fname) == None or len(stu.Fname) > 10:
        error_for_stu["Fname"]= 'نام باید فقط باید فارسی و کمتر از 10 حرف باشند '

    if re.match(pattern= names , string= stu.Lname) == None or len(stu.Lname) > 10:
        error_for_stu["Lname"]= 'نام خانوادگی باید فقط باید فارسی و کمتر از 10 حرف باشند '

    if re.match(pattern= names , string= stu.fathername) == None or len(stu.fathername) > 10:
        error_for_stu["fathername"]= 'نام پدر باید فقط باید فارسی و کمتر از 10 حرف باشند '
        
    if re.match(pattern=birth , string= stu.birth) == None:
        error_for_stu["birth"]= 'تاریخ تولد وارد شده نادرست می باشد'

    if re.match(pattern=ids , string= stu.IDS) == None:
        error_for_stu["IDS"]= 'شماره سریال شناسنامه نادرست می باشد'

    if re.match(pattern= borncity , string= stu.borncity) == None:
        error_for_stu["borncity"]= 'شهر تولد باید مرکز یکی استانها باشد '
    
    if len(stu.address) > 100:
        error_for_stu["address"]= 'نشانی محل زندگی باید کمتر از 100 حرف باشد'

    if len(str(stu.zipcode)) != 10:
        error_for_stu["zipcode"]= 'کد پستی باید یک عدد 10 رقمی باشد'

    if re.match(pattern= cphone , string= stu.cphone) == None:
        error_for_stu["cphone"]= 'شماره تلفن همراه نادرست می باشد'
    
    if re.match(pattern= hphone , string= stu.hphone) == None:
        error_for_stu["hphone"]= ' شماره تلفن ثابت نادرست می باشد'

    if re.match(pattern= department , string= stu.department) == None:
        error_for_stu["department"]= 'دانشکده باید از دانشکده های مجاز باشد'

    if re.match(pattern= major , string= stu.major) == None:
        error_for_stu["major"]= 'رشته تحصیلی باید از رشته های دانشکده فنی و مهندسی باشد '

    if re.match(pattern= married , string= stu.married) == None:
        error_for_stu["married"]= 'فیلد وضعیت تاهل باید با کلمات متاهل یا مجرد کامل شود'
        
    if re.match(pattern= id , string= stu.ID) == None or stu_id(stu.ID) == False:
        error_for_stu["ID"]= 'شماره ملی وارد شده نادرست می باشد'

    for scourseid in ScourseIds:
        if len(scourseid) != 5 or scourseid.isdigit() == False:
            error_for_stu["ScourseIds"]= f'کد درس {scourseid} باید یک عدد 5 رقمی باشند و به وسیله کاما از همدیگر جدا شوند'  
    for lid in Lids:
        if len(lid) != 6 or lid.isdigit() == False:
            error_for_stu["LIDs"]= f'کد استاد ,{lid} باید یک عدد 6 رقم باشند و به وسیله کاما از همدیگر جدا شوند'

    if error_for_stu:
        raise HTTPException(status_code=400 , detail=error_for_stu)


#استاد
def ostad_valid(ostad):

    Lcourseid = ostad.lcourseids.split(",")
    names = r"[آ-ی\s]+"
    id = r"^[1-9]\d{9}$"
    birth = r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    borncity = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    department = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی|شیمی|علوم انسانی)"
    major = r"(مهندسی کامپیوتر|مهندسی پلیمر|مهندسی مکانیک|مهندسی عمران|مهندسی معدن|مهندسی برق|مهندسی نفت)"
    cphone = r"^(09|\+989)(\d{9})$"
    hphone = r"^(0[1-9][0-9])([1-9]\d{7})$"
    def ostad_id(ID):
        sum = 0 
        l = 10
        for i in range(0 , l - 1):
            c = ord(ID[i])
            c -= 48
            sum = sum + c * (l - i)
        r = sum % 11
        c = ord(ID[l - 1])
        c -= 48
        if r > 2:
            r = 11 - r
        if r == c:
            return True
        else:
            return False
        

    error_for_ostad= {}

    if len(str(ostad.LID)) != 6 :
        error_for_ostad["LID"]= 'کد استاد باید یک عدد 6 رقمی باشد'

    if re.match(pattern= names , string= ostad.Fname) == None or len(ostad.Fname) > 10:
        error_for_ostad["Name"]= 'نام باید فقط  فارسی و کمتر از 10 حرف باشد '

    if re.match(pattern= names , string= ostad.Lname) == None or len(ostad.Lname) > 10:
        error_for_ostad["FName"]= 'نام خانوادگی باید فقط فارسی و کمتر از 10 حرف باشد '

    if re.match(pattern= id , string= ostad.ID) == None or ostad_id(ostad.ID) == False:
        error_for_ostad["ID"]= 'شماره ملی نادرست می باشد'

    if re.match(pattern= department , string= ostad.department) == None:
        error_for_ostad["department"]= 'دانشکده باید یکی از دانشکده های مجاز باشد'

    if re.match(pattern= major , string= ostad.major) == None:
        error_for_ostad["major"]= 'رشته تحصیلی باید یکی از رشته های دانشکده فنی و مهندسی باشد '   

    if re.match(pattern=birth , string= ostad.Birth) == None:
        error_for_ostad["Birth"]= 'تاریخ تولد وارد شده نادرست می باشد'

    if re.match(pattern= borncity , string= ostad.borncity) == None:
        error_for_ostad["borncity"]= 'شهر تولد باید مرکز یکی استانها باشد '

    if len(ostad.address) > 100:
        error_for_ostad["address"]= 'آدرس محل زندگی باید کمتر از 100 حرف باشد'

    if len(str(ostad.zipcode)) != 10:
        error_for_ostad["zipcode"]= 'کد پستی باید یک عدد 10 رقمی باشد'

    if re.match(pattern= cphone , string= ostad.cphone) == None:
        error_for_ostad["cphone"]= 'شماره تلفن همراه نادرست می باشد'
    
    if re.match(pattern= hphone , string= ostad.hphone) == None:
        error_for_ostad["hphone"]= ' شماره تلفن ثابت نادرست می باشد'

    for lcourseids in Lcourseid:
        if len(lcourseids) != 5 or lcourseids.isdigit() == False:
            error_for_ostad["lcourseids"]=f'کد درس {lcourseids} باید یک عدد 5 رقمی باشند و به وسیله کاما از همدیگر جدا شوند'  

    if error_for_ostad:
        raise HTTPException(status_code= 400 , detail= error_for_ostad)


#درس
def cou_valida(cou):
    name = r"[آ-ی\s]+"
    department = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی|شیمی)"
    


    error_for_cou = {}
    if re.match(pattern= name , string= cou.Cname) == None or len(cou.Cname) >25:
        error_for_cou["Cname"]= 'نام درس باید فارسی و کمتر از 25 حرف باشد'
    
    if len(cou.CID) !=5:
        error_for_cou["CID"]= 'کد درس باید یک عدد 5 رقمی باشد'

    if re.match(pattern= department , string= cou.department) == None:
        error_for_cou["department"]= 'دانشکده باید از دانشکده های مجاز باشد'
    
    if not 1 <= cou.credit <= 4:
        error_for_cou["credit"]= 'واحد دروس باید یک عدد بین 1 تا 4 باشد'

    if error_for_cou:
        raise HTTPException(status_code= 400 , detail= error_for_cou)

