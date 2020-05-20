from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from database import *
from django.core.files.storage import FileSystemStorage
from random import randrange, randint
from database import SMS,mail
from datetime import *
import http.client
import smtplib


@csrf_exempt
def adminRegisteration(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['passw']
            type = request.POST['fname']
            mobile = request.POST['mobile']
            if email and password and type and mobile and ('@' in email) and (
                    str(mobile).isnumeric() == True) and str(
                type).isnumeric() == False:
                s = 'insert into admin values ("{}","{}","{}","{}")'.format(email, password, type, mobile)
                # print(s)

                result = Insert(s)
                # print(s)
                if result == 'success':
                    return redirect(adminview)
                else:
                    return render(request, 'adminRegistration.html',
                                  {'title': 'Admin Registration', 'message': 'Admin Already Exist'})
            else:
                return render(request, 'adminRegistration.html',
                              {'title': 'Admin Registration', 'message': 'Data is not valid'})
        else:
            return render(request, 'adminRegistration.html', {'title': 'Admin Registration'})
    else:
        return redirect(adminLogin)


def adminDelete(request):
    s = 'delete from admin where email="{}"'.format(request.GET['email'])
    result = Delete(s)
    return HttpResponse(result)


@csrf_exempt
def adminUpdate(request):
    if 'admin' in request.session:
        email = request.POST['email']
        type = request.POST['fname']
        mobile = request.POST['mobile']
        if type and mobile and ('@' in email) and (str(mobile).isnumeric() == True) and str(
                type).isnumeric() == False:
            s = 'update admin set type="{}",mobile="{}" where email="{}"'.format(type, mobile, email)
            # print(s)
            result = Update(s)
            return HttpResponse(result)
    else:
        return redirect(adminLogin)


def adminview(request):
    if 'admin' in request.session and request.session['admin']['type'] == 'Super-Admin':
        s = 'select * from admin'
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result:
            d = {}
            d['srno'] = count
            d['email'] = i[0]
            d['password'] = i[1]
            d['type'] = i[2]
            d['mobile'] = i[3]
            count += 1
            lt.append(d)
        return render(request, 'adminview.html', {'context': lt})
    else:
        return redirect(adminLogin)


@csrf_exempt
def adminLogin(request):
    if 'admin' in request.session:
        return redirect(alladmin)
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select * from admin where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result != None:
                request.session['admin'] = {'adminEmail': result[0], 'type': result[2], 'mobile': result[3]}
                return redirect(alladmin)
            else:
                return render(request, 'adminLogin.html',
                              {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
        else:
            return render(request, 'adminLogin.html',
                          {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
    return render(request, 'adminLogin.html', {'title': 'Admin Login'})


def adminChangePassword(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            s = 'select password from admin where email="{}"'.format(request.session['admin']['adminEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                u = 'update admin set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                             request.session['admin'][
                                                                                 'adminEmail'])
                result = Update(u)
                if result == 'success':
                    return HttpResponse(result)
                else:
                    return HttpResponse('Something went wrong. Try after sometime')
            else:
                return HttpResponse('Wrong Password; or Try after some time!!')
        return redirect(alladmin)
    else:
        return redirect(adminLogin)


def alladmin(request):
    if 'admin' in request.session:
        s = 'select * from bill group by email'
        result = Fetchall(s)
        return render(request, 'adminDashBoard.html', {"context": list(result)})
    else:
        return redirect(adminLogin)


def adminlogout(request):
    if 'admin' in request.session:
        request.session['admin'] = ''
        del request.session['admin']
    return redirect(adminLogin)


@csrf_exempt
def addgenre(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            genre = request.POST['genre']
            description = request.POST['description']
            # print(genre, description)
            if str(genre).isnumeric() == False:
                s = f'INSERT INTO genre(genreid, genre, description) VALUES (null ,"{genre}","{description}")'
                result = Insert(s)
                # print('result:- ', result)
                if result == 'success':
                    return redirect(viewgenre)
                else:
                    return render(request, 'addgenre.html', {"message": "Something went wrong. Try After some time!"})
            else:
                return render(request, 'addgenre.html', {"message": "Genre cannot be a numeric value. Fill valid data"})
        return render(request, 'addgenre.html')
    else:
        return redirect(adminLogin)


@csrf_exempt
def addcategory(request):
    if request.method == 'POST':
        file = request.FILES['photo']
        uploadname = str(randint(1, 1000)) + file.name
        catname = request.POST["category"]
        description = request.POST["description"]
        if str(catname).isnumeric() == False:
            s = "INSERT INTO category VALUES ('" + catname + "','" + description + "','" + uploadname + "')"
            result = Insert(s)
            if result == 'success':
                fs = FileSystemStorage()
                fs.save(uploadname, file)
                return redirect(viewcategory)
            else:
                return render(request, 'addcategory.html', {'message': 'Something went wrong!'})
        else:
            return render(request, 'addcategory.html', {'message': 'Invalid Data!'})
    return render(request, 'addcategory.html')


@csrf_exempt
def addvideos(request):
    if 'admin' in request.session:
        s = "select catname from category "
        result = Fetchall(s)
        listdata = []
        x = []
        for r in result:
            d = {"catname": r[0]}
            x.append(d)
        v = "select * from genre"
        result1 = Fetchall(v)
        # print(result1)
        y = []
        for r in result1:
            d = {"genreid": r[0], "genre": r[1], "description": r[2]}
            y.append(d)
        listdata.append(x)
        listdata.append(y)
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            cast = request.POST['cast']
            catname = request.POST['catname']
            rating = request.POST['rating']
            genre = request.POST['genre']
            photo = request.FILES['photo']
            uploadphoto = str(randint(1, 1000)) + photo.name
            videos = request.FILES['videos']
            uploadvideo = str(randint(1, 1000)) + videos.name
            # print(title, description, catname, cast, genre, photo, videos)
            if str(catname).isnumeric() == False and str(title).isnumeric() == False:
                k = "INSERT INTO videos (vid, title, description, catname, genreid, photo, movievideopath, moviecast, rating) VALUES (null ,'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    title, description, catname, genre, uploadphoto, uploadvideo, cast, rating)
                print(k)
                result2 = Insert(k)
                print(result2)
                if result2 == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadphoto, photo)
                    fs.save(uploadvideo, videos)
                    return redirect(viewMovies)
                else:
                    return render(request, 'addvideos.html', {'message': 'Something went wrong!', "ar": listdata})
            else:
                return render(request, 'addvideos.html', {'message': 'Invalid Data!', "ar": listdata})
        return render(request, 'addvideos.html', {"ar": listdata})
    else:
        return redirect(adminLogin)


@csrf_exempt
def addEpisodes(request):
    if 'admin' in request.session:
        s = "select vid,title from videos where catname='Tv Shows'"
        result = Fetchall(s)
        # print(result)
        x = []
        for r in result:
            d = {"vid": r[0], "title": r[1]}
            x.append(d)
        if request.method == 'POST':
            title = request.POST['title']
            name = request.POST['name']
            description = request.POST['description']
            cast = request.POST['cast']
            rating = request.POST['rating']
            videos = request.FILES['videopath']
            photo = request.FILES['photo']
            uploadphoto = str(randint(1, 1000)) + photo.name
            uploadvideo = str(randint(1, 1000)) + videos.name
            if str(cast).isnumeric() == False and str(name).isnumeric() == False:
                k = 'INSERT INTO episodes(eid, vid, name, description, videopath, photo, cast, rating) VALUES (null,"{}","{}","{}","{}","{}","{}","{}")'.format(
                    title, name, description, uploadvideo, uploadphoto, cast, rating)
                # print(k)
                result2 = Insert(k)
                # print(result2)
                if result2 == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadphoto, photo)
                    fs.save(uploadvideo, videos)
                    return redirect(viewEpisode)
                else:
                    return render(request, 'addEpisodes.html', {'message': 'Something went wrong!', "ar": x})
            else:
                return render(request, 'addEpisodes.html', {'message': 'Invalid Data!', "ar": x})
        return render(request, "addEpisodes.html", {"ar": x})
    else:
        return redirect(adminLogin)


def viewgenre(request):
    if 'admin' in request.session:
        s = "select * from genre"
        result = Fetchall(s)
        # print(result)
        listdata = []
        count = 0
        for r in result:
            count += 1
            d = {"genreid": r[0], "genre": r[1], "description": r[2], 'srno': count}
            listdata.append(d)
        return render(request, 'viewgenre.html', {"ar": listdata})
    else:
        return redirect(adminLogin)


def viewcategory(request):
    if 'admin' in request.session:
        s = "select * from category"
        result = Fetchall(s)
        # print(result)
        listdata = []
        count = 0
        for r in result:
            count += 1
            d = {"catname": r[0], "description": r[1], "photo": r[2], 'srno': count}
            listdata.append(d)
        return render(request, 'viewcategory.html', {"ar": listdata})
    else:
        return redirect(adminLogin)


def viewMovies(request):
    if 'admin' in request.session:
        s = "select catname from category "
        result = Fetchall(s)
        listdata = []
        x = []
        for r in result:
            d = {"catname": r[0]}
            x.append(d)
        v = "select * from genre"
        result1 = Fetchall(v)
        # print(result1)
        y = []
        for r in result1:
            d = {"genreid": r[0], "genre": r[1], "description": r[2]}
            y.append(d)
        listdata.append(x)
        listdata.append(y)
        t = "select * from videos"
        result2 = Fetchall(t)
        # print(result2)
        listdata1 = []
        for r in result2:
            d = {"vid": r[0], "title": r[1], "description": r[2], "catname": r[3], "genreid": r[4], "photo": r[5],
                 'moviecast': r[7], 'rating': r[8]}
            listdata1.append(d)
        return render(request, 'viewMovies.html', {'ar': listdata1, "ar1": listdata})
    else:
        return redirect(adminLogin)


def viewEpisode(request):
    if 'admin' in request.session:
        s = 'select * from episodes'
        result = Fetchall(s)
        x = []
        count = 0
        for row in result:
            count += 1
            k = 'select title from videos where vid="{}"'.format(row[1])
            result1 = Fetchone(k)
            d = {'srno': count, "name": row[2], "descp": row[3], 'photo': row[5], 'cast': row[6], 'rating': row[7],
                 'seriesname': result1[0], 'eid': row[0]}
            x.append(d)
        return render(request, "viewepisode.html", {"ar": x})
    else:
        return redirect(adminLogin)


def deletegenre(request):
    try:
        genreid = request.GET["q"]
        genrename = request.GET["genrename"]
        # print(genreid, genrename)
        s = "delete from genre where genreid='" + genreid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(genrename + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def deletecategory(request):
    try:
        categoryname = request.GET["categoryname"]
        s = "delete from category where catname='" + categoryname + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(categoryname + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


@csrf_exempt
def updateCategorySave(request):
    try:
        catname = request.POST['catname']
        description = request.POST['description']
        try:
            file = request.FILES['photo']
            uploadname = str(randint(1, 1000)) + file.name
            s = "UPDATE category SET description='{}',photo='{}' WHERE catname='{}'".format(description, uploadname,
                                                                                            catname)
            result = Update(s)
            fs = FileSystemStorage()
            fs.save(uploadname, file)
        except:
            s = "UPDATE category SET description='{}' WHERE catname='{}'".format(description, catname)
            result = Update(s)
        return HttpResponse(result)
    except:
        return redirect(http4o4page)


def deletevideos(request):
    try:
        vid = request.GET["vid"]
        videosname = request.GET['vidname']
        # print(videosname)
        s = "delete from videos where vid='" + vid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(videosname + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def updatevideos(request):
    try:
        if request.method == 'POST':
            vid = request.POST['vid']
            title = request.POST['title']
            description = request.POST['description']
            cast = request.POST['cast']
            catname = request.POST['catname']
            rating = request.POST['rating']
            genre = request.POST['genre']
            # print(title, description, catname, cast, genre)
            try:
                file = request.FILES['file']
                uploadname = str(randint(1, 1000)) + file.name
                s = 'UPDATE videos SET title="{}",description="{}",catname="{}",genreid="{}",photo="{}",moviecast="{}",rating="{}" WHERE vid="{}"'.format(
                    title, description, catname, genre, uploadname, cast, rating, vid)
                result = Update(s)
                if result == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadname, file)
            except:
                s = 'UPDATE videos SET title="{}",description="{}",catname="{}",genreid="{}",moviecast="{}",rating="{}" WHERE vid="{}"'.format(
                    title, description, catname, genre, cast, rating, vid)
                result = Update(s)
        return HttpResponse(result)
    except:
        return redirect(http4o4page)


def deleteEpisode(request):
    try:
        eid = request.GET["eid"]
        episodename = request.GET['episodename']
        # print(episodename)
        s = "delete from episodes where eid='" + eid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(episodename + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


@csrf_exempt
def updateEpisode(request):
    try:
        if request.method == 'POST':
            eid = request.POST['eid']
            name = request.POST['name']
            description = request.POST['description']
            cast = request.POST['cast']
            rating = request.POST['rating']
            # print(title, description, catname, cast, genre)
            try:
                file = request.FILES['file']
                uploadname = str(randint(1, 1000)) + file.name
                s = 'UPDATE `episodes` SET `name`="{}",`description`="{}",`photo`="{}",`cast`="{}",`rating`="{}" WHERE `eid`="{}"'.format(
                    name, description, uploadname, cast, rating, eid)
                result = Update(s)
                if result == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadname, file)
            except:
                s = 'UPDATE `episodes` SET `name`="{}",`description`="{}",`cast`="{}",`rating`="{}" WHERE `eid`="{}"'.format(
                    name, description, cast, rating, eid)
                result = Update(s)
        return HttpResponse(result)
    except:
        return redirect(http4o4page)


def view(request):
    if 'client' in request.session and request.session['client']['clienttype'] == 'subscribe':
        return redirect(browseview)
    else:
        return render(request, 'view.html')


def browseview(request):
    if 'client' in request.session:
        if request.session['client']['clienttype'] == 'subscribe':
            return render(request, 'browseview.html')
        else:
            return redirect(paymentoffer)
    else:
        return redirect(clientlogin)


def detail(request):
    if 'client' in request.session:
        if request.session['client']['clienttype'] == 'subscribe':
            # print(request.GET['q'])
            s = 'select * from videos where vid="{}"'.format(request.GET['q'])
            result = Fetchone(s)
            if result[3] == 'Movies':
                return render(request, 'detail.html', {'context': list(result), 'type': 'movie'})
            elif result[3] == 'Tv Shows':
                k = 'select * from episodes where vid="{}"'.format(result[0])
                result1 = Fetchall(k)
                lt = []
                count = 0
                for i in result1:
                    count += 1
                    d = {}
                    d['srno'] = count
                    d['name'] = i[2]
                    d['descp'] = i[3]
                    d['video'] = i[4]
                    d['photo'] = i[5]
                    d['cast'] = i[6]
                    d['rating'] = i[7]
                    lt.append(d)
                # print(lt)
                return render(request, 'detail.html', {'context': list(result), 'type': 'episode', 'season': lt})
        else:
            return redirect(paymentoffer)
    else:
        return redirect(clientlogin)


def browsedata(request):
    if request.GET['search'] == 'main':
        s = 'select * from genre'
        result = Fetchall(s)
        lt = []
        for i in result:
            k = {}
            d = 'select vid,title,photo from videos where genreid="{}"'.format(i[0])
            result1 = Fetchall(d)
            if result1 != ():
                k['key'] = i[0]
                k['genrename'] = i[1]
                lts = []
                for j in result1:
                    # print(j)
                    g = {}
                    g['videoid'] = j[0]
                    g['videotitle'] = j[1]
                    g['videophoto'] = j[2]
                    lts.append(g)
                k['video'] = lts
                lt.append(k)
        # print(lt)
    return JsonResponse(lt, safe=False)


def paymentoffer(request):
    if 'client' in request.session:
        return render(request, 'paymentoffer.html')
    else:
        return redirect(clientlogin)


@csrf_exempt
def clientlogin(request):
    if 'client' in request.session:
        return redirect(browseview)
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select * from clientregistration where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            print(result)
            if result:
                request.session['client'] = {'clientEmail': result[0], "clientPhone": result[4],
                                             "clientName": result[1], 'clienttype': result[3]}
                if result[3] == 'subscribe':
                    return redirect(screendisplay)
                else:
                    return redirect(paymentoffer)
            else:
                return render(request, 'clientlogin.html',
                              {'message': 'Email and Password is not correct'})
        else:
            return render(request, 'clientlogin.html',
                          {'message': 'Email and Password is not correct'})
    return render(request, 'clientlogin.html')


def clientRegistration(request):
    if 'client' in request.session:
        del request.session['client']
    if request.method == 'POST':
        email = request.POST['clientemail']
        password = request.POST['cpassw']
        fullname = request.POST['fname']
        mobile = request.POST['mobile']
        if email and password and fullname and mobile and ('@' in email) and (str(mobile).isnumeric() == True):
            s = 'insert into clientregistration values ("{}","{}","{}","{}","{}",null)'.format(email, fullname,
                                                                                               password,
                                                                                               'unsubscribe', mobile)
            # print(s)
            result = Insert(s)
            if result == 'success':
                return redirect(clientlogin)
            else:
                return render(request, 'clientregister.html', {'message': 'Technical Error or Email is already taken'})
        else:
            return render(request, 'clientregister.html', {'message': 'Data is not correct'})
    return render(request, 'clientregister.html')


def clientlogout(request):
    if 'client' in request.session:
        request.session['client'] == ''
        del request.session['client']
        return redirect(view)
    else:
        return redirect(view)


def clientChangePassword(request):
    if 'client' in request.session:
        if request.method == 'POST':
            s = 'select password from clientregistration where email="{}"'.format(
                request.session['client']['clientEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                if request.POST['cpassw'] == request.POST['npassw']:
                    u = 'update clientregistration set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                                              request.session['client'][
                                                                                                  'clientEmail'])
                    result = Update(u)
                    return HttpResponse(result)
                else:
                    return HttpResponse('Password Does not Match')
            else:
                return HttpResponse('Wrong Password.')
        else:
            return redirect(browseview)
    else:
        return redirect(browseview)


def person2(request):
    if request.method == 'POST':
        billid = request.session['bill']['billid']
        # print(billid)
        person1name = request.POST['person1name']
        person2name = request.POST['person2name']
        photo1 = request.FILES['photo1']
        photo2 = request.FILES['photo2']
        # print(billid,person1name,photo1.name)
        uploadphoto1 = str(randint(1, 1000)) + photo1.name
        uploadphoto2 = str(randint(1, 1000)) + photo2.name
        s = f'UPDATE `bill` SET `person1name`="{person1name}",`person1image`="{uploadphoto1}",`person2name`="{person2name}",`person2image`="{uploadphoto2}" WHERE `billid`="{billid}"'
        result = Update(s)
        if result == 'success':
            fs = FileSystemStorage()
            fs.save(uploadphoto1, photo1)
            fs.save(uploadphoto2, photo2)
            return redirect(thanksyou)
        else:
            return redirect(failpayment)
    return render(request, 'person2.html')


def person4(request):
    if request.method == 'POST':
        billid = request.session['bill']['billid']
        # print(billid)
        person1name = request.POST['person1name']
        person2name = request.POST['person2name']
        person3name = request.POST['person3name']
        person4name = request.POST['person4name']
        photo1 = request.FILES['photo1']
        photo2 = request.FILES['photo2']
        photo3 = request.FILES['photo3']
        photo4 = request.FILES['photo4']
        # print(billid,person1name,photo1.name)
        uploadphoto1 = str(randint(1, 1000)) + photo1.name
        uploadphoto2 = str(randint(1, 1000)) + photo2.name
        uploadphoto3 = str(randint(1, 1000)) + photo3.name
        uploadphoto4 = str(randint(1, 1000)) + photo4.name
        s = f'UPDATE `bill` SET `person1name`="{person1name}",`person1image`="{uploadphoto1}",`person2name`="{person2name}",`person2image`="{uploadphoto2}",`person3name`="{person3name}",`person3image`="{uploadphoto3}",`person4name`="{person4name}",`person4image`="{uploadphoto4}" WHERE `billid`="{billid}"'
        result = Update(s)
        if result == 'success':
            fs = FileSystemStorage()
            fs.save(uploadphoto1, photo1)
            fs.save(uploadphoto2, photo2)
            fs.save(uploadphoto3, photo3)
            fs.save(uploadphoto4, photo4)
            return redirect(thanksyou)
        else:
            return redirect(failpayment)
    return render(request, 'person4.html')


@csrf_exempt
def paymentBill(request):
    if 'client' in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            mobile = request.POST['mobile']
            total = request.POST['total']
            # print(email,mobile,total)
            date = datetime.today().now()
            s = 'INSERT INTO `bill`(`billid`, `datetime`, `email`, `total`, `status`, `mobile`) VALUES (null,"{}","{}","{}","{}","{}")'.format(
                date, email, total, 'unsubscribe', mobile)
            # print(s)
            result = Insert(s)
            if result == 'success':
                d = 'select billid,datetime from bill order by billid DESC'
                result1 = Fetchone(d)
                # print(result1)
                request.session['bill'] = {"billid": result1[0]}
                # print(request.session['bill'])
                return HttpResponse(result)


@csrf_exempt
def person1(request):
    if request.method == 'POST':
        billid = request.session['bill']['billid']
        # print(billid)
        person1name = request.POST['person1name']
        photo1 = request.FILES['photo']
        # print(billid,person1name,photo1.name)
        uploadphoto = str(randint(1, 1000)) + photo1.name
        s = f'UPDATE `bill` SET `person1name`="{person1name}",`person1image`="{uploadphoto}" WHERE `billid`="{billid}"'
        result = Update(s)
        if result == 'success':
            fs = FileSystemStorage()
            fs.save(uploadphoto, photo1)
            return redirect(thanksyou)
        else:
            return redirect(failpayment)
    return render(request, 'person1.html')


def thanksyou(request):
    try:
        if 'client' in request.session:
            del request.session['client']
        return render(request, 'thanksyou.html')
    except:
        return render(request, 'thanksyou.html')


def failpayment(request):
    return render(request, 'failpayment.html')


def subscribe(request):
    try:
        email = request.GET['email']
        status = request.GET['status']
        # print(email)
        s = f'UPDATE `bill` SET `status`="{status}" WHERE `email`="{email}"'
        result = Update(s)
        if result == 'success':
            d = f'UPDATE `clientregistration` SET `type`="{status}" WHERE `email`="{email}"'
            result1 = Update(d)
            if result1 == 'success':
                l = 'select password,mobile from clientregistration where email="{}"'.format(email)
                result2 = Fetchone(l)
                msg = 'Your Email is: "{}'.format(email)
                msg += '\n'
                msg += 'Password is: "{}" for your NetFlix Account'.format(result2[0])
                print(msg)
                try:
                    mail.send_Mail(email,msg)
                    msg = msg.replace(" ", "%20")
                    SMS.confirm_Msg(result2[1],msg)
                    return HttpResponse(result1)
                except:
                    return HttpResponse(result1)
        else:
            return HttpResponse(result)
    except:
        return redirect(http4o4page)


def screendisplay(request):
    if 'client' in request.session:
        if request.session['client']['clienttype'] == 'subscribe':
            s = 'select * from bill where email="{}"'.format(request.session['client']['clientEmail'])
            result = Fetchone(s)
            print(list(result))
            return render(request, 'screendisplay.html', {'context': list(result)})
    else:
        return redirect(clientlogin)


def allshows(request):
    if 'client' in request.session:
        try:
            search = request.GET['search']
            s = 'SELECT vid,title,photo FROM videos WHERE title LIKE "%{}%"'.format(search)
            print(s)
            content = "Search"
        except:
            s = 'select vid,title,photo from videos where catname="{}"'.format(request.GET['catname'])
            content = request.GET['catname']
        result = Fetchall(s)
        # print(list(result))
        lt = []
        for i in result:
            d = {}
            d['vid'] = i[0]
            d['title'] = i[1]
            d['photo'] = i[2]
            lt.append(d)
        # print(lt)
        return render(request, 'allshows.html', {'context': lt, 'videocat': content})


def searchlist(request):
    s = 'select title from videos'
    result = Fetchall(s)
    lt = []
    for i in result:
        lt.append(i[0])
    # print(lt)
    return JsonResponse(lt, safe=False)


def http4o4page(request):
    return render(request, '4o4page.html')


@csrf_exempt
def forgetpassword(request):
    if request.method == 'POST':
        status = request.POST['status']
        # print(status)

        email = ''
        phone = ''
        try:
            email = request.POST['email']
            phone = request.POST['phone']
        except:
            try:
                phone = request.POST['phone']
                email = ''
            except:
                email = request.POST['email']
                phone = ''
        if status == 'client':
            otp = randrange(10000, 99999)
            data=''
            if email != '' and phone != '':
                s = 'select email,mobile from clientregistration where email="{}" and mobile="{}"'.format(email, phone)
                d = 'UPDATE clientregistration SET otp="{}" WHERE email="{}" and mobile="{}"'.format(otp, email, phone)
                data = 'email-phone'
                # print(s)
                # print(d)
            elif email != '':
                s = 'select email from clientregistration where email="{}"'.format(email)
                d = 'UPDATE clientregistration SET otp="{}" WHERE email="{}"'.format(otp, email)
                data='email'
                # print(s)
                # print(d)
            else:
                s = 'select mobile from clientregistration where mobile="{}"'.format(phone)
                d = 'UPDATE clientregistration SET otp="{}" WHERE mobile="{}"'.format(otp, phone)
                data='phone'
                # print(s)
                # print(d)
            result = Fetchone(s)
            # print(result)
            if result != None:
                result1 = Update(d)
                # print(result1)
                if result1 == 'success':
                    request.session['otp'] = {'otp': otp, 'crendential': result[0], 'status': status}
                    msg = 'Your OTP is = ' + str(otp)
                    msg = msg.replace(" ", "%20")
                    if data == 'email-phone':
                        SMS.confirm_Msg(phone, msg)
                        mail.send_Mail(email,msg)
                    elif data == 'email':
                        mail.send_Mail(email, msg)
                    else:
                        SMS.confirm_Msg(phone, msg)
                    return HttpResponse(result1)
            else:
                return HttpResponse(result)
        elif status == 'admin':
            otp = randrange(10000, 99999)
            data = ''
            if email != '' and phone != '':
                s = 'select email,mobile from admin where email="{}" and mobile="{}"'.format(email, phone)
                d = 'UPDATE admin SET otp="{}" WHERE email="{}" and mobile="{}"'.format(otp, email, phone)
                data = 'email-phone'
                # print(s)
                # print(d)
            elif email != '':
                s = 'select email from admin where email="{}"'.format(email)
                d = 'UPDATE admin SET otp="{}" WHERE email="{}"'.format(otp, email)
                data='email'
                # print(s)
                # print(d)
            else:
                s = 'select mobile from admin where mobile="{}"'.format(phone)
                d = 'UPDATE admin SET otp="{}" WHERE mobile="{}"'.format(otp, phone)
                data='phone'
                # print(s)
                # print(d)
            result = Fetchone(s)
            # print(result)
            if result != None:
                result1 = Update(d)
                # print(result1)
                if result1 == 'success':
                    request.session['otp'] = {'otp': otp, 'crendential': result[0], 'status': status}
                    # print(request.session['otp'])
                    msg = 'Your OTP is = ' + str(otp)
                    if data=='email-phone':
                        SMS.confirm_Msg(phone,msg)
                        msg = msg.replace(" ", "%20")
                        mail.send_Mail(email,msg)
                    elif data=='email':
                        mail.send_Mail(email,msg)
                    else:
                        msg = msg.replace(" ", "%20")
                        SMS.confirm_Msg(phone,msg)
                    return HttpResponse(result1)
            else:
                print('select')
                return HttpResponse(result)
        return HttpResponse('success')
    else:
        return HttpResponse('error')


def forgetpage(request):
    if request.method == 'POST':
        otp = request.POST['otppage']
        print(otp)
        print(request.session['otp'])
        if str(request.session['otp']['otp']) == str(otp):
            return render(request, 'otpchangepassword.html')
        else:
            return render(request, 'forgetpage.html', {'message': 'otp is wrong'})
    return render(request, 'forgetpage.html')


def otpchangepassword(request):
    if request.method == "POST":
        print(request.session['otp'])
        status = request.session['otp']['status']
        if status == 'client':
            if '@' in str(request.session['otp']['crendential']):
                s = 'update clientregistration set password="{}", otp="{}" where email="{}"'.format(
                    request.POST['cpassw'], None, request.session['otp']['crendential'])
            else:
                s = 'update clientregistration set password="{}", otp="{}" where mobile="{}"'.format(
                    request.POST['cpassw'], None, request.session['otp']['crendential'])
            result = Update(s)
            if result == 'success':
                request.session['otp'] = ''
                del request.session['otp']
                return redirect(clientlogin)
            else:
                return render(request, 'otpchangepassword.html', {'message': result})
        elif status == 'admin':
            if '@' in str(request.session['otp']['crendential']):
                s = 'update admin set password="{}", otp="{}" where email="{}"'.format(request.POST['cpassw'], None,
                                                                                       request.session['otp'][
                                                                                           'crendential'])
            else:
                s = 'update admin set password="{}", otp="{}" where mobile="{}"'.format(request.POST['cpassw'], None,
                                                                                        request.session['otp'][
                                                                                            'crendential'])
            result = Update(s)
            if result == 'success':
                request.session['otp'] = ''
                del request.session['otp']
                return redirect(adminLogin)
            else:
                return render(request, 'otpchangepassword.html', {'message': result})
        else:
            return render(request, 'otpchangepassword.html', {'message': 'unidentified status'})
