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
        }
    })
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


