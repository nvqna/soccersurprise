
var table = $('#dataTable').DataTable({
    "paging": true,
    "ordering": true,
    "order": [[4,"desc"]],
  });

 $(document).ready(function() {
    $.fn.dataTable.ext.search.push(
       function (settings, data, dataIndex) {
           var min = $('#datepicker_from').datepicker('getDate');
           var max = $('#datepicker_to').datepicker('getDate');

           var startDate = new Date($.trim(data[0])); // this is the date column
           if (min == null && max == null) return true;
           if (min == null && startDate <= max) return true;
           if (max == null && startDate >= min) return true; 
           if (startDate <= max && startDate >= min) return true;
           return false;
       }
   );

   $('#datepicker_from').datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });
   $('#datepicker_to').datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });
   var table = $('#dataTable').DataTable();

   // Event listener to the two range filtering inputs to redraw on input
   $('#datepicker_from,#datepicker_to').change(function () {
       table.draw();

   });

   $(".clear-date-filter").on("click", function() {
    $('#datepicker_from').val("").datepicker("update");
    $('#datepicker_to').val("").datepicker("update");
   });

} );