function deletegenre(genreid, genrename) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'viewgenre'
            }
        };
        xml.open('GET', 'deletegenre?q=' + genreid + "&genrename=" + genrename, true);
        xml.send()
    }
}

function deletecategory(categoryname) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'viewcategory'
            }
        };
        xml.open('GET', 'deletecategory?categoryname=' + categoryname, true);
        xml.send()
    }
}

function editcategorymodel(data) {
    $('#up_catname').val(data.catname);
    $('#catDescp').val(data.description);
    $("#photo").attr({"src": "static/media/" + data.photo});
    $('#myUpdateCategoryModel').modal('show');
}

function updateCat() {
    var form = new FormData();
    form.append('catname', $('#up_catname').val());
    form.append('description', $('#catDescp').val());
    form.append('photo', document.getElementById('file').files[0]);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output == 'success') {
                alert("Updated " + this.response);
                $('#myUpdateCategoryModel').modal('hide');
                window.location.href = 'viewcategory'
            } else {
                document.getElementById('error').innerHTML = 'Something went wrong.Try after some time'
            }
        }
    };
    xml.open('POST', 'updateCategorySave', true);
    xml.send(form);
}

function deletevideos(vid, vidname) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'viewMovies'
            }
        };
        xml.open('GET', 'deletevideos?vid=' + vid + "&vidname=" + vidname, true);
        xml.send()
    }
}

function editvideomodel(data) {
    $('#title').val(data.title);
    $('#description').val(data.description);
    $('#cast').val(data.moviecast);
    $('#catname').val(data.catname);
    $('#rating').val(data.rating);
    $('#genre').val(data.genreid);
    $("#photo").attr({"src": "static/media/" + data.photo});
    $('#vid').val(data.vid);
    $('#myModaleditvideo').modal('show');

}

function updatevideos() {
    var controls = document.getElementById("myformeditmodal").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response;
            alert(output);
            if (output == 'success') {
                $("#myModaleditvideo").modal('hide');
                window.location.href = 'viewMovies'
            } else {
                document.getElementById('error').innerHTML = 'Something is wrong. Try After sometimes!!'
            }
            // window.location.href = '';
        }

    };
    httpreg.open("POST", "updatevideos", true);
    httpreg.send(formdata);

}


function deleteEpisode(eid, episodename) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'viewEpisode'
            }
        };
        xml.open('GET', 'deleteEpisode?eid=' + eid + "&episodename=" + episodename, true);
        xml.send()
    }
}


function editEpisodemodel(data) {
    document.getElementById('title').innerHTML = data.seriesname;
    $('#name').val(data.name);
    $('#description').val(data.descp);
    $('#cast').val(data.cast);
    $('#rating').val(data.rating);
    // $('#rating').val(data.rating);
    // $('#genre').val(data.genreid);
    $("#photo").attr({"src": "static/media/" + data.photo});
    $('#eid').val(data.eid);
    $('#myModaleditEpisode').modal('show');
}

function updateEpisode() {
    var controls = document.getElementById("myform").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response;
            alert(output);
            if (output == 'success') {
                $("#myModaleditEpisode").modal('hide');
                window.location.href = 'viewEpisode'
            } else {
                document.getElementById('error').innerHTML = 'Something is wrong. Try After sometimes!!'
            }
            // window.location.href = '';
        }

    };
    httpreg.open("POST", "updateEpisode", true);
    httpreg.send(formdata);

}


function changeadminpassword() {
    var controls = document.getElementById("adminChangePassword").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response;
            alert(output);
            if (output == 'success') {
                $("#mymodalchangepassword").modal('hide');

            } else {
                document.getElementById('error').innerHTML = output;
            }
            for (var i = 0; i < controls.length; i++) {
                if (controls[i].type == "file") {
                    controls[i].files[0]="";
                } else {
                    controls[i].value="";
                }
            }
        }

    };
    httpreg.open("POST", "adminChangePassword", true);
    httpreg.send(formdata);
}


function deleteadmin(email) {
    alert(email);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.response);
            window.location.href = 'adminview'
        }
    };
    xml.open('GET', 'adminDelete?email=' + email, true);
    xml.send()
}

function updatemodel(data) {
    // alert(data);
    $('#email').val(data.email);
    $('#fname').val(data.type);
    $('#mobile').val(data.mobile);
    // $('#email').val(data.password);
    $('#updateadminmodel').modal('show');
}


function updateAdmin() {
    var controls = document.getElementById("myform").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            $('#updateadminmodel').modal('hide');
            window.location.href = 'adminview';
        }
    };
    xml.open('POST', 'adminUpdate', true);
    xml.send(formdata)
}


function subscribe(status,email) {
    alert(status)
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output=='success'){
                window.location.href = 'alladmin';
            }else{
                alert(output)
            }
        }
    };
    xml.open('GET', 'subscribe?status='+status+"&email="+email, true);
    xml.send()
}

function forgetpassword(status) {
    var formdata = new FormData();
    var xml = new XMLHttpRequest();
    var output = '';
    if (status == 'admin') {
        if (document.getElementById('otpemail').value != "" && document.getElementById('otpphone').value != "") {
            formdata.append('status', status);
            formdata.append('email', document.getElementById('otpemail').value);
            formdata.append('phone', document.getElementById('otpphone').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'

                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)

        } else if (document.getElementById('otpemail').value != "") {
            alert(document.getElementById('otpemail').value);
            formdata.append('status', status);
            formdata.append('email', document.getElementById('otpemail').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'
                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)

        } else if (document.getElementById('otpphone').value != "") {
            alert(document.getElementById('otpphone').value);
            formdata.append('status', status);
            formdata.append('phone', document.getElementById('otpphone').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'
                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)
        } else {
            document.getElementById('otperror').innerHTML = '<div class="alert alert-danger">Please Fill any field</div>'
        }
    }
}


