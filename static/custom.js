$(document).ready(function () {
            $("#CycleList").append('<option>' +"Cycle 29" + '</option>');
            $("#releaseStatus").hide();
            $("#branchStatus").hide();
            $("#jobSetting").hide();
            $("#buildLog").hide();

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