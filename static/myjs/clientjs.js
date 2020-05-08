function getdata(find) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            // console.log(output);
            crousel(output);
        }
    };
    xml.open('GET', 'browsedata?search=' + find, true);
    xml.send();
}

function crousel(data) {
    var t = '';
    for (var i of data) {
        var w = 0;
        // console.log(i);
        // console.log(i.key);
        t += `<p class="section-title text-white mt-5">${i.genrename}</p>`;
        t += `<div id="carouselExampleControls${i.key}" class="carousel slide" data-ride="carousel">`;
        t += `<div class="carousel-inner">`;
        // console.log(i.video.length);
        for (var s = 0; s < i.video.length;) {
            var b = '';
            for (var j = 0; j < 4; j++) {
                var videoindex = s;
                s++;
                // console.log(s);
                if (s > i.video.length) {
                    if (s + 1 % 4 == 0) {
                        // console.log(b);
                        // t += `<div class="carousel-item active"><div class="row">${b}</div></div>`
                        break;
                    } else {
                        //dummy card
                        b += `<div class="col-sm-3"></div>`;
                        // console.log("dummy");
                    }
                } else {
                    //actual video card
                    b += `<div class="col-sm-3"><a href="detail?q=${i.video[videoindex]['videoid']}"><img class="img-fluid" src="static/media/${i.video[videoindex]['videophoto']}" alt="slide"><div class="text-white">${i.video[videoindex]['videotitle']}</div></a></div>`;
                    // console.log(i.video[videoindex]['videophoto'] + " ---- actual");
                }
            }
            if (w == 0) {
                t += '<div class="carousel-item active"><div class="row">' + b + '</div></div>';
            } else {
                t += '<div class="carousel-item"><div class="row">' + b + '</div></div>';
            }
            w++;
            // console.log(t);
            // console.log("-------------------");
        }
        t += `</div>`;
        t += `<a class="carousel-control-prev" style="background: rgba(0,0,0,0.8);width: 2%" href="#carouselExampleControls${i.key}" role="button" data-slide="prev"><span class="carousel-control-prev-icon " aria-hidden="true"></span><span class="sr-only  text-danger">Previous</span></a>`;
        t += `<a class="carousel-control-next" style="background: rgba(0,0,0,0.8);width: 2%" href="#carouselExampleControls${i.key}" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Next</span></a>`;
        t += `</div>`
    }
    // console.log(t);
    document.getElementById('cat').innerHTML = t;
}


function payment(data, page) {
    var amount = data * 100;
    var options = {
        "key": "rzp_test_dRWiKHS7zr2Gki",
        "amount": amount,
        "name": "",
        "description": "",
        "image": "",
        "handler": function (response) {
            //alert(response.razorpay_payment_id);
            if (response.razorpay_payment_id == "") {
                // alert('Failed');
                window.location.href = "failpayment";
            } else {
                var formdata = new FormData();
                formdata.append('email', $('#clientemail').val());
                formdata.append('mobile', $('#clientphone').val());
                formdata.append('total', data);
                var httpreg = new XMLHttpRequest();
                httpreg.onreadystatechange = function () {
                    if (this.status == 200 && this.readyState == 4) {
                        var output = this.response;
                        console.log(output);
                        if (output == 'success') {
                            window.location.href = page;
                        }
                    }

                };
                httpreg.open("POST", "paymentBill", true);
                httpreg.send(formdata);
            }
        },
        "prefill": {
            "name": "",
            "email": $('#clientemail').val(),
            "contact": $('#clientphone').val()
        },
        "notes": {
            "address": ""
        },
        "theme": {
            "color": "#F37254"
        }
    };
    var rzp1 = new Razorpay(options);
    rzp1.open();
}


function changepassword() {
    var controls = document.getElementById("ChangePassword").elements;
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
            var output = this.response;
            if (output == 'success') {
                $('#mymodalchangepassword').modal('hide');
            } else {
                document.getElementById('error').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'
            }
            // $('#mymodalchangepassword').modal('hide');
            // window.location.href = 'adminview';
        }
    };
    xml.open('POST', 'changepassword', true);
    xml.send(formdata)

}


function searchlist() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            console.log(output);
            $('#search').autocomplete({
                source: output,
                minLength: 2
            })
        }
    };
    xml.open('GET', 'searchlist', true);
    xml.send()

}



function forgetpassword(status) {
    var formdata = new FormData();
    var xml = new XMLHttpRequest();
    var output = '';
    if (status == 'client') {
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
                        $('#forgetpassword').modal('hide');
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
                        $('#forgetpassword').modal('hide');
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
                        $('#forgetpassword').modal('hide');
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