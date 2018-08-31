$(document).ready(function () {

            $("#CycleList").append('<option>' +"Cycle 29" + '</option>');
            $("#releaseStatus").hide();
            $("#branchStatus").hide();
            $("#jobSetting").hide();
            $("#buildLog").hide();

            $("#branchStatusLink").click(function(){
                $("#releaseStatus").hide();
                $("#jobSetting").hide();
                $("#buildLog").hide();
                $("#branchStatus").toggle();
            });

            $("#releaseStatusLink").click(function(){
                $("#branchStatus").hide();
                $("#jobSetting").hide();
                $("#buildLog").hide();
                $("#releaseStatus").toggle();
            });

            $("#jobSettingLink").click(function(){
                $("#releaseStatus").hide();
                $("#branchStatus").hide();
                $("#buildLog").hide();
                $("#jobSetting").toggle();
            });

            $("#buildLogLink").click(function(){
                $("#releaseStatus").hide();
                $("#branchStatus").hide();
                $("#jobSetting").hide(); 
                $("#buildLog").toggle();
            });

            });