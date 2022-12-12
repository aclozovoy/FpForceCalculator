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

// ADD Car AND Rpo TABLE VALUES TO INPUT BOX
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
    });
});


