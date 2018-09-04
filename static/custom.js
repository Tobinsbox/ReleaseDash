$(document).ready(function () {
            $("#currentCycle").html("Current Cycle: "+$("#cycleRange").val());
            $("#minMaxRange").html("Min:20   Max:99");
            $("#releaseStatus").hide();
            $("#branchStatus").hide();
            $("#jobSetting").hide();
            $("#buildLog").hide();

            curVal=$("#cycleRange").val();
            $("#currentCycle").html("Current Cycle: "+curVal);
            for(var i=0;i<=5;i++){
                $("#cycleList").append($("<p></p>").text("Cycle "+(Number(curVal)-i)))
            }

            $(".name").click(function () {
                $(this).siblings().removeClass('active');
                $(this).toggleClass("active");

            })


            $("#branchStatusLink").click(function(){
                $("#branchStatus").siblings('div').hide();
                $("#branchStatus").toggle();
            });

            $("#releaseStatusLink").click(function(){
                $("#releaseStatus").siblings('div').hide();
                $("#releaseStatus").toggle();
            });

            $("#jobSettingLink").click(function(){
                $("#jobSetting").siblings('div').hide();
                $("#jobSetting").toggle();
            });

            $("#buildLogLink").click(function(){
                $("#buildLog").siblings('div').hide();
                $("#buildLog").toggle();
            });

            });