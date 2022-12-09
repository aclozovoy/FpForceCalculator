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

// ADD Rpo TABLE VALUES TO INPUT BOX
$(document).ready(function(){
    $("#ComponentsTable tbody tr").click(function() {
        var RpoValue = $(this).children(".Rpo").text();

        $("#RpoBox").val(RpoValue);
    });
});