var app = angular.module('aaw')
app.controller('retrivalController', function () {
    var _this = this;
    _this.filterByHLC = filterByHLC;
    $.ajax({
        dataType: "json",
        url: "/api/retrival",
        data: "",
        success: function (data) {
            // Data needs a new field: file_link
            for(var i = 0; i < data.length; i ++){
                var record = data[i];
                record.file_link = "/api/serve/?hlc="+record.hlc_cat+"&file_name="+record.doc_name;
            }
            var jsondata = data;
            $('#table').bootstrapTable({
                //Assigning data to table
                data: jsondata
            });
        }
    });
    function filterByHLC() {
        var filterYear, deptname,hlccategory,filter,filter1,table,tr,td;
        hlccategory = document.getElementById("hlc");
        filter = hlccategory.value.toLowerCase();
        deptname = document.getElementById("dept");
        filter1 = deptname.value.toUpperCase();
        filterYear = document.getElementById("year").value;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");
        td = table.getElementsByTagName("td");
        for (var i = 1; i < tr.length; i++) {
            dept_row = tr[i].getElementsByTagName("td")[3];
            year_row = tr[i].getElementsByTagName("td")[4];
            hlc_row = tr[i].getElementsByTagName("td")[6];
            if (dept_row && year_row && hlc_row ) {
                if (dept_row.innerHTML.indexOf(filter1) > -1 &&  
                    hlc_row.innerHTML.indexOf(filter) > -1 && 
                    year_row.innerHTML.indexOf(filterYear) > -1)  {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    };
});
