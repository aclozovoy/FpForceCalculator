$(document).ready(function(){
    $("input[name$='HfRadio']").click(function(){
        var test = $(this).val();

        if (test=='PeriodKnown') {
            $("#ZInput").show("slow");
            $("#HInput").show("slow");
            $("#TaInput").show("slow");
        } else if (test=='PeriodUnknown') {
            $("#ZInput").show("slow");
            $("#HInput").show("slow");
            $("#TaInput").hide("slow")
        } else if (test=='BelowGrade') {
            $("#ZInput").hide("slow");
            $("#HInput").hide("slow");
            $("#TaInput").hide("slow")
        }

    })

})