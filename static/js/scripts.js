// SHOW AND HIDE INPUT BOXES FOR HEIGHT FACTOR
$(document).ready(function(){
    $("input[name$='HfRadio']").click(function(){
        var RadioValue = $(this).val();

        if (RadioValue=='PeriodKnown') {
            $("#ZInput").show("slow");
            $("#HInput").show("slow");
            $("#TaInput").show("slow");
        } else if (RadioValue=='PeriodUnknown') {
            $("#ZInput").show("slow");
            $("#HInput").show("slow");
            $("#TaInput").hide("slow")
        } else if (RadioValue=='BelowGrade') {
            $("#ZInput").hide("slow");
            $("#HInput").hide("slow");
            $("#TaInput").hide("slow");
            // $("#ZInput").attr('disabled', 'disabled');
            // $("#HInput").attr('disabled', 'disabled');
            // $("#TaInput").attr('disabled', 'disabled');
        }
    })
});

// LIVE CALCULATION OF R_mu FACTOR
$(document).ready(function(){
    $('[name=R]').add('[name=Omega0]').change(function() {
        // alert('R or Omega0 changed!');
        var R = parseFloat($('[name=R]').val());
        var Omega0 = parseFloat($('[name=Omega0]').val());

        if (R>0 & Omega0>0) {
            // alert('R or Omega0 are both valid!');
            var R_mu = (1.1*R/Omega0)**(0.5);
            $('[name=R_mu]').val(R_mu.toFixed(2));
        } else {
            $('[name=R_mu]').val('');
        }

    });
});

// LIVE CALCULATION OF Hf FACTOR
$(document).ready(function(){
    $('[name=z]').add('[name=h]').add('[name=Ta]').add('[name$=HfRadio]').change(function() {
        // alert('Hf inputs changed!');
        var z = parseFloat($('[name=z]').val());
        var h = parseFloat($('[name=h]').val());
        var Ta = parseFloat($('[name=Ta]').val());
        var HfRadio = $("input[name$='HfRadio']:checked").val();

        if (z>0 & h>0 & Ta>0 & HfRadio=='PeriodKnown') {

            var a1 = Math.min(1/Ta, 2.5);
            var a2 = Math.max(1 - (0.4/Ta)**2, 0);
            var Hf = 1 + a1*(z/h) + a2*(z/h)**10;

            $('[name=Hf]').val(Hf.toFixed(2));

        } else if (z>0 & h>0 & HfRadio=='PeriodUnknown') {

            var Hf = 1 + 2.5*(z/h);

            $('[name=Hf]').val(Hf.toFixed(2));

        } else if (HfRadio=='BelowGrade') {

            var Hf = 1

            $('[name=Hf]').val(Hf.toFixed(2));

        } else {
            $('[name=Hf]').val('');
        }

    });
});

// HIGHLIGHT TABLE ROW WHEN CLICKED
$(document).ready(function(){
    $("#ComponentsTable tbody tr").click(function() {
        $(this).addClass("table-success").siblings().removeClass('table-success');
    })
});

// ADD Car, Rpo, and Oop TABLE VALUES TO INPUT BOX
$(document).ready(function(){
    $("#ComponentsTable tbody tr").click(function() {

        // Car
        var HfRadio = $("input[name$='HfRadio']:checked").val();

        if (HfRadio=='PeriodKnown' || HfRadio=='PeriodUnknown') {
            var CarValue = $(this).children(".CarA").text();
        } else if (HfRadio=='BelowGrade') {
            var CarValue = $(this).children(".CarB").text();
        }

        $("#CarBox").val(CarValue);

        // Rpo
        var RpoValue = $(this).children(".Rpo").text();
        $("#RpoBox").val(RpoValue);

        // Oop
        var OopValue = $(this).children(".Oop").text();
        $("#OopBox").val(OopValue);
    });
});


// LIVE CALCULATION OF Fp
$(document).click(function() {
    var Sds = parseFloat($('[name=Sds]').val());
    var Wp = parseFloat($('[name=Wp]').val());
    // var Ip = parseFloat($("input[name$='IpRadio']:checked").val()); // Radio
    var Ip_Radio = $("input[name$='IpRadio']:checked").val(); // Radio
    var R_mu = parseFloat($('[name=R_mu]').val());
    var Hf = parseFloat($('[name=Hf]').val());
    var Car = parseFloat($('[name=Car]').val());
    var Rpo = parseFloat($('[name=Rpo]').val());
    var Oop = parseFloat($('[name=Oop]').val());
    // alert(Ip);

    if (Sds>0 & Wp>0 & R_mu>0 & Hf>0 & Car>0 & Rpo>0 & Oop>0) {
        // alert('In the loop');
        // alert(Ip)
        if (Ip_Radio=='Ip1.0') {
            var Ip = 1.0;
        } else if (Ip_Radio=='Ip1.5') {
            var Ip = 1.5;
        }

        var X_calc = (Hf/R_mu) * (Car/Rpo);
        var X = Math.min( Math.max( X_calc, 0.3), 1.6);

        var Fp = X * Sds * Ip * Wp;
        var OopFp = Oop * Fp;
        
        $('#XBox').val(X.toFixed(2) + '*SdsIpWp');
        $('#FpBox').val(Fp.toFixed(1));
        $('#OopFpBox').val(OopFp.toFixed(1));
    }
});

// CHANGE UNITS
$(document).ready(function(){
    $("#units_in").click(function() {

        if ($(this).text()=='lb') {
            $(this).text('psf');
            $('[name=units_out]').text('psf');
        } else if ($(this).text()=='psf') {
            $(this).text('k');
            $('[name=units_out]').text('k');
        } else if ($(this).text()=='k') {
            $(this).text('ksf');
            $('[name=units_out]').text('ksf');
        } else if ($(this).text()=='ksf') {
            $(this).text('lb');
            $('[name=units_out]').text('lb');
        }
    });
    $("#units_in").hover(function() {
        $(this).css('cursor','pointer')
    });
});